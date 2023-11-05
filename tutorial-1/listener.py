#!/usr/bin/env python

import rospy
from std_msgs.msg import String
#Callback function to print the subscribed data on the terminal
def callback_str(subscribedData):
     rospy.loginfo('Subscribed: ' + subscribedData.data)

     
#Subscriber node function which will subscribe the messages from the Topic
def messageSubscriber():
    #initialize the subscriber node called 'messageSubNode'
    rospy.init_node('messageSubNode', anonymous=False)
    #This is to subscribe to the messages from the topic named 'messageTopic'
    rospy.Subscriber('messageTopic', String, callback_str)
    #rospy.spin() stops the node from exitind until the node has been shut down
    print("\n listener stream")
    rospy.spin()
if __name__ == '__main__':
    try:
        messageSubscriber()
    except rospy.ROSInterruptException:
        pass