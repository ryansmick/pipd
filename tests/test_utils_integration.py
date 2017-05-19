import unittest
from base_test import BaseTest 
from utils.dep_graph import DepGraph

# Test the integrations between the pip_interface and the dep_graph
class TestUtilsIntegration(BaseTest):

    # Test building the graph using the currently installed pip packages
    def test_build_graph(self):
        g = DepGraph()
        g.build_graph()
        self.assertEqual(self.installed_packages, g.packages.keys())
        self.assertIn('six', g.packages['packaging'].dependencies)

if __name__ == '__main__':
    unittest.main()
