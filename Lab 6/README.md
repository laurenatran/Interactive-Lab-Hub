# Little Interactions Everywhere

## Prep

1. Pull the new changes from the class interactive-lab-hub. (You should be familiar with this already!)
2. Install [MQTT Explorer](http://mqtt-explorer.com/) on your laptop.
3. Readings before class:
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Overview

The point of this lab is to introduce you to distributed interaction. We have included some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects if wanted. However, we want to emphasize that the grading will focus on your ability to develop interesting uses for messaging across distributed devices. Here are the four sections of the lab activity:

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things) devices. 

#### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`. Imagine that the Broker is the messaging center!
* **Client** - A device that subscribes or publishes information to/on the network.
* **Topic** - The location data gets published to. These are *hierarchical with subtopics*. For example, If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. With this setup, the info/updates of the sidelamp's `light_status` and `voltage` will be store in the subtopics. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on the topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe. Following the previouse example of home IoT smart bulbs, subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage.
* **Publish** - This is a way of sending messages to a topic. Again, with the previouse example, you can set up your IoT smart bulbs to publish info/updates to the topic or subtopic. Also, note that you can publish to topics you do not subscribe to. 


**Important note:** With the broker we set up for the class, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`. Also, setting up a broker is not much work, but for the purposes of this class, you should all use the broker we have set up for you!


#### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.


![input settings](imgs/mqtt_explorer.png?raw=true)


Once connected, you should be able to see all the messages under the IDD topic. , go to the **Publish** tab and try publish something! From the interface you can send and plot messages as well. Remember, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`.

![publish settings](imgs/mqtt_explorer_2.png?raw=true)


### Part B
### Send and Receive on your Pi

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python. Let's spend a few minutes running these and seeing how messages are transferred and shown up. Before working on your Pi, keep the connection of `farlab.infosci.cornell.edu/8883` with MQTT Explorer running on your laptop.

**Running Examples on Pi**

* Install the packages from `requirements.txt` under a virtual environment, we will continue to use the `circuitpython` environment we setup earlier this semester:
  ```
  pi@ixe00:~ $ source circuitpython/bin/activate
  (circuitpython) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 6
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ pip install -r requirements.txt
  ```
* Run `sender.py`, fill in a topic name (should start with `IDD/`), then start sending messages. You should be able to see them on MQTT Explorer.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python sender.py
  pi@ReiIDDPi:~/Interactive-Lab-Hub/Lab 6 $ python sender.py
  >> topic: IDD/ReiTesting
  now writing to topic IDD/ReiTesting
  type new-topic to swich topics
  >> message: testtesttest
  ...
  ```
* Run `reader.py`, and you should see any messages being published to `IDD/` subtopics.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python reader.py
  ...
  ```

**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***
1. Concert Message Broadcasting: Creating a communication device used specifically for concerts where people can create topics for their section, for the bathroom lines, for the food and merch lines, for emergencies, etc to communicate with others at the concert venue. This would allow users to not be on their phones if they do want to live in the moment and want to avoid being tempted to check on other things in their phone. There would likely have to be a location aspect so that people not actually at the concert venue could not join the communication channels and mess with those actually at the concert


2. Smart Refrigerator IoT Broadcasting Items: When items that are low in your refrigerator are ON SALE, a message is broadcasted to all users who need this item and the closest store to them that has this item on sale. Users could also opt in to “all sale” notifications based on their location so whenever any item is on sale near them and they have bought it previously, they are notified


3. Alert system for retailers: Usually agents have to show the house to users, but to do this either they need a key or the house owner. We can create a system such that door lock is controlled by rpi and when someone requests access to the house, home owners can approve it over sms


4. Smart Mirror: Users get dressed in the morning and look at the mirror one final time before leaving the house. The mirror uses AI to recognize their outfit and cross check it with the weather outside. It then broadcasts the message to all users who aren’t wearing appropriate clothing that they will be too hot or too cold. It will then broadcast the weather to all users all at once


5. Patient SOS system: This product is designed for bed ridden patients who need support from nurses or need constant monitoring.
It will have both automatic mode and manual mode. In manual mode, when the patient needs help, they can press a button on the system, and the hospital's helpdesk or relevant authority would be notified about the same.
In automatic mode, we will constantly monitor the patient using a camera and in case some unusual motion is detected, it will be notified to the doctors.


### Part C
### Streaming a Sensor

We have included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Fall2021/Lab%204) that streams the [capacitor sensor](https://learn.adafruit.com/adafruit-mpr121-gator) inputs over MQTT. We will also be running this example under `circuitpython` virtual environment.

Plug in the capacitive sensor board with the Qwiic connector. Use the alligator clips to connect a Twizzler (or any other things you used back in Lab 4) and run the example script:

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
<img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150"/>
<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" height="150">
</p>

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python distributed_twizzlers_sender.py
 ...
 ```

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***
![IMG_6767 2](https://user-images.githubusercontent.com/89945550/141885902-0283f590-c959-4fa9-b5b7-5ad6f869dc2d.JPG)
<img width="259" alt="Screen Shot 2021-11-15 at 12 38 49 PM" src="https://user-images.githubusercontent.com/89945550/141885962-3f7762d2-5fe0-47fe-81fd-4da431cd064f.png">


**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***
![IMG_6768](https://user-images.githubusercontent.com/89945550/141886046-28b44a51-6366-4525-a9b7-791a8c36f668.JPG)

<img width="275" alt="Screen Shot 2021-11-15 at 12 48 24 PM" src="https://user-images.githubusercontent.com/89945550/141886729-99f1857a-a356-491e-9627-728e81d11fbe.png">



### Part D
### The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB, we too can find unity in our heart, minds and souls. With the help of machines, we can overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [MiniPiTFT Display](https://www.adafruit.com/product/4393). You are almost there!

<p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
  <img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="150">
</p>


The second step to achieving our great enlightenment is to run `color.py`. We have talked about this sensor back in Lab 2 and Lab 4, this script is similar to what you have done before! Remember to ativate the `circuitpython` virtual environment you have been using during this semester before running the script:

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python color.py
 ...
 ```

By running the script, wou will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one.

(A message from the previous TA, Ilan: I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also, I haven't load-tested it so things might just immediately break when everyone pushes the button at once.)

You may ask "but what if I missed class?" Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can go to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs. Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 

**\*\*\*Can you set up the script that can read the color anyone else publish and display it on your screen?\*\*\***


### Part E
### Make it your own

Find at least one class (more are okay) partner, and design a distributed application together based on the exercise we asked you to do in this lab.

**\*\*\*1. Explain your design\*\*\*** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.

On November 5th, Travis Scott hosted his Astroworld Festival, a music festival in Houston where 9 people died and there was outrage over the lack of communication between concert goers, Travis, his team and the venue management. We decided to create a communication wristband meant for users at concerts to improve communication at widespread events. 
The wristband will have a screen and one button for controls. The screen will show multiple communication channels such as “bathroom lines” and “emergencies” and channels for specific seating sections. Users will be able to choose which channel they broadcast to and which channel they want to see messages from. Any emergency messages will be broadcast to everyone. 
Because this device is meant to communicate in large networks at concert venues, users will not be able to input custom messages and will use the button to choose options. We considered using a voice to text feature but since concerts are typically very loud, we vetoed this idea. Instead, there will be a fixed amount of messages a user can send to avoid having to put a keyboard or other large input device. For example, in the bathroom channel, users could choose between message options such as “how many people are in line?” “0-10 people” and “10-25 people.” In the section channel, users can send different emojis for fun. 
 


**\*\*\*2. Diagram the architecture of the system.\*\*\*** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

Below are different ideas of possible features and functions of this device, with the final 2 photos showing the final paper prototype design. Users press the button to input their message and the screen is used to show output where the user will be able to see the message they sent as well as incoming messages. The user is at a concert where the wristband will be handed out to all concert goes. Alternatively, more advanced forms of this design could be sold for people to bring to concerts but the idea for this device is that is is simple enough that it is not too expensive and will be able to be given to ticket holders at events similar to how Taylor Swift gives out light up wristbands at her concerts. 

<img width="617" alt="Screen Shot 2021-11-15 at 9 42 21 PM" src="https://user-images.githubusercontent.com/89945550/141886158-83c6872e-55e5-4fc1-b89c-0e630fce63f8.png"><img width="504" alt="Screen Shot 2021-11-15 at 9 42 37 PM" src="https://user-images.githubusercontent.com/89945550/141886190-74d394b1-04d3-459b-9530-6e13b5d3eeaa.png">
<img width="478" alt="Screen Shot 2021-11-15 at 9 42 50 PM" src="https://user-images.githubusercontent.com/89945550/141886208-4dabf3a3-7611-4050-901c-72e950db8181.png">
![Quiic Button](https://user-images.githubusercontent.com/89945550/141886296-84e10984-028e-49d6-92aa-f8f83247dd1d.png)

![Quiic Button-2](https://user-images.githubusercontent.com/89945550/141886304-13ad17c1-b65b-4086-ac93-ab6763dd40a9.png)


**\*\*\*3. Build a working prototype of the system.\*\*\*** Do think about the user interface: if someone encountered these bananas somewhere in the wild, would they know how to interact with them? Should they know what to expect?

The build of the wristband is intuitive and straightforward. In the first iteration (for Lab 6), our prototype has one button (we implemented the QWIC green button). Clicking the button on this wristband will change the channel, and long pressing the button will allow the user to select a message, change the color, and interact with the wristband. As we know with research, products such as the well known and loved Apple Watch only have 2 buttons and are still highly functional. As this wristband’s main purpose is functionality, connectivity, and simplicity, through our first iteration we believe that one button will allow all the features to be accessed easily and intuitively. We also implemented Mini OLED for the display on the wristband and give details to the users about different broadcasted messages through certain “channels”. 

The different channels are programmed to broadcast messages such as food availability and line length, bathroom line length, section announcements and color coordinating selection, and finally an emergency channel. 

During orientation for the concert, users will be given a brief instructional demo so they will know what to expect. 
In the case of an emergency, the user would not have to select the emergency or notification channel, it would be automatically broadcast to all users in the area of danger/vicinity of the emergency. 


For future iterations for the final project we will be adding more complex features including but not limited to: LED lights that light up and indicate the number of people per line: for every 5 people, an additional LED light would turn on. We are also adding the ability to send emojis, other broadcast ways, and thinking that the wristband will also emit a vibration and/or other mode of notifying the user other than light and display. 



**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

Video: https://drive.google.com/file/d/1SVgkmsH7HKQVv_Le5bUmqw4kjKrMLpJg/view?usp=sharing

<!--**\*\*\*5. BONUS (Wendy didn't approve this so you should probably ignore it)\*\*\*** get the whole class to run your code and make your distributed system BIGGER.-->

