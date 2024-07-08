#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def joint_command_callback(msg):
    rospy.loginfo("Received joint command: %f", msg.data)

def joint_command_subscriber():
    rospy.init_node('joint_command_subscriber', anonymous=True)
    rospy.Subscriber('/joint_commands', Float64, joint_command_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        joint_command_subscriber()
    except rospy.ROSInterruptException:
        pass
