# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.

## Prep

1.  Pull the new Github Repo.
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2021/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:

1. Raspberry Pi
1. Webcam 
1. Microphone (if you want to have speech or sound input for your design)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

Following is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

Contours Detection:

<img width="300" alt="Screen Shot 2021-11-02 at 5 56 57 PM" src="https://user-images.githubusercontent.com/89945550/139960043-4b94eb96-1a95-468d-b7a9-975eb9bdb020.png">

The first thing that came to mind with the countours detection example was being able to use this for makeup purposes, especially given the recent trends of enhacing the contours of the face. By using this contour detection algorithm, a makeup artist could use the image of their client's face to determine the best makeup application to enhance the client's face depending on their preferences. Knowing where the contours of a person's face are could help makeup artists deepen and emphasize those contours or minimize them based on the requests of their client. 

Face Detection:

<img width="300" alt="Screen Shot 2021-11-02 at 6 01 52 PM" src="https://user-images.githubusercontent.com/89945550/139960073-51b64558-8a8f-4c27-8239-717e6e9efd5a.png">

<img width="300" alt="Screen Shot 2021-11-02 at 6 02 16 PM" src="https://user-images.githubusercontent.com/89945550/139960081-9e7b8a9e-1cf7-4b1a-a6da-a22a4cbe8a69.png">

A face detection algorithm could be used to count the number of people going into a store so that stores can keep track for covid safety and general crowd purposes. Many stores have a person at the door counting how many people go in and cutting people off if the store limit is reached so that stores are not crowded. Using this algorithm could negate the use of a human counter at the door. 

Flow-Detection 

<img width="300" alt="Screen Shot 2021-11-02 at 6 07 49 PM" src="https://user-images.githubusercontent.com/89945550/139960119-436bf8da-8eec-40ec-8ffd-c188cd09d36b.png">

The optical flow detection algorithm could be used on a large scale to determine walking paths in places where paths do not already exist For example, at my undergrad school people would constantly cut across a grass meadow because it provided a shortcut from the road to a building. The flow detection could illuminate this irregegular path that students favored over the sidewalks which could encourage the university to put a paved path across the grass rather than continue to have the grass trampled and ruined in the meadoww. 

Object Detection

<img width="300" alt="Screen Shot 2021-11-02 at 6 09 59 PM" src="https://user-images.githubusercontent.com/89945550/139960153-bcd515c6-86ac-41da-847f-81a40533df46.png">

This algorithm reminded me of whe my parents used to yell at me and my siblings for having toys all over our playroom. The object detection algorithm could be used as an incentive for people to clean their rooms, especially for kids to know that their room is cleaned when the algorithm does not detect any objects on the floor. 

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi4 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53.

<img width="300" alt="Screen Shot 2021-11-02 at 6 20 10 PM" src="https://user-images.githubusercontent.com/89945550/139960293-cb4e52dd-8ed2-4feb-bb96-d4f201fd287b.png">

<img width="300" alt="Screen Shot 2021-11-02 at 6 20 34 PM" src="https://user-images.githubusercontent.com/89945550/139960304-f85d2c90-10a6-4805-abd0-205bea61cd58.png">

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)

As a child, I hated practicing piano and especially when my mom would tell me that I was using bad form when practicing by having my back slouch or my wrists limp. A hand and body tracking program could determine when students are having bad form and give suggestions to the user to improve their form without having the annoyance of a teacher or parents scolding them. 


#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***

I trained a model to detec when I was holding a coffee in my hand. This method was interesting because it relied on user inputs to determine how the model was run, leaving it more open ended than the OpenCV or Media Pipe options which were more fixed in scope. Another interesting feature was that the user could input images rather than rely solely on the webcam which was limited. The webcam could only capture so much and was limited by the user's surroundings but imputting images allows for more diversity of image classifications. 

<img width="292" alt="Screen Shot 2021-10-28 at 10 27 32 AM" src="https://user-images.githubusercontent.com/89945550/139960692-554eccd3-d561-4658-bd88-5ad4f2a216fe.png">
<img width="312" alt="Screen Shot 2021-10-28 at 10 28 09 AM" src="https://user-images.githubusercontent.com/89945550/139960708-e6b8e903-05dc-4405-bfce-f6866a5610a7.png">
<img width="534" alt="Screen Shot 2021-10-28 at 10 44 47 AM" src="https://user-images.githubusercontent.com/89945550/139960764-83606d7d-ddf7-4a53-8398-025996c4247f.png">
<img width="484" alt="Screen Shot 2021-10-28 at 10 47 19 AM" src="https://user-images.githubusercontent.com/89945550/139960803-f7befb06-d427-45ab-a826-18d64b64e2eb.png">

*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


#### Filtering, FFTs, and Time Series data. (optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

One event I am very interested in is the Met Gala and my first idea was to build a teachable machine model that would identify different designers. I built a model with photos from the 2021, 2019, and 2018 Met Gala focusing on Louis Vuitton, Gucci, Valentino, and Versace. However, when I trained the model and tested on images from the 2017 Met Gala, the resulting predictions were not very acccurate, likely because the fashion at the Met Gala is so extreme and tailored to specific themes that the looks do not neccessarily correlate or relate directly to any designer's specific aesthetics and it would be difficult for the model to be very precise with very extreme fashion. As a result, I decided to simplify my idea to looking at general dress codes which led me to my next idea.

A few week ago, a girl went viral on TikTok because she was invited to a Black Tie wedding and thought that meant she had to wear a black dress; she posted a video of herself trying on multiple short black dresses for the event and TikTok users mocked for for completely missing the dress code and not understanding what black tie meant. This inspired my device which will classify users' outfits based on different dress codes such as semi formal, black tie, business casual, business formal, etc. A user will be able to step in front of their web cam and the algorithm will determine which dress code standard they are following. For example, if a user has an interview coming up that asks for business formal attire, it may be difficult for the user to understand the diffrence between business formal, formal, and business casual outfits. This device will help remedy that. Similarly, if a user is invited to a black tie wedding, the algorithm willl be able to detect whether the user's outfit is black tie, white tie, formal, or semi formal. 

One challenge I am anticipating for this project is determining between stereotypical male and female norms of dressing. The standard of what people can wear for differetn events is constantly evolving and I do not want my device to perpetrate only heterosexual stereotypes For example, at the 2019 Met Gala, Michael Urie wore a half tuxedo half tulle gown outfit that was out of the box and seems difficult to classify; however, Urie is following the Met Gala's dress code. While this is a very specific situation, this challenge reflects the constantly shifting norms and trends of fashion that would be difficult to quantify in a dress code algorithm. 

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?

The model has the highest success rate when I tested it on the teachable machines website using photos I found online of casual, business casual, and business formal outfits. One mistake I was anticipating was failing when multiple people were shown in the photo but surprisingly, the model was accurate in classifying multiple people's outfits as business formal. Simialrly, I was anticipating classification issues with people who were not a typical "size small" and people with disabilities because the model was mainly trained on stock photos from website with people of stereotypical western beauty standards but the model was able to classify outfits on people who were not similar to the training data people. When I tested the model using the webcam and my raspberry pi, the model worked best when I was standing in front of a plain background with a lot of natural light.

3. When does it fail?

When testing the model using my raspberry pi and webcam, the model failed when I was standing too close to the camera and when the lighting was not bright. I had tested my device in the middle of the day and it was working well but when I changed it a bit and re tested in the evening, the device made many mistakes in classifying my outfits. Lastly, the model generally started classifying outfits with dark colors and business formal and bright colors as casual. 

5. When it fails, why does it fail?

Regarding the lighting, the device likely failed because the images it was picking up were not detailed enough to make a good prediction. Since the model worked better using my computer camera than it did with the raspberry pi webcome, a camera of a certain quality threshold would be necessary for the device to work best. Furthermore, my model may be overfit to the training data. Most of the suits I used for the business formal training data were dark blue, grey, or navy because those are the most common colors. However, this was generalized to classifying most. dark colored outfits included those with black t shirts and ripped black jeans as businness formal when they were most definitely casual. 

7. Based on the behavior you have seen, what other scenarios could cause problems?

While I was excited about building this device when the idea came to mind, while I was building it I saw how this device could be problematic in many ways. The model was trained on western standards of casual, business casual, and business formal. Seeing how the device was overfit to the training set, this device would not be effective on cultures with other standards of dress as well as people with disabilities that may not be able to conform to the traditional American dress codes. The training set was limited and improvements could be made if the model was able to generalize with a larger dataset. Similarly, the model was trained on stereotypical mens and womens styles of dress which despite my initial assumption that they were similar in the world of business fashion, they are not. My options here were to creat separate models for those two genderes or to combine them. I chose to combine them beucase I did not want to perpetrate gender norms and conform people to choosing male or female when using this device but the device did occasionally misclassify wearing athletic shorts or casual dresses as business casual, likely beucase of the business casual skirts used in the training set.

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?

I can use my dress code device to identify outfits that are casual, business casual, or business formal.

* What is a good environment for X?

A good environment for my dress code device is a well lit space with minimal background and a good quality webcam in the US. 

* What is a bad environment for X?

A bad environment for my dress code device is a low lit space with a business background with a lesser quality webcam in places that do not conform to American styles of dress. A bad environment would also be when the webcame can not see the user's full body 

* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
