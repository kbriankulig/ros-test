#!/usr/bin/env python3
#
# This file contains unit tests for source code in listener.py
#

PKG = 'my_pkg'
NAME = 'unit_test_listener'

import unittest

class TestListener(unittest.TestCase):
    def __init__(self, *args):
        super(TestListener, self).__init__(*args)

    def test_listen(self):
        """ listen() should return in 2 seconds without causing any python exceptions. """
        l.listen(wait_time=20)
        self.assertTrue(True)

    def test_callback(self):
        """ This callback should accept the input parameter and not cause a python exception. """
        class UTClass():
            def __init__(self):
                self.data = "test message string"
        data = UTClass()
        l.callback(data)
        self.assertTrue(True)

        
if __name__ == '__main__':
    import rosunit
    import sys
    sys.path.append("..")  # Include all the python packages/folders in the root of the catkin package
    
    from scripts import listener as l   
    
    rosunit.unitrun(PKG, NAME, TestListener, sys.argv)