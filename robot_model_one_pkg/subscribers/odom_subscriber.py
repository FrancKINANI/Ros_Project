#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def odom_callback(msg):
    rospy.loginfo("Received odometry: %s", msg)

def odom_subscriber():
    rospy.init_node('odom_subscriber', anonymous=True)
    rospy.Subscriber('/odom', Odometry, odom_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        odom_subscriber()
    except rospy.ROSInterruptException:
        pass
