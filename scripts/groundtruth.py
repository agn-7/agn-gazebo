#!/usr/bin/env python

import rospy

from gazebo_msgs.msg import ModelStates
from sensor_msgs.msg import PointCloud2


__author__ = 'aGn'

ROTARY_MODEL_NAME = rospy.get_param('/agn_gazebo/rotary_model_name')
LINEAR_MODEL_NAME = rospy.get_param('/agn_gazebo/linear_model_name')
PATH_TO_SAVE = rospy.get_param('/agn_gazebo/path_to_save')


class GroundTruth(object):
    def __init__(self):
        self.frame = 0
        print("The .csv files store in " + PATH_TO_SAVE)
        rospy.Subscriber("/gazebo/model_states", ModelStates, self.export_pose, queue_size=1)
        rospy.Subscriber("/velodyne_points", PointCloud2, self.get_frame, queue_size=1)

    def get_frame(self, pcl):
        self.frame += 1

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

        with open(PATH_TO_SAVE + 'groundtruth_linear.csv', mode='a') as file_:
            file_.write("{},{},{}".format(self.frame, pose_x_1, pose_y_1))
            file_.write("\n")

        with open(PATH_TO_SAVE + 'groundtruth_rotary.csv', mode='a') as file_:
            file_.write("{},{},{}".format(self.frame, pose_x_2, pose_y_2))
            file_.write("\n")


if __name__ == "__main__":
    rospy.init_node('agn_gazebo', anonymous=True)
    GroundTruth()
    rospy.spin()
