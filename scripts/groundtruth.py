#!/usr/bin/env python

import rospy

from gazebo_msgs.msg import ModelStates


__author__ = 'aGn'

DUMMY = """
rosservice call /gazebo/set_model_state '{model_state: {model_name: model1.sdf, 
pose: {position: {x: 0.0, y: 0.0 ,z: 0.1}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 0.0}},
twist: {linear: {x: 0.0 , y: 0 ,z: 0}, angular: {x: 0.0 , y: 0 , z: 0.0}},
reference_frame: world}}'
"""

ROTARY_MODEL_NAME = rospy.get_param('/agn_gazebo/rotary_model_name')
LINEAR_MODEL_NAME = rospy.get_param('/agn_gazebo/linear_model_name')


class GroundTruth(object):
    def __init__(self):
        rospy.Subscriber("/gazebo/model_states", ModelStates, self.export_pose, queue_size=1)

    def export_pose(self, models_state):
        try:
            index_ = models_state.name.index(ROTARY_MODEL_NAME)
            index_2 = models_state.name.index(LINEAR_MODEL_NAME)
        except:
            index_ = -1
            index_2 = -1

        '''Get rotary model init pose'''
        pose_x_1 = models_state.pose[index_].position.x
        pose_y_1 = models_state.pose[index_].position.y

        '''Get linear model init pose'''
        pose_x_2 = models_state.pose[index_2].position.x
        pose_y_2 = models_state.pose[index_2].position.y

        with open('/home/agn/groundtruth_linear.csv', mode='a') as file_:
            file_.write("{},{}".format(pose_x_1, pose_y_1))
            file_.write("\n")

        with open('/home/agn/groundtruth_rotary.csv', mode='a') as file_:
            file_.write("{},{}".format(pose_x_2, pose_y_2))
            file_.write("\n")


if __name__ == "__main__":
    rospy.init_node('agn_gazebo', anonymous=True)
    GroundTruth()
    rospy.spin()
