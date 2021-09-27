import digitalio
import board
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import webcolors
import time
import subprocess
from PIL import Image, ImageDraw, ImageFont
from time import strftime, sleep


# The display uses a communication protocol called SPI.
# SPI will not be covered in depth in this course. 
# you can read more https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # the rate  the screen talks to the pi


# Create the ST7789 display:
display = st7789.ST7789(
    board.SPI(),
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
height = display.width  # we swap height/width to rotate it to landscape!
width = display.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
display.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0
y = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)


# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True




# Main loop:
while True:
   # draw.rectangle((0, 0, width, height), outline=0, fill=0)
   # display.image(image, rotation)
    padding = -2
    top = padding
    bottom = height - padding
    x = 0
    y = 0 
    Time = strftime("%H:%M:%S")
    # Setting up holidays and next holidats
    if strftime("%m") == "09":
        days_until = str(29 - int(strftime("%d")))
        Holiday = ("your birthday!")
        Screencolor = "#FF75DE"
        Next_holiday = "Sydney's birthday!"
        days_until_next = (str (30 - int(strftime("%d")) + 5))
        next_color = "#75E6FF"
    if strftime("%m") == "10": 
        if (int(strftime("%d")))<5:
            days_until = str(5 - int(strftime("%d")))
            Holiday = ("Sydney's birthday!")
            Screencolor = "#75E6FF"
            Next_holiday = "Sophie's birthday!"
            days_until_next = (str(27 - int(strftime("%d"))))
            next_color = "#C375FF"
        elif (int(strftime("%d")))<=27:
            days_until = str(27 - int(strftime("%d")))
            Holiday = ("Sophie's birthday!")
            Screencolor = "#C375FF"
            Next_holiday = "Halloween!"
            days_until_next = str(31 - int(strftime("%d")))
            next_color = "#FFB375"
        elif (int(strftime("%d")))<=31:
            days_until = str(31 - int(strftime("%d")))
            Holiday = ("Halloween!")
            Screencolor = "#FFB375"
            Next_holiday = "Thanksgiving!"
            days_until_next = str(31 - int(strftime("%d")) + 25)
            next_color = "#BF3F00"
    if strftime("%m") == "11": 
        if (int(strftime("%d")))<25:
            days_until = str(25 - int(strftime("%d")))
            Holiday = ("Thanksgiving!")
            Screencolor = "#BF3F00"
            Next_holiday = "Christmas!"
            days_until_next = str(int(days_until) + 25)
            next_color = "#FF0000"
    if strftime("%m") == "12":
        if (int(strftime("%d")))<25:
            days_until = str(25 - int(strftime("%d")))
            Holiday = ("Christmas!")
            Screencolor = "#FF0000"
            Next_holiday = "New Year's Eve!"
            days_until_next = str(int(days_until) + 6)
            next_color = "#C2C2C2"
        else:
            days_until = str(31 - int(strftime("%d")))
            Holiday = ("New Years Eve!")
            Screencolor = "#C2C2C2"
    # Setting up buttons
   # if not buttonA.value and not buttonB.value:
       # backlight.value = False  # turn off backlight
    # no buttons pressed: 
    #else:
    backlight.value = True  # turn on backlight
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)
    #draw.rectangle((0, 0, width, height), outline=0, fill=0)
    if buttonA.value and buttonB.value: 
        if days_until == "0":
            if Holiday == "Holiday":
                draw.text((x, y), Time, font = font, fill = Screencolor)
                y += font.getsize(Time)[1]
                draw.text((x, y), "There are no more holidays this month", font = font, fill = Screencolor)
                display.image(image, rotation)
            else:
                draw.text((x, y), Time, font = font, fill = Screencolor)
                y += font.getsize(Time)[1]
                draw.text((x, y), "Today is " + Holiday, font = font, fill = Screencolor) 
                display.image(image, rotation)     
        else:
            draw.text((x, y), Time, font = font, fill = Screencolor)
            y += font.getsize(Time)[1]
            draw.text((x, y), "There are "+ days_until, font = font, fill = Screencolor)
            y += font.getsize(Time)[1]
            draw.text((x, y), "days until " + Holiday, font = font, fill = Screencolor)
            display.image(image, rotation)
    # Button A Pressed
    if buttonB.value and not buttonA.value:  # just button A pressed
        image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        #draw.text((x, y), "Button A Pressed", font=font, fill="#FFFFFF")
        draw.text((x, y), Time, font = font, fill = Screencolor)
        y += font.getsize(Time)[1]
        draw.text((x, y), "There are "+ days_until_next, font = font, fill = Screencolor)
        y += font.getsize(Time)[1]
        draw.text((x, y), "days until " + Next_holiday, font = font, fill = Screencolor)
        display.image(image, rotation)
        display.image(image, rotation)
    # Button B Pressed
    elif buttonA.value and not buttonB.value:  # just button B pressed
        image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, y), "Button B Pressed", font=font, fill="#FFFFFF") 
        display.image(image, rotation)
    #Both Pressed
    elif not buttonA.value and not buttonB.value:  # both pressed
        image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, y), 'Both Pressed', font=font, fill="#FFFFFF")
        display.image(image, rotation)
    time.sleep(0.5)

