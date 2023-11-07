#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
from time import sleep

class gotogoal():
    def __init__(self) -> None:
        rospy.init_node('gotogoal', anonymous=True)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.posecallback1)
        self.rate = rospy.Rate(10)
        self.pose = Pose()
        self.goal_pose = Pose()
        self.vel = Twist()
        self.distance = 0
        self.angle = 0

    def posecallback1(self, msg1):
        self.pose = msg1
        self.x = round(self.pose.x,4)
        self.y = round(self.pose.y,4)

    def move2goal(self):
        self.goal_pose.x = float(input("Enter goal x - ")) #input the goal co-ordinates
        self.goal_pose.y = float(input("Enter goal y - "))
        self.distance = sqrt(pow((self.goal_pose.x - self.pose.x), 2) + pow((self.goal_pose.y - self.pose.y), 2)) #linear error
        self.angle = atan2(self.goal_pose.y - self.pose.y, self.goal_pose.x - self.pose.x) #angular error
        self.vel.linear.x = 1.5 * self.distance
        self.vel.angular.z = 6 * (self.angle - self.pose.theta)
        self.pub.publish(self.vel)
        self.rate.sleep()
        while self.distance >= 0.1: #tolerance value is taken as 0.1
            self.distance = sqrt(pow((self.goal_pose.x - self.pose.x), 2) + pow((self.goal_pose.y - self.pose.y), 2))
            self.angle = atan2(self.goal_pose.y - self.pose.y, self.goal_pose.x - self.pose.x)
            self.vel.linear.x = 1.5 * self.distance
            self.vel.angular.z = 6 * (self.angle - self.pose.theta)
            self.pub.publish(self.vel)
            self.rate.sleep()
        self.vel.linear.x = 0
        self.vel.angular.z = 0        
        self.pub.publish(self.vel)
        rospy.spin()

if __name__ == '__main__':
    try:
        turtle = gotogoal()
        turtle.move2goal()
    except rospy.ROSInterruptException:
        pass