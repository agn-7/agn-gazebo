

### Versiones compatibles:
 - *ROS: Kinetic*
 - *Sistema Operativo: Ubuntu-16.04*
 - *Gazebo 7.0*

# Dependencias:
 - [Simulador Velodyne](https://github.com/agn-7/modified_velodyne_simulator)
 - ```sudo apt-get install ros-kinetic-husky-gazebo```
 - [Elementos de Arenas Hector NIST](https://github.com/tu-darmstadt-ros-pkg/hector_nist_arenas_gazebo)

---
# Instalación:
Clona este proyecto en tu espacio de trabajo (workspace) de ROS y luego ejecuta el siguiente comando:

```~/catkin_ws$ catkin_make```

---

## Modelo de Gazebo para LiDAR de personas
Un modelo de Gazebo con el fin de [detección de personas](https://github.com/agn-7/hdl_people_tracking) en un entorno exterior utilizando un LiDAR 3D Velodyne compatible con ROS.

### Uso:
Ejecuta sus archivos de lanzamiento (launch):

 - **Personas fijas**:
    ```
    roslaunch agn_gazebo static_velodyne.launch
    ```

 - **Personas animadas**:
    ```
    roslaunch agn_gazebo animated_person.launch
    roslaunch agn_gazebo movement.launch
    ```
    
 - Para guardar la posición de las personas en archivos .csv, ejecuta el siguiente comando:
    ```
    roslaunch agn_gazebo groundtruth.launch
    ```   
Gazebo:
![default_gzclient_camera(1)-2019-05-23T15_06_12 310211](https://user-images.githubusercontent.com/14202344/58246505-7dade880-7d6c-11e9-8482-28f42baeb138.jpg "Person and LiDAR")

Rviz:
![RVIZ-MARKER](https://user-images.githubusercontent.com/14202344/58627451-911cfe80-82ec-11e9-8270-592f09e5c37a.png "Animated person and LiDAR") 
---

## Modelo de Gazebo para Pioneer P3DX
Un modelo de Gazebo con el fin de aplicar algoritmos de [seguimiento de paredes]() y go-to, como el algoritmo de navegación [Bug](https://github.com/agn-7/bugs) 

### Uso:
Ejecuta su archivo de lanzamiento (launch):

```
roslaunch agn_gazebo pioneer.launch
```
![default_gzclient_camera(1)-2019-05-30T15_22_49 379103](https://user-images.githubusercontent.com/14202344/58628547-3638d680-82ef-11e9-91a0-3ee7d6ac8893.jpg "Ready to wall following or goto x,y scenario")

---

## Modelo de Gazebo para exploración de robot de rescate
Un modelo de Gazebo para preparar un entorno para un robot de rescate en una tarea de [Exploración]() en un mapa de laberinto con rampas. 

### Uso:
Ejecuta su archivo de lanzamiento (launch):

```
roslaunch agn_gazebo rescue.launch
```

![default_gzclient_camera(1)-2019-09-09T13_59_48 114326](https://user-images.githubusercontent.com/14202344/64522067-6f311000-d30e-11e9-8a6e-b416ad28bdd3.jpg "Rescue robot in maze map")

---
