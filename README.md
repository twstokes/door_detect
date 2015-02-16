# door_detect
Detecting a garage door's status with a Foscam camera and OpenCV - written in Python

[Video Demo](https://www.youtube.com/watch?v=fCRlvkibfxc)

The goal of this project is to provide feedback to a user on whether a door is detected open or closed. It uses OpenCV to scan images for expected objects, and determines the physical orientation.

Currently it only supports network-attached Foscam cameras.

##### Process:

1. Load image from the camera
2. Look for certain objects in the image
3. If the objects are all detected the door is closed, if not it's open
4. Give feedback to the user on the door's state

##### What it takes to get it running:

* Python, python-cv2, python-numpy
* Networked Foscam (though it should be evident in the code how easy it is to replace the image data with any other source)
* Printed shapes placed on a door
* Template files of the shapes in the source image

#### Notes:

If you see the following in stdout: "Corrupt JPEG data: 2 extraneous bytes before marker 0xd9", it appears to be a known issue with a library OpenCV uses. Since we're just using it for outputting the status, it's not a big deal.
