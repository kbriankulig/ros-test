#!/usr/bin/env python3

import os

def check_version_info():
    print("Hello from list_sw_version_info.py")
    
    print("Checking Ubuntu version")
    os.system("lsb_release -a")
    os.system("docker -v")

    print("Done with python script")
    
if __name__ == '__main__':
    check_version_info()