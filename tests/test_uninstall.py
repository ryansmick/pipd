import unittest
from base_test import BaseTest 
from utils.dep_graph import DepGraph
from utils import pip_interface

# Test the dependency graph building functionality
class TestUninstall(unittest.TestCase):

    # Test uninstalling a package that is not depended on and doesn't have any dependencies
    def test_removing_top_level_package_with_no_dependencies(self):
        # Create a graph
        graph = DepGraph()
        graph.build_graph()
        
        # Assertions for initial state
        self.assertIn("termcolor", graph.packages, "Termcolor not initially installed in environment.")
        
        # Perform action: add dependency
        graph.uninstall("termcolor")

        # Post-action assertions
        self.assertTrue("termcolor" not in pip_interface.get_package_names(), "Termcolor still installed")


    # Test removing a package that isn't depended on but has dependencies
    def test_removing_top_level_package_with_dependencies(self):
        # Create a graph
        graph = DepGraph()
        graph.build_graph()

        # Assertions for initial state
        self.assertIn("packaging", graph.packages, "Packaging package not initially installed in environment")
        self.assertIn("pyparsing", graph.packages, "Pyparsing package not initially installed in environment")
        self.assertIn("six", graph.packages, "Six package not initially installed in environment")

        # Perform uninstall
        graph.uninstall("packaging")

        # Post-action assertions
        self.assertTrue("packaging" not in pip_interface.get_package_names(), "Packaging still installed")
        self.assertTrue("pyparsing" not in pip_interface.get_package_names(), "Pyparsing still installed")
        self.assertTrue("six" not in pip_interface.get_package_names(), "Six still installed")

    # Test removing a nonexistent package raises a ValueError
    def test_removing_bad_package_raises_ValueError(self):
        # Create a graph
        graph = DepGraph()
        graph.build_graph()

        with self.assertRaises(ValueError):
            graph.uninstall("packing")
        
if __name__ == '__main__':
    unittest.main()
