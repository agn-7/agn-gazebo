#!/usr/bin/env python

import rospy
import math

from time import sleep

from gazebo_msgs.msg import ModelState, ModelStates
from gazebo_msgs.srv import SetModelState


__author__ = 'aGn'

DUMMY = """
rosservice call /gazebo/set_model_state '{model_state: {model_name: model1.sdf, 
pose: {position: {x: 0.0, y: 0.0 ,z: 0.1}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 0.0}},
twist: {linear: {x: 0.0 , y: 0 ,z: 0}, angular: {x: 0.0 , y: 0 , z: 0.0}},
reference_frame: world}}'
"""

RADIUS = float(rospy.get_param('/agn_gazebo/radius'))
STEP = float(rospy.get_param('/agn_gazebo/step'))
SLEEP = float(rospy.get_param('/agn_gazebo/sleep'))
ROTARY_MODEL_NAME = rospy.get_param('/agn_gazebo/rotary_model_name')
REACH = float(rospy.get_param('/agn_gazebo/reach'))
LINEAR_MODEL_NAME = rospy.get_param('/agn_gazebo/linear_model_name')


class Animating(object):
    def __init__(self):
        rospy.Subscriber("/gazebo/model_states", ModelStates, self.run, queue_size=1)

    def run(self, models_state):
        srv_ = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)

        try:
            index_ = models_state.name.index(ROTARY_MODEL_NAME)
            index_2 = models_state.name.index(LINEAR_MODEL_NAME)
        except:
            index_ = -1
            index_2 = -1

        '''Get rotary model init pose'''
        init_x = models_state.pose[index_].position.x
        init_y = models_state.pose[index_].position.y

        '''Get linear model init pose'''
        init_x_2 = models_state.pose[index_2].position.x
        init_y_2 = models_state.pose[index_2].position.y

        msg_ = ModelState()
        msg_2 = ModelState()
        msg_.model_name = ROTARY_MODEL_NAME
        msg_2.model_name = LINEAR_MODEL_NAME

        '''Circle equation: (x-a)**2 + (y-b)**2 = r**2'''
        a = init_x - RADIUS
        b = init_y
        x_sign = -1  # Counterclockwise
        y_sign = 1
        msg_.pose.position.x = init_x
        msg_2.pose.position.y = init_y_2
        sleep(1)

        try:
            while True:
                '''Rotary model movement'''
                msg_.pose.position.x += STEP * x_sign
                msg_.pose.position.y = (math.sqrt(abs(RADIUS**2 -
                                                      (msg_.pose.position.x - a)**2)) * y_sign) + b
                msg_.pose.position.z = 0
                msg_.pose.orientation.x = 0
                msg_.pose.orientation.y = 0
                msg_.pose.orientation.z = 0
                msg_.pose.orientation.w = 0
                msg_.twist.linear.x = 0
                msg_.twist.linear.y = 0
                msg_.twist.linear.z = 0
                msg_.twist.angular.x = 0.0
                msg_.twist.angular.y = 0
                msg_.twist.angular.z = 0
                msg_.reference_frame = 'world'

                '''Linear model movement'''
                msg_2.pose.position.x = init_x_2
                msg_2.pose.position.y += STEP * x_sign
                msg_2.pose.position.z = 0
                msg_2.pose.orientation.x = 0
                msg_2.pose.orientation.y = 0
                msg_2.pose.orientation.z = 0
                msg_2.pose.orientation.w = 0
                msg_2.twist.linear.x = 0
                msg_2.twist.linear.y = 0
                msg_2.twist.linear.z = 0
                msg_2.twist.angular.x = 0.0
                msg_2.twist.angular.y = 0
                msg_2.twist.angular.z = 0
                msg_2.reference_frame = 'world'

                res = srv_(msg_)
                srv_(msg_2)
                print(res)
                sleep(SLEEP)

                if abs(msg_.pose.position.x - a) - RADIUS >= 0:
                    x_sign *= -1
                    y_sign *= -1

        except rospy.ServiceException, e:
            print "Service call failed: %s" % e

        except KeyboardInterrupt:
            pass

        except Exception as exc:
            print(exc)


if __name__ == "__main__":
    rospy.init_node('agn_gazebo', anonymous=True)
    Animating()
    rospy.spin()
