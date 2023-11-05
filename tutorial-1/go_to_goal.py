#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class Turtlesim:
    def __init__(self):
        rospy.init_node("turtlesim_motion_pose",anonymous=True)
        self.pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
        self.pose_sub = rospy.Subscriber("/turtle1/pose",Pose,self.poseCallback)
        self.pose = Pose()
        self.rate = rospy.Rate(30)

    def poseCallback(self,pose_message):
        # callback function to read the current pose of turtle and store it in a global variable 

    def distance(self,goal):
        # Calculating euclidean distance between goal pose and turtle's current pose

    def linear_vel(self,goal,k_l = 1.5):
        return k_l * self.distance(goal)

    def steering_angle(self,goal):
        # Calculating angle between goal pose and turtle's current pose

    def angular_vel(self,goal, k_a = 6):
        return k_a * (self.steering_angle(goal) - self.pose.theta)
        
    def go_to_goal(self):
        # Initialising the goal pose variable
        # Publishing velocity commands based on distance and steering angle functions
        # How do you ensure that turtle has reached the goal? 

if __name__ == "__main__":
    try:
        g2g = Turtlesim()
        g2g.go_to_goal()
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")