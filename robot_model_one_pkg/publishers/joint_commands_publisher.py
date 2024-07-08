#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def publish_joint_commands():
    rospy.init_node('joint_command_publisher', anonymous=True)
    pub = rospy.Publisher('/joint_commands', Float64, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    command = 1.0  # Example command

    while not rospy.is_shutdown():
        pub.publish(command)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_joint_commands()
    except rospy.ROSInterruptException:
        pass
