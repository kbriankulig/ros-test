#!/usr/bin/env bash

# This script sets up the ROS container for development.
# This script is meant to be run once after the container is created and the source repo has been copied
#   over or mounted to the container in /root/my_ws. 

# Setup ROS env
chmod +x /opt/ros/noetic/setup.bash
source /opt/ros/noetic/setup.bash

# Initialize/create the catkin build and devel folders
mv ./my_ws/src ./my_ws/src_ignore
mkdir -p ./my_ws/src
rm -rf ./my_ws/build
rm -rf ./my_ws/devel
cd ./my_ws
catkin_make
cd ..
rm -rf ./my_ws/src
mv ./my_ws/src_ignore ./my_ws/src

# Setup ROS env
chmod +x ./my_ws/devel/setup.bash
source ./my_ws/devel/setup.bash

echo "Try: source new.bash"