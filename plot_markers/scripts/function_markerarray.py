#!/usr/bin/env python3

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy


count = 1

def main(x):

#For iterating the list

    for l in x:

        global count

        marker = Marker()
        ma = MarkerArray()

        marker.header.stamp = rospy.Time.now()
        marker.header.frame_id = "map"
        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.lifetime = rospy.Duration(0)
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.pose.orientation.w = 1.0
        marker.pose.position.x = l[0]
        marker.pose.position.y = l[1]
        marker.pose.position.z = l[2]
        marker.ns = "Point " + str(count) + " at {}".format(marker.pose.position)

#Appending the markers into markerarray

        ma.markers.append(marker)

# Initializing unique id for corresponding markers in markersarray

        id = 0
        for m in ma.markers:
            m.id = id
            id += 1
        
        rospy.sleep(2)
        pub.publish(ma)

        count += 1
        
        print("count is",count)

if __name__ == "__main__":
    
    rospy.init_node('markerarray')
    pub = rospy.Publisher("markerarray", MarkerArray,queue_size=10)
    points = [[1,1,1],[2,1,1], [3,1,1], [4,1,1]]
    main(points)