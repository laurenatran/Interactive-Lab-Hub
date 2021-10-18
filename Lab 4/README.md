# Ph-UI!!!

For lab this week, we focus on both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 

## Part 1 Lab Preparation

### Get the latest content:
As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the personal access token for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab4 content"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

### Start brasinstorming ideas by reading: 
* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 
* [Dyson Vacuum Cardboard Prototypes](http://media.dyson.com/downloads/JDF/JDF_Prim_poster05.pdf)
<p align="center"><img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > </p>

### Gathering materials for this lab:

* Cardboard (start collecting those shipping boxes!)
* Found objects and materials--like bananas and twigs.
* Cutting board
* Cutting tools
* Markers

(We do offer shared cutting board, cutting tools, and markers on the class cart during the lab, so do not worry if you don't have them!)

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Group members can turn in one repository, but make sure your Hub readme.md links to the shared repository.
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.


## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Record the interaction](#part-f)

## The Report (Part 1: A-D, Part 2: E-F)


###  Lab Partners: Magdalena Horowitz (myh26) and Lauren Tran (lat89)
## Lab ideas Brainstorming Pad: 
- alarm clock that turns off when it senses you've turned the light on
- coffee machine that tells whne your coffee has the right amount of milk based on the color
- proximity sensor for finding your phone
- snake game with the joystick

## Coffee Idea brainstorm: 
- Light/Proximity/Gesture sensor: tell what color the coffee is
- sensor could be on the milk carton
- could be on the coffee maker
- could be an independent device like a phone camera
- could be on a mug Capacitive Sensing, a.k.a. Human-Twizzler Interaction: gives user a warning that the cup is hot if they touch it too soon Distance Sensor:
- makes sure the user doesn't forget their cofee when they leave


### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 

We want to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we are able to provide. At boot, it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes, it considers it a user touch. You can attach any conductive material. In your kit, you have copper tape that will work well, but don't limit yourself! In the example below, we use Twizzlers--you should pick your own objects.


<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
</p>

Plug in the capacitive sensor board with the QWIIC connector. Connect your Twizzlers with either the copper tape or the alligator clips (the clips work better). In this lab, we will continue to use the `circuitpython` virtual environment we created before. Activate `circuitpython` and `cd` to your Lab 4 folder to install the requirements by:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" width=400>
These Twizzlers are connected to pads 6 and 10. When you run the code and touch a Twizzler, the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Twizzler 10 touched!
Twizzler 6 touched!
```

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" width=200>

Connect it to your pi with Qwiic connector and try running the 3 example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python light_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Rotary Encoder

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separated breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">
<img src="https://cdn-shop.adafruit.com/970x728/4991-01.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up? 

#### Joystick

A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### (Optional) Distance Sensor

Note: We did not distribute this sensor to you, so if you are interested in playing with it, please come pick it up from the TA!

Earlier we have asked you to play with the proximity sensor, which is able to sense object within a short distance. Here, we offer [Qwiic Multi Distance Sensor](https://www.sparkfun.com/products/17072), which has a field of view of about 25° and is able to detect objects up to 3 meters away! 

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/0/3/4/17072-Qwiic_Multi_Distance_Sensor_-_VL53L3CX-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python distance_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_VL53L1X_Py) to learn more about the sensor and see other examples!

### Part C
### Physical considerations for sensing

Usually, sensors need to positioned in specific locations or orientations to make them useful for their application. Now that you've tried a bunch of the sensors, pick one that you would like to use, and an application where you use the output of that sensor for an interaction. For example, you can use a distance sensor to measure someone's height if you position it overhead and get them to stand under it.

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***

# 1.
![image](https://user-images.githubusercontent.com/27168450/137630850-3f1125f3-07a5-4e91-9b8f-9790497d4c8e.png)

# 2.
![image](https://user-images.githubusercontent.com/27168450/137630860-d5e2fb74-97f8-43a5-a350-81cdb9bd1a1b.png)

# 3.
![image](https://user-images.githubusercontent.com/27168450/137630875-59f083b3-3881-4492-a4e3-40f56571ed37.png)

# 4.
![image](https://user-images.githubusercontent.com/27168450/137630879-f0af9fa1-f612-4f3f-ace4-36c6bea8260d.png)

# 5.
![image](https://user-images.githubusercontent.com/27168450/137630889-51902afe-977e-46f5-9e68-3632dd72f480.png)


**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

Durability of the sensors: one problem is that the sensors need to be very near to hot coffee which could cause problems if the sensor is not water or heat proof. Our first design has the color sensor right on the inside side of the mug which could be very accident prone. To possible account for this, we created another design with the color sensor on the bottom of the mug under a glass or otherwise clear screen that may do a better job of protecting the sensor from hot coffee. This also would prevent the sensor from getting in the way of someone drinking the coffee. It would be difficult to physically protptype to test the durability of the sensors because we do not want to break the sensor. However, we could use a real mug and something disposable such as a piece of paper towel that acts as a sensor and see if the fake sensor gets wet in our prototype.

Weight: Although mugs are typically heavy, adding screens and sensors coudl make the mug more heavy. Our first sketch had the color sensor and display on the mug but our next designs have the display as a separate device that could ideally connect wirelessly to the mug to display the coffee's readiness separate from the mug itself. If the mug is too bulky with all of the sensors, it could take away from the appeal of the mug. To prototype this, we could try using different real mugs and adding the sensors and testing of users feel comfortable lifting the mug. We could try using lightweight plastic mugs and adding the sensors and seeing if the weight is comprable to the weight of a heavier ceramic mug.

Ability to drink from the mug: The sensors could possible hinder people's ability to drink from the mug if they are not placed correctly. If the screen is too close to the handle or the sensor is too close to the lip of the mug, it would be annoying to drink or hold the mug around the sensor so we will need to take into account the most natural and comfortable way for people to hold mugs and build our sensors aroaund the natural grasp. To test this, we could create a cardboard mug or use a real mug and see how people hold the mug. We could then add the sensors to the mug and see if they change the way people grasp the mug or otherwise get in the way of the person's natural handhold.

Ability to wash the mug: The ability to use a dishwasher on a mug is a salient consideration when people buy mugs so it is improtant that the sensors are able to be washed in a dish washer without the sensors prevent spaces from getting clean. To test this, we could create fake sensors and add rthem to the mug and see if the mug is still able to be cleaned with the fake sensors. Prototopying this problem is difficult similar to the first problem because we don't want to actually put the sensors through the dishwasher but by creating fake sensors out of dish washer safe materials, we could mimic the shape of the mug with sensors and see how well the prototype holds up in the dishwasher.

**\*\*\*Pick one of these designs to prototype.\*\*\***


Some of the sensing ideas seemed cool at first but raised a couple of questions. For the gesture sensing option, we'd need to find some way to connect the coffee mug device to the actual coffee maker itself. There would be quite a lot of connectivity issues that might be solved through bluetooth, wires (not ideal), or NFC communication. In order to add milk, sugar, etc based on a gesture, the cups sensors would have to send the signal back to the coffee machine, or we'd also have to implement sensors onto the coffee making machine itself.

Using the distance sensor to greet a user in the morning might end up being intrusive and annoying. While it is good to remind a user to make coffee in the morning, if someone wants to wake up discreetly or wants to practice yoga or meditate in their living room/kitchen area, they would not want a coffee device speaking to them every time they moved close to it. 

Finally, the sensors themselves are relatively big so finding a way to incorporate them into the coffee mug while hiding them but also allowing them to function is a bit tricky. We thought of encasing the light sensor in a internal glass inner layer, so it is water resistant and is protected from all liquids. The distance sensor could be placed on the handle, but it too must be protected from damage while still allowing access to its surroundings to perform its sensing capabilities.

We decided that options 4 and 5 would work best with our coffee mug and would provide the most interactive and useful user experience. By determining the RGB content of the coffee color, the device would be unique and be able to add value by telling the user if the coffee color is related or matches the user's preference for coffee. This way, the user would always know when to add more milk to get the perfect cup of coffee every time. 

Option 5 would also be extremely useful, because sometimes when you pour a cup of coffee, you step away for a minute to do other tasks as it's brewing. With the distance sensor, the device could warn you that you are getting too far away and remind you to pick up and drink your cup of coffee. No more cups of coffee wasted!

### Part D
### Physical considerations for displaying information and housing parts


Here is an Pi with a paper faceplate on it to turn it into a display interface:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but the mounting of the display constrains the display location and orientation a lot. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

Your kit includes these [SparkFun Qwiic OLED screens](https://www.sparkfun.com/products/17153). These use less power than the MiniTFTs you have mounted on the GPIO pins of the Pi, but, more importantly, they can be more flexibily be mounted elsewhere on your physical interface. The way you program this display is almost identical to the way you program a  Pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>


It holds a Pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>

Think about how you want to present the information about what your sensor is sensing! Design a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***

# 1. 
![image](https://user-images.githubusercontent.com/27168450/137631800-c2f6dffa-d4ad-4505-ac0f-362df7507680.png)

# 2.
![image](https://user-images.githubusercontent.com/27168450/137631806-18100f79-b903-4af5-a14b-428c0a987bd3.png)

# 3.
![image](https://user-images.githubusercontent.com/27168450/137631810-500a0b15-2635-4bda-8948-f021d3c28fad.png)

# 4.
![image](https://user-images.githubusercontent.com/27168450/137631814-601e30b2-13cf-44b6-b1b3-11f111661c09.png)


# 5.
![image](https://user-images.githubusercontent.com/27168450/137631821-b5bbd26a-c574-42b7-8cb6-90f72e2cb432.png)


**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

The tricky part is balancing the amount of hardware on the device to increase functionality and interaction with the actual weight and usability of the device itself. The mug may need to need to be larger, taller, or a little heavier to implement all the desired features.

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

We decided that design 5 would most likely incorporate the most features while maintaining usability. 

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

Build a cardbord prototype of your design.

** See photos: ** 
![image](https://user-images.githubusercontent.com/27168450/137638692-0421af01-a4d9-4474-b43b-33b0ca453ee1.png)
![image](https://user-images.githubusercontent.com/27168450/137638698-882a189a-5685-42e1-99db-3bef7b55c707.png)

** See photo ** 


**\*\*\*Document your rough prototype.\*\*\***

See the pictures below for the rough prototype wizarded with current materials. 
The RGB sensor at the bottom of the mug will be encased in class, sealed off from liquid damage, but will still be able to view the color of the liquid through a glass material.

The distance sensor will remain on the side of the mug and the display screen will sit on the side. 




# ** ACTUAL PROTOTYPE: See the progression of coffee shades that the device will detect: ** 
![image](https://user-images.githubusercontent.com/27168450/137631853-c03db935-238d-4f6c-b4f4-1c70476e4db9.png)

![image](https://user-images.githubusercontent.com/27168450/137631861-66fcc24d-625e-463e-aeb1-259dbfa44224.png)

![image](https://user-images.githubusercontent.com/27168450/137631871-532ac86a-ea51-4d5f-a117-9c0d33390626.png)
![image](https://user-images.githubusercontent.com/27168450/137631877-00518a11-795f-4510-aba4-fd2ceb408a67.png)
![image](https://user-images.githubusercontent.com/27168450/137631888-ab1169ca-eaa9-4eac-b5c9-96a62a364cd1.png)

LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part E (Optional)
### Servo Control with Joystick

In the class kit, you should be able to find the [Qwiic Servo Controller](https://www.sparkfun.com/products/16773) and [Micro Servo Motor SG51](https://www.adafruit.com/product/2201). The Qwiic Servo Controller will need external power supply to drive, which we will be distributing the battery packs in the class. Connect the servo controller to the miniPiTFT through qwiic connector and connect the external battery to the 2-Pin JST port (ower port) on the servo controller. Connect your servo to channel 2 on the controller, make sure the brown is connected to GND and orange is connected to PWM.

<img src="https://scontent-lga3-1.xx.fbcdn.net/v/t1.15752-9/245605956_303690921194525_3309212261588023460_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_ohc=FvFLlClTKuUAX9nJ3LR&_nc_ht=scontent-lga3-1.xx&oh=b7ec1abc8d458b6c1b7a00a6f11398ac&oe=618D7D96" width="400"/>

In this exercise, we will be using the nice [ServoKit library](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) developed by Adafruit! We will continue to use the `circuitpython` virtual environment we created. Activate the virtual environment and make sure to install the latest required libraries by running:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

A servo motor is a rotary actuator or linear actuator that allows for precise control of angular or linear position. The position of a servo motor is set by the width of an electrical pulse, that is, we can use PWM (pulse-width modulation) to set and control the servo motor position. You can read [this](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn a bit more about how exactly a servo motor works.

Now that you have a basic idea of what a servo motor is, look into the script `qwiic_servo_example.py` we provide. In line 14, you should see that we have set up the min_pulse and max_pulse corresponding to the servo turning 0 - 180 degree. Try running the servo example code now and see what happens:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python servo_test.py
```

It is also possible to control the servo using the sensors mentioned in as in part A and part B, and/or from some of the buttons or parts included in your kit, the simplest way might be to chain Qwiic buttons to the other end of the Qwiic OLED. Like this:

<p align="center"> <img src="chaining.png"  width="200" ></p>

You can then call whichever control you like rather than setting a fixed value for the servo. For more information on controlling Qwiic devices, Sparkfun has several python examples, such as [this](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples).

We encourage you to try using these controls, **while** paying particular attention to how the interaction changes depending on the position of the controls. For example, if you have your servo rotating a screen (or a piece of cardboard) from one position to another, what changes about the interaction if the control is on the same side of the screen, or the opposite side of the screen? Trying and retrying different configurations generally helps reveal what a design choice changes about the interaction -- _make sure to document what you tried_!

### Part F
### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do
* "Acts like": shows how a person would interact with the device

