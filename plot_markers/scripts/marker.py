# #!/usr/bin/env python3

# import rospy
# import time
# from visualization_msgs.msg import Marker 

# def marker():

#     rospy.init_node("marker",anonymous = True)
#     pub = rospy.Publisher("/Marker_topic", Marker, queue_size=1)

#     while not rospy.is_shutdown():

#         M = Marker()
#         M.header.frame_id = "map"
#         M.id = 0
#         M.header.stamp = rospy.Time.now()
#         M.ns = "My_marker"
#         M.type = M.SPHERE
#         M.action = M.ADD
        
#         M.scale.x = 1
#         M.scale.y = 1
#         M.scale.z = 1

#         M.color.a = 1.0
#         M.color.g = 1.0
#         M.color.r = 1.0

#         M.pose.position.x = 1
#         M.pose.position.y = 1
#         M.pose.position.z = 0
#         M.pose.orientation.x = 0
#         M.pose.orientation.y = 0
#         M.pose.orientation.z = 0
#         M.pose.orientation.w = 1.0

#         pub.publish(M)
#         # rospy.spin()
#         rospy.sleep(10)


# if __name__ == "__main__":
#     marker()



