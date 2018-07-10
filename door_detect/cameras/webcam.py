import cv2

class Webcam:
    def __init__(self, capture):
        self.cap = cv2.VideoCapture(capture)

    def getSnapshotCV(self):
        _, frame = self.cap.read()
        return frame

    def release(self):
        self.cap.release()