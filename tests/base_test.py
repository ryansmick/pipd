import unittest
import subprocess
import time

# Base class to install some packages in the virtual env
class BaseTest(unittest.TestCase):

    base_packages = {"six", "packaging", "pyparsing", "appdirs"}
    packages_to_install = {"pygame"}
    installed_packages = base_packages | packages_to_install

    def setUp(self):
        # Initialize commands
        pip_install_command = ["pip", "install"]

        # Install packages to virtual env
        try:
            for package in BaseTest.packages_to_install:
                subprocess.check_call(pip_install_command + [package], stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            raise
