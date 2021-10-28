# Ph-UI!!!

For lab this week, we focus on both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 


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
### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

#### (Optional) Distance Sensor

We also used this sensor. Please keep reading for further details on implementation and a demo.

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

Display: One difficult part to figure out was where to put the display on the mug to make it easy to read. Our first sketch has the display on the side which we thought was a pretty design but may be difficult for the user to read since the mug must be set on its bottom (rather than its side) when the mug is used. We also figured it may be hard to read the device if the display is on the side incase people are holding the mug and covering the display which led us to the idea of having a projected display. We also played with the idea of using a separate device with a display as well.

Color sensor: Our sketches also brought up the question of how the color sensor could see the color of the coffee without actually being in contact with the cofee which could be dangerous. We did not want the sensor right in the device so we found out it was probably best to use a clear glass mug similar to a mason jar to place the color sensor on the outside while still being able to sense through the mug the color of the coffee.

Weight: As we were drawing the sketches, there were many sensors that we originally wanted in the device which may greatly increase the weight of the mug. The tricky part is balancing the amount of hardware on the device to increase functionality and interaction with the actual weight and usability of the device itself.

The mug may need to need to be larger, taller, or a little heavier to implement all the desired features.

***Pick one of these display designs to integrate into your prototype.***

We decided that design 5 would most likely incorporate the most features while maintaining usability.

***Explain the rationale for the design.*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

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

##### Feedback we got from Part 1:
"I thought it was fun that all your part c sketches were related to coffee, and I think you did a great job of discussing the considerations for your physical prototype and potential ideas to address them. For the color sensor, it would be good to make sure the sensor can distinguish between background color (since the mug is translucent) vs coffee. For the distance sensor, a slight adjustment or addition to the idea could be to have the device alert you that the coffee is done brewing if you are getting too far away."

- Sara Wang, Oct 19 at 2:54pm

"Cool ideas, I also thought it was funny how all of your initial ideas were related to coffee. My main concern about the implementation of the idea is the close proximity of the sensors to liquid, which it looks like you gave some thought to in your "raised questions" section"

- Alexander Bradley Kluver, Oct 20 at 6:24pm

" I think this is a really interesting idea. It can help people control their coffee and remind people to pick coffee up, which is useful and convinient. My first concern is that if putting the color detection sensor under the bottom, whether it will only detect black instead of the real color of the coffee. Maybe it can be on the side of the bottle. And my second concern is that the distance sensor can only detect people in front of it, namely, if the user is on the side of the bottle, even if she is close to the bottle, the sensor still can not detect her. Overall, it's a great idea!" 

- Tianyun Zou, Oct 21 at 12:18am

" It's very creative, but a lot going on! Might want to focus on on just making one or two features. But it's a great idea!" 

- Brandon Kyle Newman, Oct 21 at 10:05am

## ** Based on the feedback we received, we decided to focus on two sensors, try to place them around the cup and not too close to the liquid. In future implementations, we would try double insulating the glass and putting the sensors in the middle layer, protected from the heat of the liquid. Additionally, we would implement smaller distance sensors all around the cup so it could detect the user from every angle. Finally, the color sensor would no longer be on the bottom, it would be in that inner insulated layer that does not touch the heated portion of the mug and it would reside on the front side of the mug behind the screen. **


### Part E (Optional) - Servo Control with Joystick (N/A)

### Part F
### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:

See images here during the build process of Part 2:
![IMG_7394](https://user-images.githubusercontent.com/27168450/138793211-733f60d3-659b-404c-91a8-6da4a5e9254d.JPG)
![image](https://user-images.githubusercontent.com/27168450/138793231-eddf8884-9551-479a-9f8c-f1555e96392a.png)
![image](https://user-images.githubusercontent.com/27168450/138793253-e41a6e77-86a3-4a16-be8c-45e5bfc5204b.png)
![image](https://user-images.githubusercontent.com/27168450/138793264-d7335e47-fb75-4d82-b961-ac8d0cbf6101.png)
![image](https://user-images.githubusercontent.com/27168450/138794877-d1d41711-eb41-4ae5-82b9-91976b92cd3f.png)






##### Prototype Final Summary
#### * "Looks like": shows how the device should look, feel, sit, weigh, etc.
To show what the device will look like, we created a paper prototype, a paper/pi prototype, and a physical prototype. Because we wanted our display to have color, we were unable to use the mini scren for a functional prototype and needed to use the large screen that attached directly onto the pi which was difficult to integrate into a 3d physical prototype. To illutrate the shape of the device, we found it was better to create a fully paper prototype to be able to mimic what the mug would look like with the sensors seamlessly integrated. This prototype was unable to capture the weight of the prototype but gave a better visual as to the functionalities and overall look of the device. Because we wanted to use color, we used the larger screen to create a prototype with paper and the pi. This allowed us to show how the device dislay would look built into the mug. The bulkiness of the pi made it difficult to create a mug shape around it so we decided to make this prototype 2d. Our last physical prototype made with the glass mason jar and the sensors attached illustrates the weight and feel of the prototype. We wanted to be able to mimic the weight of a normal sized mug with the attached sensors. This prototype did not look exactly like our intended device but gave the feel of the device to users.

#### * "Works like": shows what the device can do
#### * "Acts like": shows how a person would interact with the device
To show how the device works and how users should interact with the device, we filmed these videos that showcased the 3 features of the mug. The final video shows how the coffee mug reminds users to come back if they venture too far away from a hot cup of cofee. It also shows how users can input the desired color of their coffee and how the device will prompt users to continue adding milk to their coffee until it reaches the desired color.

#### See the video uploaded on Google Drive for a FULL DEMO (Put sound on to hear VOICE)

https://drive.google.com/file/d/17R9gVht4VkaXWXcz3chjbj25huugX8Mb/view?usp=sharing
![image](https://user-images.githubusercontent.com/27168450/138792991-085b1db9-974c-4932-b5cd-683043f5ec62.png)


