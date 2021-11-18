#!/usr/bin/env python3
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import rospy

count = 0
def main(x):
    # This function takes a list of lists with [x,y,z] coordinates
    # And spawn sphere with scale of(0.2,0.2,1.0) on rviz
    pub = rospy.Publisher("markerarray", MarkerArray,queue_size=10)
    global count
    for l1 in x:
        marker.header.frame_id = "map"
        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.pose.orientation.w = 1.0
        marker.pose.position.x = l1[0]
        marker.pose.position.y = l1[1]
        marker.pose.position.z = l1[2]
        count+=1
        id = count
        marker.id =id
        ma.markers.append(marker)
        rospy.sleep(5)
        print("count is",count)
        pub.publish(ma)


    

if __name__ == "__main__":
    rospy.init_node('markerarray')
    
    marker = Marker()
    ma = MarkerArray()
    mark = [[1,1,1],[1,2,1],[2,1,1],[2,2,1]]
    main(mark)
