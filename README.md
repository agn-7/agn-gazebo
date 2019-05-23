# Dependencies:
 - [Velodyne Simulator](https://github.com/agn-7/modified_velodyne_simulator)

---
# Install:
Clone this project on your ROS workspace, then run the command below:

```~/catkin_ws$ catkin_make```

---

## Person LiDAR Gazebo model
A Gazebo model in order to [person detection](https://github.com/agn-7/hdl_people_tracking) purpose in an outdoor location using 3D LiDAR Velodyne which is 
compatible to ROS.

### Usage:
Launch its launch file:

```
roslaunch agn_gazebo static_velodyne.launch
```

![](url "Person and LiDAR")

---

## Pioneer P3DX Gazebo model
A Gazebo model in order to wall following and go-to algorithms purpose like the [Bug](https://github.com/agn-7/bugs) navigation algorithm 

### Usage:
Launch its launch file:

```
roslaunch agn_gazebo gazebo.launch
```
![default_gzclient_camera(1)-2019-05-23T15_06_12 310211](https://user-images.githubusercontent.com/14202344/58246505-7dade880-7d6c-11e9-8482-28f42baeb138.jpg "Person and LiDAR")


---

## Rescue robot exploration Gazebo model
A Gazebo model in order to prepare an environmental for a rescue robot on [Exploration]() task in a ramped maze map. 

### Usage:
Launch its launch file:

```
roslaunch agn_gazebo rescue.launch
```

![](url "Person and LiDAR")

---