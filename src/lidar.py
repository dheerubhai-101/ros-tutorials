#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32

class laserscan():
    def __init__(self) -> None:
        rospy.init_node("laserscan_node", anonymous=True)
        self.scan_sub = rospy.Subscriber("/scan", LaserScan, self.callback)
        self.scan_pub = rospy.Publisher("/scan_at_x", Float32, queue_size=10)
        self.scan0 = Float32()


        
    
    def callback(self, msg):
        a_min = msg.angle_min
        self.incres = msg.angle_increment
        self.n = round((msg.angle_max - msg.angle_min)/msg.angle_increment)
        self.range0 = msg.ranges[round(self.n/2)]
        self.scan0.data = self.range0

    def scan_publish(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.scan_pub.publish(self.scan0)
            rate.sleep()


if __name__ == "__main__":
    laser = laserscan()
    laser.scan_publish()
    rospy.spin()
        