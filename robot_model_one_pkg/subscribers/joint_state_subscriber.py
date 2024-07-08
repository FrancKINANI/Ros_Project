#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState

def joint_state_callback(msg):
    rospy.loginfo("Received joint states: %s", msg)

def joint_state_subscriber():
    rospy.init_node('joint_state_subscriber', anonymous=True)
    rospy.Subscriber('/joint_states', JointState, joint_state_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        joint_state_subscriber()
    except rospy.ROSInterruptException:
        pass
