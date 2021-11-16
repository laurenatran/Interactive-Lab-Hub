import paho.mqtt.client as mqtt
import uuid
import busio
import board
import time
import adafruit_ssd1306
from adafruit_bus_device.i2c_device import I2CDevice
from struct import pack, unpack
from PIL import Image, ImageDraw, ImageFont


def draw_text(text):
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    # Draw a white background
    font = ImageFont.load_default()

    # Draw Some Text
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    (font_width, font_height) = font.getsize(text)
    draw.text(
        (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
        text,
        font=font,
        fill=255,
    )
    oled.image(image)
    oled.show()

def read_register(dev, register, n_bytes=1):
    # write a register number then read back the value
    reg = register.to_bytes(1, 'little')
    buf = bytearray(n_bytes)
    with dev:
        dev.write_then_readinto(reg, buf)
    return int.from_bytes(buf, 'little')


DEVICE_ADDRESS = 0x6f  # device address of our button
STATUS = 0x03 # reguster for button status
AVAILIBLE = 0x1
BEEN_CLICKED = 0x2
IS_PRESSED = 0x4


# The follow is for I2C communications
i2c = busio.I2C(board.SCL, board.SDA)
device = I2CDevice(i2c, DEVICE_ADDRESS)

oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
oled.fill(0)
# we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
oled.show()
WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 5


# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')
#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)
channels = ['select ch', 'ch> emergency', 'ch> bathroom 1', 'ch> bathroom 2','ch> emergency','ch> food 1', ]
messages = ['msg> Help!!!',
            'msg> dance!',
            'line is 0-10 people',
            'line is 10-25 people',
            'line is 25-40 people',
            'line is greater than 40 people',
            'help needed']
channel_state = 0
message_state = 0
pressed_since = 0
prev_time = 0
counter = 10
short_press, long_press = False, False
mode = 0
while True:

    btn_status = read_register(device, STATUS)
    # check if button pressed
    if (btn_status & IS_PRESSED) != 0:
        if abs(prev_time - time.time()) < 1:
            pressed_since = pressed_since + time.time() - prev_time
            prev_time = time.time()
            print("prev_time", pressed_since)
        prev_time = time.time()
        time.sleep(0.2)
        print("Button pressed")
        continue
    else:
        if pressed_since < 2 and pressed_since > 0:
            if mode == 0:
                channel_state += 1
                channel_state = channel_state % 5
            else:
                message_state += 1
                message_state = message_state % 5

            # mode = 0
        elif pressed_since >= 3:
            #message_state += 1
            #message_state = message_state % 5
            mode += 1
            mode = mode % 3
        pressed_since = 0
        prev_time = 0

    cmd = channels[channel_state]
    if ' ' in cmd:
        print('sorry white space is a no go for topics')
    else:
        topic = f"IDD/{cmd}"
        print(f"now writing to topic {topic}")
        if True:
            val = messages[message_state]
            if val == 'new-topic':
                break
            else:
                client.publish(topic, val)
    if mode == 0:
        draw_text(channels[channel_state])
    elif mode == 1:
        draw_text(messages[message_state])
    elif mode == 2:
        draw_text("msg sent")
