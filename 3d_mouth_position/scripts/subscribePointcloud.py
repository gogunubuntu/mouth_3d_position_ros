#!/usr/bin/env python
import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def callback(data):
    rospy.loginfo("asdf")

def imageCallback(data) : 
    rospy.loginfo("image")
rospy.init_node('converter', anonymous=True)

rospy.Subscriber("/camera/depth_registered/points", PointCloud2, callback)
rospy.Subscriber("/camera/color/image_raw", Image, imageCallback)


rospy.spin()

