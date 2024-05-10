# from pyparrot.Bebop import Bebop
# from pyparrot.DroneVisionGUI import DroneVisionGUI
# import threading
# import cv2
# import time
#
# import generated_vlc
#
# bebop = Bebop()
# success = bebop.connect(num_retries=3)
# bebop.sensors.battery
# bebopVision = DroneVisionGUI(bebop, is_bebop=True, user_code_to_run="", user_args=(bebop, ))
# bebopVision.open_video()



import cv2

cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
gst = "rtspsrc location=rtp://192.168.99.1/media/stream2 latency=10 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! appsink"
cap = cv2.VideoCapture(gst)
while(cap.isOpened()):
    ret, frame = cap.read()
    # you can add your processing here on the frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
