#!/usr/bin/env python

import os

def callback():
    print("Hello from python_test_script.py")
    
    print("Checking Ubuntu version")
    os.system("lsb_release -a")

    print("Done with python script")
    
if __name__ == '__main__':
    callback()