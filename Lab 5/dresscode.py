
#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
from time import sleep


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      print("Unable to access webcam.")


# Load the model
model = tensorflow.keras.models.load_model('dresscode_keras_model.h5')
# Load Labels:
labels=[]
f = open("dresscode_labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())

signal = input('Type "ready" when you have your outfit on! Once you are ready, you will have 5 seconds to get into position! Make sure your whole body is shown in the camera.')

while(signal == 'ready'):
#if signal == 'ready':
    sleep(5)
    if webCam:
        ret, img = cap.read()

    rows, cols, channels = img.shape
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    size = (224, 224)
    img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    #turn the image into a numpy array
    image_array = np.asarray(img)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    ###############
    prediction = model.predict(data)
    print("Your outfit is: ",labels[np.argmax(prediction)])

   
    if webCam:
        if sys.argv[-1] == "noWindow":
           cv2.imwrite('detected_out.jpg',img)
           continue
        cv2.imshow('detected (press q to quit)',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
    else:
        break
    signal = input('Type "ready" when you have your outfit on!')

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()
