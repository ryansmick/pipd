import unittest
import subprocess

# Base class to install some packages in the virtual env
class BaseTest(unittest.TestCase):
   
    def setUp(self):
        # Initialize commands
        pip_install_command = ["pip", "install"]
        packages = ["pygame"]

        # Install packages to virtual env
        try:
            for package in packages:
                subprocess.check_call(pip_install_command + [package])
        except subprocess.CalledProcessError:
            raise
