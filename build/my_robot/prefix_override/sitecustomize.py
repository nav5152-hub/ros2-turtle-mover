import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/yunseo/ros2_ws/src/my_robot/install/my_robot'
