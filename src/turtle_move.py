#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

if __name__=='__main__':
    try:
        rospy.init_node('turtle_move', anonymous=True)
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            msg = Twist()
            msg.linear.x = 1.0
            msg.angular.z = 0.0
            pub.publish(msg)
            rate.sleep()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass