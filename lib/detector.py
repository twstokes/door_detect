import numpy as np
import cv2
from lib import Shape

# class that detects objects and overlays a box
class Detector:
  def __init__(self, threshold, shapes, templateDir, horizAlignThresh):
    self.threshold = threshold
    self.shapes = shapes
    self.templateDir = templateDir
    self.horizAlignThresh = horizAlignThresh

  # detects image and overlays box on region of detection
  def detectAndOverlay(self, image, shape):
      # convert input image to gray
      imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

      # search for matches
      result = cv2.matchTemplate(imageGray, shape.templateImage, cv2.TM_CCOEFF_NORMED)

      # get our location and values of best match
      minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

      # determine if the match is good enough depending on our set threshold
      if maxVal >= (self.threshold / 100):
          # set top left coord
          topLeft = maxLoc

          # set bottom right coord
          bottomRight = (topLeft[0] + shape.width, topLeft[1] + shape.height)

          shape.setMatchInfo(topLeft, bottomRight, maxVal)

      return

  # looks for shapes in an image and returns whether they were found or not
  # if found returns top left and bottom right coords of surrounding box
  def findShapes(self, image):

      # dict to hold our shapes
      shapesDict = {}

      # iterate through our template names to create shapes
      for template in self.shapes:
          newShape = Shape(template, self.templateDir+'/'+template+'.png')
          # add to our dictionary of templates
          # value will be either coordinates or False
          self.detectAndOverlay(image, newShape)
          # add the shape to our dict
          shapesDict[template] = newShape

      # return our dictionary
      return shapesDict

  # detects and returns current state of the door
  def detectState(self, inputImage):
      # a dict of our shapes
      shapesDict = self.findShapes(inputImage)

      # default state is "fail"
      state = "fail"
      
      # by default, no detected shapes
      detectedShapesCount = 0

      for shape in shapesDict:
          if shapesDict[shape].detected == True:
              detectedShapesCount += 1

      # if the number of shapes detected equals the number of shapes,
      # we've detected all shapes
      if detectedShapesCount == len(shapesDict):
          cv2.rectangle(inputImage, shapesDict['triangle'].topLeft, shapesDict['pentagon'].bottomRight, (0, 255, 0), 2)
          triangleLeft = shapesDict['triangle'].topLeft[0]
          pentagonLeft = shapesDict['pentagon'].topLeft[0]
          # we're paying attention to the horizontal difference of the two
          # they should be pretty close at this distance
          horizDiff = abs(triangleLeft - pentagonLeft)

          # we're setting a horizontal threshold of 30 pixels
          # when it comes to vertical alignment of the two shapes
          # print "Horizontal difference between shapes:", horizDiff
          if horizDiff <= self.horizAlignThresh:
              state = "closed"
          else:
              state = "fail"
      else:
          state = "open"

      return state, shapesDict

  # currently experimental
  def diffStates(self, state1, state2):
      diffDict = {}

      state1Status = state1[0]
      state2Status = state2[0]

      state1Dict = state1[1]
      state2Dict = state2[1]

      if state1Status != state2Status:
          diffDict['doorStateChange'] = (state1Status, state2Status)
      else:
          diffDict['doorStateChange'] = None

      # iterate through state1 shapesDict that will have the same
      # dict layout as state2
      for shape in state1Dict:
          diffDict[shape] = {}
          #state1Dict[shape].printInfo()
          #state2Dict[shape].printInfo()
          if state1Dict[shape].detected != state2Dict[shape].detected:
              diffDict[shape]['detectionChange'] = (state1Dict[shape].detected, state2Dict[shape].detected)
          else:
              diffDict[shape]['detectionChange'] = None

          if state1Dict[shape].middle != state2Dict[shape].middle:
              diffDict[shape]['middleChange'] = (state1Dict[shape].middle, state2Dict[shape].middle)
          else:
              diffDict[shape]['middleChange'] = None

      return diffDict

  # iterates through our shapes list and prints info of each
  def printShapeInfo(self, shapeList):
      for shape in shapeList:
          shape.printInfo()






