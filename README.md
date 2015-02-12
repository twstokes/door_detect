# door_detect
Detecting a garage door's status with a Foscam camera and OpenCV - written in Python

The goal of this project is to provide feedback to a user on whether a door is detected open or closed. It uses OpenCV to scan images for expected objects, and determines the physical orientation.

Currently it only supports network-attached Foscam cameras.

Process:
1. Load image from the camera
2. Look for certain objects in the image
3. If the objects are all detected the door is closed, if not it's open
4. Give feedback to the user on the door's state
