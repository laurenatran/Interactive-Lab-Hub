# Interactive Prototyping: The Clock of Pi

Does it feel like time is moving strangely during this semester?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

**Please indicate anyone you collaborated with on this Lab here.**
<<<<<<< HEAD
For this lab I worked on my own
=======
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

## Prep

[Lab prep](prep.md) is extra long this week! Make sure you read it over in time to prepare for lab on Thursday.

### Get your kit
If you are remote but in the US, let the teaching team know you need the parts mailed.


If you are in New York, you can come to the campus and pick up your parts. If you have not picked up your parts by Thursday lab you should come to Tata 351.
>>>>>>> b4f31bcf6c9d48655b13298e331b4c0ee4919ec7


### Set up your Lab 2

<<<<<<< HEAD
=======
1. [Pull changes from the Interactive Lab Hub](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md#to-pull-lab-updates) so that you have your own copy of Lab 2 on your own lab hub. (This may have to be done again at the start of lab on Thursday.)
  
  If you are organizing your Lab Hub through folder in local machine, go to terminal, cd into your Interactive-Lab-Hub folder and run:

  ```
  Interactive-Lab-Hub $ git remote add upstream https://github.com/FAR-Lab/Interactive-Lab-Hub.git
  Interactive-Lab-Hub $ git pull upstream Fall2021
  ```
  
  The reason why we are adding a upstream with **course lab-hub** instead of yours is because the local Interactive-Lab-Hub folder is linked with your own git repo already. Try typing ``git remote -v`` and you should see there is the origin branch with your own git repo. We here add the upstream to get latest updates from the teaching team by pulling the **course lab-hub** to your local machine. After your local folder got the latest updates, push them to your remote git repo by running:
  
  ```
  Interactive-Lab-Hub $ git add .
  Interactive-Lab-Hub $ git commit -m "message"
  Interactive-Lab-Hub $ git push
  ```
  Your local and remote should now be up to date with the most recent files.

2. Go to the [lab prep page](prep.md) to inventory your parts and set up your Pi before the lab session on Thursday.


>>>>>>> b4f31bcf6c9d48655b13298e331b4c0ee4919ec7
## Overview
For this assignment, you are going to 

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)

## The Report

## Part A. 
### Connect to your Pi
### Setup Personal Access Tokens on GitHub


## Part B. 
### Try out the Command Line Clock

## Part C. 
### Set up your RGB Display

### Hardware (you have done this in the prep)


### Testing your Screen

#### Displaying Info with Texts

#### Displaying an image


## Part D. 
### Set up the Display Clock Demo

### How to Edit Scripts on Pi



## Part E.
### Modify the barebones clock to make it your own

Does time have to be linear?  How do you measure a year? [In daylights? In midnights? In cups of coffee?](https://www.youtube.com/watch?v=wsj15wPpjLY)

Can you make time interactive? You can look in `screen_test.py` for examples for how to use the buttons.



\*\*\***A copy of your code should be in your Lab 2 Github repo.**\*\*\*

For this project, I was inspired by my family's tradition of considering dates in the fall only in relation to holidays. My birthday as well as my 2 sisters' birthdays are in the fall, followed closely by Halloween, Thanksgiving, Christmas, and New Years. I decided to propgram my clock so that the date is shown only in relation to the next holiday, using colors that represented each event. 

My code in screen_clock.py is configured using the strftime to capture current dates and times. The code in screen_clock_example.py is a similar version of the code in screen_clock.py but allows me to input dates so that I can show what the clock looks like on any given date. 


## Part F. 
## Make a short video of your modified barebones PiClock

\*\*\***Take a video of your PiClock.**\*\*\*
https://drive.google.com/file/d/1D1cZJM2ePubKxQdQTBiHWnK5oVR9BZ9V/view?usp=sharing

## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.

Future ideas:
One possible addition could be to add background images to the clock interface so it looks less boring when announcing holidays. 

Another idea I had was to use the buttons to allow users to see the next holiday following the upcoming one. For example, my birthday is September 29 so until then, I will see the countdown to my birthday. However, if I press one of the buttons, I would be able to see a countdown to my sister Sydney's birthday which is the next holiday after my birthday. 

I could also add a feature for users to input their own holidays so that the clock is more inclusive. Rather than comming pre programed with holidays, the user could add in the holidays they celebrate. 


# Prep for Part 2

1. Pick up remaining parts for kit on Thursday lab class. Check the updated [parts list inventory](partslist.md) and let the TA know if there is any part missing.
  

2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)

# Lab 2 Part 2

Pull Interactive Lab Hub updates to your repo.

Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required.

As always, make sure you document contributions and ideas from others explicitly in your writeup.

You are permitted (but not required) to work in groups and share a turn in; you are expected to make equal contribution on any group work you do, and N people's group project should look like N times the work of a single person's lab. What each person did should be explicitly documented. Make sure the page for the group turn in is linked to your Interactive Lab Hub page. 

Part 2 Video: https://drive.google.com/file/d/1PNL22F6hqBPmfYYdLQ-XYF7fjA-Oah3S/view?usp=sharing 


