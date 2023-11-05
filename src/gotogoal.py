#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

pub = None
pose = Pose()
speed = Twist()
sub = None

def callback(data):
    pose = data
    rospy.loginfo("x: %f, y: %f", pose.x, pose.y)

def gotogoal():
    rospy.init_node('gotogoal', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/turtle1/pose', Pose, callback)
    rate = rospy.Rate(10)

    goal_pose = Pose()
    goal_pose.x = 6
    goal_pose.y = 6
    # goal_pose.theta = 2.4 #radians

    kp_v = 0.1
    kp_w = 1.0
    error = sqrt(pow((goal_pose.x - pose.x), 2) + pow((goal_pose.y - pose.y), 2))
    while error > 0.01:
        error = sqrt(pow((goal_pose.x - pose.x), 2) + pow((goal_pose.y - pose.y), 2)) #distance to goal
        rot_error = atan2(goal_pose.y - pose.y, goal_pose.x - pose.x) - pose.theta

        speed.linear.x = kp_v * error
        speed.angular.z = kp_w * rot_error
        pub.publish(speed)
        rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    try:
        gotogoal()
    except rospy.ROSInterruptException:
        pass
