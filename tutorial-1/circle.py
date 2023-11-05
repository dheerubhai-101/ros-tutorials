#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def circle():
    # Your code goes here
    #
    # Your goal is to make a circle by giving linear and angular velocity commands to the turtle
    #
    # Now as the turle moves only in 2D and in striaght line, linear velocity in x direction and 
    # angular velocity along z direction will be important.

def main():
    rospy.init_node('circle',anonymous=True)
    pub = rospy.Publisher('________',Twist,queue_size=10)
    rate = rospy.Rate(10)
    circle()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")