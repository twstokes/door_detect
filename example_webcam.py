import config
import sys
import traceback
import time

from door_detect import Detector
from door_detect.cameras import Webcam


if __name__ == '__main__':
  # set up camera object - if you have multiple cameras, changed this integer to reference their ID!
  camera = Webcam(0)

  try:
    previousState = None

    while True:
        # get live webcam data in OpenCV format
        inputImage = camera.getSnapshotCV()

        # set up our detector object
        detector = Detector(config.THRESHOLD, config.SHAPES, config.TEMPLATEDIR, config.HORIZ_ALIGN_THRESH, config.OUTPUTDIR, config.OUTPUT_DETECTION_IMAGE)

        # get the current state of the door
        currentState = detector.detectState(inputImage)
        
        # output the state of the door
        print "Current state: ", currentState[0]

        #previousState = currentState
        time.sleep(.2)


  except Exception, e:
    print "Fatal error."
    print e
    print traceback.format_exc()
    camera.release()
    sys.exit(1)
