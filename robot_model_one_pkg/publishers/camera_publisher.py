#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def publish_camera_image():
    rospy.init_node('camera_publisher', anonymous=True)
    image_pub = rospy.Publisher('/camera/image_raw', Image, queue_size=10)
    bridge = CvBridge()
    rate = rospy.Rate(10)  

    cap = cv2.VideoCapture(0)  

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:
            image_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            image_pub.publish(image_msg)
        rate.sleep()

    cap.release()

if __name__ == '__main__':
    try:
        publish_camera_image()
    except rospy.ROSInterruptException:
        pass
