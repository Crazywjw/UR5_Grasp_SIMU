# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/noetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/noetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/jerry/ros_projects/Study/ur5_robot/devel;/home/jerry/canopen/devel;/home/jerry/serial_imu_ws/devel;/home/jerry/carto/devel_isolated/cartographer_rviz;/home/jerry/carto/install_isolated;/home/jerry/xju-robot/devel;/home/jerry/robot_ws/devel;/home/jerry/xfspeech_ws/devel;/home/jerry/ws_kmdrobot/devel;/home/jerry/test/ws_kmdrobot/devel;/home/jerry/ws_myrobot/devel;/home/jerry/catkin_ws/devel;/opt/ros/noetic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python3/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/jerry/ros_projects/Study/ur5_robot/devel/env.sh')

output_filename = '/home/jerry/ros_projects/Study/ur5_robot/build/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
