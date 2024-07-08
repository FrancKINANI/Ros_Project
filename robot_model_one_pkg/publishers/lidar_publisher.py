#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import random

def publish_lidar_scan():
    rospy.init_node('lidar_publisher', anonymous=True)
    scan_pub = rospy.Publisher('/scan', LaserScan, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        scan = LaserScan()
        scan.header.stamp = rospy.Time.now()
        scan.header.frame_id = 'lidar_link'
        scan.angle_min = -1.57
        scan.angle_max = 1.57
        scan.angle_increment = 3.14 / 720
        scan.time_increment = (1.0 / 30) / 720
        scan.range_min = 0.2
        scan.range_max = 30.0
        scan.ranges = [random.uniform(0.2, 30.0) for _ in range(720)]
        scan.intensities = [random.uniform(0.0, 1.0) for _ in range(720)]
        
        scan_pub.publish(scan)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_lidar_scan()
    except rospy.ROSInterruptException:
        pass
