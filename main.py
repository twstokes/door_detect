import config
import sys
import traceback
import numpy as np
import cv2
import time

from lib import Detector
from lib import Foscam


if __name__ == '__main__':
  try:
    # used for local testing
    #inputImage = cv2.imread('door_down.jpg')
    previousState = None

    while True:
        # get live webcam data
        camera = Foscam(config.CAMADDRESS, config.USERNAME, config.PASSWORD)
        webcamImage = camera.getSnapshot()

        # convert webcam returned data to array
        imageDataArray = np.asarray(bytearray(webcamImage), dtype=np.uint8)

        # create an opencv image with webcam data
        inputImage = cv2.imdecode(imageDataArray, cv2.IMREAD_ANYCOLOR)

        detector = Detector(config.THRESHOLD, config.SHAPES, config.TEMPLATEDIR, config.HORIZ_ALIGN_THRESH)

        currentState = detector.detectState(inputImage)
        
        #if(previousState != None):
        #    statesDiff = Detector.diffStates(currentState, previousState)
        #    print statesDiff

        print currentState[0]
        # output image with overlays
        cv2.imwrite(config.OUTPUTDIR+'/'+str(time.time())+'.png', inputImage)
        # sleep for a second
        #previousState = currentState
        time.sleep(.2)


  except Exception, e:
    print "Fatal error."
    print e
    print traceback.format_exc()
    sys.exit(1)
