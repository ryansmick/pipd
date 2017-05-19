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

    # Test that getting dependencies for a given package functions properly
    def test_get_package_deps(self):
        expected_deps = {"six", "pyparsing"}
        deps = pip_interface.get_package_dependencies("packaging")

        self.assertEqual(deps, expected_deps)

    # Test uninstalling a given package
    def test_uninstall(self):
        package_to_uninstall = "six"
        pip_interface.uninstall(package_to_uninstall)
        self.assertTrue(package_to_uninstall not in pip_interface.get_package_names(), "{} found in packages after attempted uninstall".format(package_to_uninstall))

    # Test that uninstall raises a ValueError on incorrect input
    def test_uninstall_raises_ValueError(self):
        package_to_uninstall = "siz"
        self.assertRaises(ValueError, pip_interface.uninstall(package_to_uninstall))

    # Helper function to ensure that subset is a subset of superset
    def assertSubset(self, subset, superset):
        for package in subset:
            self.assertIn(package, superset)

if __name__ == '__main__':
    unittest.main()
