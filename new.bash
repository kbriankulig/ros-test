#!/usr/bin/env bash

# Convenience script
# Maybe run this script first after spawning a new bash shell.
#  Usage: 
#          >> source ./new.bash

# Setup ROS env
source /opt/ros/noetic/setup.bash
source ./my_ws/devel/setup.bash

# Navigate to the test folder
cd ./my_ws/src/my_pkg/test
echo "Try: rostest my_pkg pub_sub_test.test"
