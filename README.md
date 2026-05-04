# ROS 2 Turtle Control Project

A collection of ROS 2 Jazzy nodes for controlling turtles in turtlesim.

## Environment
- ROS 2 Jazzy
- Ubuntu 24.04
- Python 3.12

## Setup
cd ~/ros2_ws
colcon build
source install/setup.bash

## Nodes

### 1. turtle_mover
Moves turtle in a square pattern.
ros2 run my_robot turtle_mover

### 2. obstacle_avoider
Detects walls and automatically changes direction.
ros2 run my_robot obstacle_avoider

### 3. two_turtles
Controls two turtles simultaneously in opposite directions.
ros2 run turtlesim turtlesim_node
ros2 service call /spawn turtlesim/srv/Spawn "{x: 3.0, y: 3.0, theta: 0.0, name: 'turtle2'}"
ros2 run my_robot two_turtles

### 4. param_turtle
Controls turtle speed using ROS 2 parameters without modifying code.
ros2 run my_robot param_turtle
ros2 param set /param_turtle linear_speed 5.0
ros2 param set /param_turtle angular_speed 3.0

### 5. turtle_follow
turtle2 follows turtle1 automatically.
ros2 run turtlesim turtlesim_node
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2.0, y: 2.0, theta: 0.0, name: 'turtle2'}"
ros2 run my_robot turtle_follow
ros2 run turtlesim turtle_teleop_key

### 6. Launch File
Runs turtlesim and obstacle_avoider with a single command.
ros2 launch my_robot turtle_launch.py

