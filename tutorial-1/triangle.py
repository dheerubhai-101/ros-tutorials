#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

def triangle(side):
    global vel,pub,rate
    rospy.init_node('triangle',anonymous=True)
    pub = rospy.Publisher('_________',______,queue_size=10)
    rate = rospy.Rate(30)
    vel = Twist()
    rotations = 0

    while rotations < 3:
        triangle_side(side)
        rotations += 1

def triangle_side(side):
    # Tracing the side length of the triangle
    # You have to give a constant linear velocity
    # To keep track of distance covered 
    # you can calculate time required to cover the distance 
    # using rospy.Time.now().to_sec()
    
    turn() # turn after covering one side

def turn():
    # Rotating by 120 degrees

if __name__ == '__main__':
    try:
        triangle(5)
    except rospy.ROSInterruptException:
        pass