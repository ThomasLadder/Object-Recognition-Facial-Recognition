# Object-Recognition-Facial-Recognition
Tech demo for Technology + Ethics

## Object-Recogntion
Object recognition will be ran on the Raspberry Pi. Demo requires Tensorflow, OpenCV, and Protobuf.

### Usage
Boot up Raspberry Pi. Make sure camera module is plugged in and propped up on "camera stand". To run the object recognition script, navigate to the correct directory:
```
cd /home/pi/tensorflow1/models/research/object_detection
```
Now simply run the script with python3:
```
python3 Object_detection_picamera.py
```
The script will take up to 30 seconds to run. Eventually, a window labeled "Object detector" should pop up. This window shows the view of the camera. It will draw a rectangle around any objects it recognizes, with the name of the object and the % confidence that it is that object. 

### Information
The model I am running is called ssdlite_mobilenet_v2_coco. It is a pre-trained model that is optimized for low-power machines. That means it sacrifices a bit of accuracy and frame rate so it can run on the Raspberry Pi, but it works fine for a demo. The model is trained to recognize 90 objects, which are listed here: https://github.com/amikelive/coco-labels/blob/master/coco-labels-paper.txt

### Adjustments
The main adjustment I have made to the model is a single change in labeling. I changed the label of "cell phone" to "gun", which means every time the model recognizes a cell phone, it will label it as "gun". This is to get some conversation started by framing an example of a deadly mistake that actual humans have made.

## Facial-Recongition
Facial-Recognition will be ran on Macbook Pro. Demo requires Tensorflow, OpenCV, and Dlib.

### Usage
Navigate to 
