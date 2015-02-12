import config
import sys
import traceback
import time

from lib import Detector
from lib import Foscam


if __name__ == '__main__':
  try:
    # used for local testing
    #inputImage = cv2.imread('door_down.jpg')
    previousState = None

    while True:
        # set up camera object
        camera = Foscam(config.CAMADDRESS, config.USERNAME, config.PASSWORD)

        # get live webcam data in OpenCV format
        inputImage = camera.getSnapshotCV()

        # set up our detector object
        detector = Detector(config.THRESHOLD, config.SHAPES, config.TEMPLATEDIR, config.HORIZ_ALIGN_THRESH, config.OUTPUTDIR, config.OUTPUT_DETECTION_IMAGE)

        # get the current state of the door
        currentState = detector.detectState(inputImage)
        
        # experimental
        #if(previousState != None):
        #    statesDiff = detector.diffStates(currentState, previousState)
        #    print statesDiff

        # output the state of the door
        print "Current state: ", currentState[0]

        #previousState = currentState
        time.sleep(.2)


  except Exception, e:
    print "Fatal error."
    print e
    print traceback.format_exc()
    sys.exit(1)
