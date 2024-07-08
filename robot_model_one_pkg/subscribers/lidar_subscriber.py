#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
    rospy.loginfo("Received a LiDAR scan")
    rospy.loginfo("Ranges: {}".format(msg.ranges))

def lidar_subscriber():
    rospy.init_node('lidar_subscriber', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, scan_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        lidar_subscriber()
    except rospy.ROSInterruptException:
        pass
