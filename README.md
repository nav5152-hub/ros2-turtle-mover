# ROS 2 Turtle Mover

A ROS 2 Jazzy node that controls a turtle to move in a circle automatically.

## Requirements
- ROS 2 Jazzy
- Ubuntu 24.04

## How to Run

1. Build the package:
colon build
source install/setup.bash

2. Run turtlesim:
ros2 run turtlesim turtlesim_node

3. Run turtle mover:
ros2 run my_robot turtle_mover

## Result
The turtle moves in a circle automatically using a ROS 2 publisher node.
