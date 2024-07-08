#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_callback(msg):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    cv2.imshow("Camera Image", cv_image)
    cv2.waitKey(1)

def camera_subscriber():
    rospy.init_node('camera_subscriber', anonymous=True)
    rospy.Subscriber('/camera/image_raw', Image, image_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        camera_subscriber()
    except rospy.ROSInterruptException:
        pass
