import unittest
from utils import pip_interface
from base_test import BaseTest 
import subprocess

# Test the utilities defined in pip_interface.py
class TestPipInterface(BaseTest):

    # Test pip_interface.get_package_names() function
    def test_get_package_names(self):
        packages = pip_interface.get_package_names()
        self.assertSubset(self.installed_packages, packages)

    def test_get_package_deps(self):
        expected_deps = {"six", "pyparsing"}
        deps = pip_interface.get_package_dependencies("packaging")

        self.assertEqual(deps, expected_deps)

    # Helper function to ensure that subset is a subset of superset
    def assertSubset(self, subset, superset):
        for package in subset:
            self.assertIn(package, superset)

if __name__ == '__main__':
    unittest.main()
