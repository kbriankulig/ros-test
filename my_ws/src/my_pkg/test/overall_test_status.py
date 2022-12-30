#!/usr/bin/env python3

# This script is meant to be called from github Actions.
# This script runs catkin_test_results on the output to decide if the corresponding github Action should be failed.
# If catkin_test_results contain the string "0 errors", return a succesful system exit code of 0 to git Actions,
# otherwise return 1.to fail the git Action.
        
if __name__ == '__main__':
    import subprocess
    import sys
    
    # Build a shell command to send to a bash shell subprocess
    system_command = 'source /opt/ros/noetic/setup.bash; '
    system_command += 'source /root/test_ws/devel/setup.bash; '
    system_command += 'catkin_test_results /github/home/.ros/test_results'
    print(system_command)
    
    
    # Run shell command
    result = subprocess.run([system_command], stdout=subprocess.PIPE, shell=True, executable='/bin/bash')
    print(result.stdout.decode("utf-8"))
    
    # Check if catkin_test_results contains the string "0 errors"
    if "0 errors" in result.stdout.decode("utf-8"):
        print("No errors reported with catkin_test_results.")
        sys.exit(0)
    else:
        print("1 or more errors reported with catkin_test_results.")
        sys.exit(1)
    
    