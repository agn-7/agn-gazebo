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

RADIUS = 2
STEP = .01
SLEEP = .1
MODEL_NAME = 'model1.sdf'


class Animating(object):
    def __init__(self):
        rospy.Subscriber("/gazebo/model_states", ModelStates, self.run, queue_size=1)

    def run(self, models_state):
        srv_ = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)

        try:
            index_ = models_state.name.index(MODEL_NAME)
        except:
            index_ = -1

        init_x = models_state.pose[index_].position.x
        init_y = models_state.pose[index_].position.y
        msg_ = ModelState()
        msg_.model_name = MODEL_NAME
        a = init_x - RADIUS
        b = init_y
        x_sign = -1  # Counterclockwise
        y_sign = 1
        msg_.pose.position.x = init_x
        print(a, b)
        print(init_x, init_y)
        sleep(5)

        try:
            while True:
                msg_.pose.position.x += STEP * x_sign
                msg_.pose.position.y = (math.sqrt(abs(RADIUS**2 -
                                                      (msg_.pose.position.x - a)**2)) * y_sign) + b
                msg_.pose.position.z = 1
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

                res = srv_(msg_)
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
