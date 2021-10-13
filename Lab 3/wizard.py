import busio
import board
import time
from adafruit_bus_device.i2c_device import I2CDevice
from struct import pack, unpack
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789


subprocess.call(["./wizardvoice.sh"])

DEVICE_ADDRESS = 0x6f  # device address of our button
STATUS = 0x03 # reguster for button status
AVAILIBLE = 0x1
BEEN_CLICKED = 0x2
IS_PRESSED = 0x4


# The follow is for I2C communications
i2c = busio.I2C(board.SCL, board.SDA)
device = I2CDevice(i2c, DEVICE_ADDRESS)

def write_register(dev, register, value, n_bytes=1):
    # Write a wregister number and value
    buf = bytearray(1 + n_bytes)
    buf[0] = register
    buf[1:] = value.to_bytes(n_bytes, 'little')
    with dev:
        dev.write(buf)

def read_register(dev, register, n_bytes=1):
    # write a register number then read back the value
    reg = register.to_bytes(1, 'little')
    buf = bytearray(n_bytes)
    with dev:
        dev.write_then_readinto(reg, buf)
    return int.from_bytes(buf, 'little')

# clear out LED lighting settings. For more info https://cdn.sparkfun.com/assets/learn_tutorials/1/1/0/8/Qwiic_Button_I2C_Register_Map.pdf
write_register(device, 0x1A, 1)
write_register(device, 0x1B, 0, 2)
write_register(device, 0x19, 0)

filler_words = 0

##########################
# setting up display
##########################

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True


#######################################

while True:
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    # drawing text 
    y = top
    line1 = "You used"
    line2 = "4"
    line3 = "filler words"
    draw.text((x, y), line1, font=font, fill="#FFFFFF")
    y += font.getsize(line1)[1]
    draw.text((x, y), line2, font=font, fill="#FFFFFF")
    y += font.getsize(line1)[1]
    draw.text((x, y), line3, font=font, fill="#FFFFFF")

     # Display image.
    disp.image(image, rotation)
    time.sleep(0.1)


    try:
        # get the button status
        btn_status = read_register(device, STATUS)
        #print(f"AVAILIBLE: {(btn_status&AVAILIBLE != 0)} BEEN_CLICKED: {(btn_status&BEEN_CLICKED != 0)} IS_PRESSED: {(btn_status&IS_PRESSED != 0)}")
        # if pressed light LED
        if (btn_status&IS_PRESSED) !=0:
            write_register(device, 0x19, 255)
            filler_words = filler_words + 1
        # otherwise turn it off
        else:
            write_register(device, 0x19, 0)
        # don't slam the i2c bus
        time.sleep(0.1)

    except KeyboardInterrupt:
        # on control-c do...something? try commenting this out and running again? What might this do
        write_register(device, STATUS, 0)
        break

print(filler_words)

