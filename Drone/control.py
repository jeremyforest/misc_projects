from pyparrot.Bebop import Bebop
from pyparrot.DroneVisionGUI import DroneVisionGUI
import threading
import cv2
import time

import vlc


## Original sample code from https://pyparrot.readthedocs.io/en/latest/vision.html
class UserVision:
    def __init__(self, vision):
        self.index = 0
        self.vision = vision

    def save_pictures(self, args):
        #print("saving picture")
        img = self.vision.get_latest_valid_picture()

        if (img is not None):
            filename = "test_image_%06d.png" % self.index
            #cv2.imwrite(filename, img)
            self.index +=1


def demo_user_code_after_vision_opened(bebopVision, args):
    bebop = args[0]

    print("Vision successfully started!")

    if (bebopVision.vision_running):
        print("Moving the camera using velocity")
        bebop.pan_tilt_camera_velocity(pan_velocity=0, tilt_velocity=-2, duration=4)

        bebopVision.close_video()




if __name__ == "__main__":
    #Create the drone object
    bebop = Bebop()
    #connect to the drone
    success = bebop.connect(num_retries=3)
    print("battery life is at " + str(bebop.sensors.battery) + "%")

    # if success:
    print("Connected to the drone")

    # #set maximum speed
    # bebop.set_max_tilt(5)
    # bebop.set_max_vertical_speed(1)
    # bebop.flat_trim()
    #
    # #take off
    # bebop.safe_takeoff(5)
    #
    # #fly
    # bebop.fly_direct(roll=0, pitch=1, yaw=0, vertical_movement=0, duration=1)
    #
    # #land
    # bebop.safe_land(5)
    # start up the video

    bebopVision = DroneVisionGUI(bebop, is_bebop=True, user_code_to_run=demo_user_code_after_vision_opened,
                                 user_args=(bebop, ))

    userVision = UserVision(bebopVision)
    bebopVision.set_user_callback_function(userVision.save_pictures, user_callback_args=None)
    bebopVision.open_video()


        #disconnect
        # bebop.d   isconnect()

    # else:
    #     print("Error connecting to bebop.  Retry")
    #


"""
## possible commands
connect(num_retries)
disconnect()
safe_takeoff(timeout)
safe_land(timeout)
set_max_tilt(degrees)
set_max_vertical_speed(speed)
flat_trim()
smart_sleep(seconds)
fly_direct(roll, pitch, yaw, vertical_movement, duration)
"""
