#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
import tf_conversions

def publish_joint_states():
    rospy.init_node('joint_state_publisher', anonymous=True)
    joint_pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
    br = TransformBroadcaster()
    rate = rospy.Rate(10)  # 10 Hz

    joint_state = JointState()
    joint_state.name = ['wheel1_joint', 'wheel2_joint', 'wheel3_joint', 'wheel4_joint']
    joint_state.position = [0.0, 0.0, 0.0, 0.0]

    while not rospy.is_shutdown():
        joint_state.header.stamp = rospy.Time.now()
        joint_pub.publish(joint_state)

        t = TransformStamped()
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0
        t.transform.rotation = tf_conversions.transformations.quaternion_from_euler(0, 0, 0)
        
        br.sendTransform(t)

        rate.sleep()

if __name__ == '__main__':
    try:
        publish_joint_states()
    except rospy.ROSInterruptException:
        pass
