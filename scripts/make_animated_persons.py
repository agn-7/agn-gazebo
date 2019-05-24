#!/usr/bin/env python

import rospy

from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState


dummy = "rosservice call /gazebo/set_model_state '{model_state: { model_name: model1.sdf, pose: { position: { x: 0.0, y: 0.0 ,z: 0.1 }, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 0.0 } }, twist: { linear: {x: 0.0 , y: 0 ,z: 0 } , angular: { x: 0.0 , y: 0 , z: 0.0 } } , reference_frame: world } }'"


def run():
    try:
        srv_ = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)

        msg_ = ModelState()

        msg_.model_name = 'model1.sdf'
        msg_.pose.position.x = -1.3
        msg_.pose.position.y = 3.2
        msg_.pose.position.z = 0
        msg_.pose.orientation.x = 0
        msg_.pose.orientation.y = 0.491983115673
        msg_.pose.orientation.z = 0
        msg_.pose.orientation.w = 0.870604813099
        msg_.twist.linear.x = 0.0
        msg_.twist.linear.y = 0
        msg_.twist.linear.z = 0
        msg_.twist.angular.x = 0.0
        msg_.twist.angular.y = 0
        msg_.twist.angular.z = 0.0
        msg_.reference_frame = 'world'

        res = srv_(msg_)
        print(res)

    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


if __name__ == "__main__":
    run()
