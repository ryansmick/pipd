# Contains a class DepGraph that represents a pip dependency graph
from . import pip_interface
from termcolor import colored
from .package_node import PackageNode

# Class to represent the pip dependency graph
class DepGraph:
    # Initialize a dictionary of package names to DepNodePGraph objects
    def __init__(self):
        self.packages = {} # Map from package name to PackageNode object

    # Function to build the dependency graph
    def build_graph(self):
        # Reset the packages
        self.packages = {}

        # Create a nwe node in self.packages for each pip package
        for package_name in pip_interface.get_package_names():
            self.packages[package_name] = PackageNode(package_name)

        # Add dependencies for each pip package
        for package_name, package in self.packages.items():
            for dep_name in pip_interface.get_package_dependencies(package_name):
                try:
                    package.add_dependency(self.packages[dep_name])
                except KeyError:
                    # If dependency isn't in self.packages, package either isn't installed and we will not worry about it
                    # Or package is a default pip package that doesn't appear in pip freeze, and we won't worry about it
                    pass

    # Function to print a graph representation of the given dependency graph
    def print_graph(self):
        marked = set()
        for package_name, package in self.packages.items():
            self.print_graph_from_node(package, marked, 0)

    # Recursive helper function to print graph starting at a given node
    def print_graph_from_node(self, package_node, marked, tabs=0):
        tab_string = '    ' * tabs

        # Base case: if package is already in marked, print the name of the package and return
        if package_node in marked:
            if tabs:
                print(colored(tab_string + package_node.name, 'red'))

            return

        # Recursive step: Print node and then recurse on children
        print(tab_string + package_node.name)
        marked.add(package_node)

        for child_name, child_node in package_node.dependencies.items():
            self.print_graph_from_node(child_node, marked, tabs=tabs+1)

    # Function to uninstall a given package and all it's dependencies
    def uninstall(self, package_name):
        if package_name not in self.packages:
            raise ValueError("Package {} not found.".format(package_name))

        package = self.packages[package_name]

        # If package is being depended upon, prompt user for uninstall
        if package.ref_count != 0:
            answer = input("{} is a dependency for another installed package. Are you sure you want to remove it? Y/n: ".format(package_name))
            if lower(answer) not in ["y", "yes"]:
                print("Aborting...")
                return

        # Recursively uninstall the package
        package.uninstall()
