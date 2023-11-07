import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

pose = Pose()

def go2goal(goal_x,goal_y):
    pass

def posecallback1(msg):
    pose = msg

def main():
    rospy.init_node('gotogoal', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=15)
    sub = rospy.Subscriber('/turtle1/pose', Pose, posecallback1)


    pass


if __name__ == '__main__':
    try:
        
        main()
    except rospy.ROSInterruptException:
        pass
