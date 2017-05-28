import unittest
from pipd.tests.base_test import BaseTest 
from pipd.utils.dep_graph import DepGraph
from pipd.utils import pip_interface

# Test the integrations between the pip_interface and the dep_graph
class TestUtilsIntegration(BaseTest):

    # Test building the graph using the currently installed pip packages
    def test_build_graph(self):
        g = DepGraph()
        g.build_graph()
        self.assertEqual(pip_interface.get_package_names(), set(g.packages.keys()))
        self.assertIn('six', g.packages['packaging'].dependencies)

if __name__ == '__main__':
    unittest.main()
