import httplib

# class used to interact and fetch data with a Foscam camera
class Foscam:
  def __init__(self, address, username, password):
    self.address = address
    self.username = username
    self.password = password

  # gets live image from webcam and tries to return an OpenCV image
  def getSnapshot(self):
    # set up our http connection
    conn = httplib.HTTPConnection(self.address)

    try:
      # make a GET request to the cam
      conn.request("GET", "/snapshot.cgi?user="+self.username+"&pwd="+self.password)
    except:
      raise Exception, "Failed to make a request to "+self.address

    # read our response
    response = conn.getresponse()

    # check to see if our request was successful
    if response.status == 200:
      imageData = response.read()
    else:
      raise Exception, "Did not get a successful response from camera - aborting. Check username and password."

    return imageData