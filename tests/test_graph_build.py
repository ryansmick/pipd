import unittest
from base_test import BaseTest 
from utils.package_node import PackageNode

# Test the dependency graph building functionality
class TestGraphBuild(unittest.TestCase):

    # Test pip_interface.get_package_names() function
    def test_adding_dependency(self):
        # Define the two packages
        package1 = PackageNode('package1')
        package2 = PackageNode('package2')
        
        # Assertions for initial state
        self.assertTrue(not package1.dependencies, "Package1's dependencies are not empty, but should be.")
        self.assertEqual(package2.ref_count, 0)
        
        # Perform action: add dependency
        package1.add_dependency(package2)

        # Post-action assertions
        self.assertEqual(len(package1.dependencies), 1)
        self.assertIn('package2', package1.dependencies)
        self.assertEqual(package2.ref_count, 1)

if __name__ == '__main__':
    unittest.main()
