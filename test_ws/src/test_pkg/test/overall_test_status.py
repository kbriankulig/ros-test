#!/usr/bin/env python3

# This script is meant to be called from a docker running on github Actions.
# Check to see if there were any errors reported by catkin_test_results.
#  If there were 0 errors return a succesful system exit code of 0 for git Actions. Otherwise return 1.
        
if __name__ == '__main__':
    import subprocess
    import sys
    
    # Note that "/root" is "/github/home" at the end of the system command.  Don't really understand this - kbk...
    system_command = 'source /opt/ros/noetic/setup.bash; source /root/test_ws/devel/setup.bash; catkin_test_results /github/home/.ros/test_results'
    print(system_command)
    
    result = subprocess.run([system_command], stdout=subprocess.PIPE, shell=True, executable='/bin/bash')
    print(result.stdout.decode("utf-8"))
    
    # Check if catkin_test_results contains the string "0 errors"
    if "0 errors" in result.stdout.decode("utf-8"):
        print("No errors in catkin_test_results.")
        sys.exit(0)
    else:
        print("1 or more errors in catkin_test_results.")
        sys.exit(1)
    
    