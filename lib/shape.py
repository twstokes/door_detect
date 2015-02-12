import cv2

# class to store our shapes
class Shape:
  def __init__(self, name, templateImageFile):
    self.name = name
    # create an OpenCV image for this shape's template
    self.templateImage = cv2.imread(templateImageFile, 0)
    self.width, self.height = self.templateImage.shape[::-1]

  def setMatchInfo(self, topLeft, bottomRight, maxValue):
    # set middle coords of the square that found the shape
    middleX = (topLeft[0] + bottomRight[0]) / 2
    middleY = (topLeft[1] + bottomRight[1]) / 2
    self.middle = (middleX, middleY)
    # set the top left coords of the square that found the shape
    self.topLeft = topLeft
    # set the bottom right coords of the square that found the shape
    self.bottomRight = bottomRight
    # set the max value of the template match
    self.maxValue = maxValue
    # this shape was detected, but could still be a false positive
    self.detected = True

  # dump out shape info
  def printInfo(self):
    print "Name:", self.name
    print "Width:", self.width
    print "Height:", self.height
    print "Detected:", self.detected
    print "Match max value:", self.maxValue
    print "Middle coords:", self.middle
    print "Top left coords of detection box:", self.topLeft
    print "Bottom right coords of detection box:", self.bottomRight, "\n"