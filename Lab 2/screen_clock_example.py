import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from time import strftime, sleep
from adafruit_rgb_display.rgb import color565
import webcolors

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

# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()


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
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
x = 0

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py
    # Setting Time Variable
    y = top
    Month = "10"
    Day = "1"
    Year = "2021"
    Time = strftime("%H:%M:%S")
    Holiday = ("Holiday")
    days_until = 0
    Screencolor = ("#FFFFFF")
    # setting up holidays based on month and date
    if Month == "09":
       days_until = str(29 - int(Day))
       Holiday = ("your birthday!")
       Screencolor = "#FF75DE"
    if Month == "10": 
       if (int(Day))<5:
            days_until = str(5 - int(Day))
            Holiday = ("Sydney's birthday!")
            Screencolor = "#75E6FF"
       elif (int(Day))<=27:
            days_until = str(27 - int(Day))
            Holiday = ("Sophie's birthday!")
            Screencolor = "#C375FF"
       elif (int(Day))<=31:
            days_until = str(31 - int(Day))
            Holiday = ("Halloween!")
            Screencolor = "#FFB375"
    if Month == "11": 
       if (int(Day))<25:
            days_until = str(25 - int(Day))
            Holiday = ("Thanksgiving!")
            Screencolor = "#BF3F00"
    if Month == "12":
       if (int(Day))<25:
            days_until = str(25 - int(Day))
            Holiday = ("Christmas!")
            Screencolor = "#FF0000"
       else:
            days_until = str(31 - int(Day))
            Holiday = ("New Years Eve!")
            Screencolor = "#C2C2C2"
    if days_until == "0":
       if Holiday == "Holiday":
            draw.text((x, y), Time, font = font, fill = Screencolor)
            y += font.getsize(Time)[1]
            draw.text((x, y), "There are no more holidays this month", font = font, fill = Screencolor)
            sleep(1)
       else:
            draw.text((x, y), Time, font = font, fill = Screencolor)
            y += font.getsize(Time)[1]
            draw.text((x, y), "Today is " + Holiday, font = font, fill = Screencolor)
            sleep(1)
    else:
       draw.text((x, y), Time, font = font, fill = Screencolor)
       y += font.getsize(Time)[1]
       draw.text((x, y), "There are "+ days_until, font = font, fill = Screencolor)
       y += font.getsize(Time)[1]
       draw.text((x, y), "days until " + Holiday, font = font, fill = Screencolor)
       sleep(1)
    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
