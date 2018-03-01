# Contains a class PackageNode that represents a given pip package in the dependency graph
from pipd.utils import pip_interface 

# Class to represent a node in the dependency graph containing information about a given pip package
class PackageNode:
    def __init__(self, package_name):
        self.name = package_name
        self.ref_count = 0 # Number of packages that depend on this package
        self.dependencies = {}

    # Add the given package node as a dependency for the current node
    def add_dependency(self, package_node):
        self.dependencies[package_node.name] = package_node
        package_node.ref_count += 1

    # Uninstalls a given package and all it's dependencies that aren't requirements for other packages
    def uninstall(self):
        # Only uninstall the package if no other packages depend on it
        if self.ref_count <= 1:
            # Recursively uninstall each child package
            for package_name, package in self.dependencies.items():
                package.uninstall()

            # Uninstall the package
            pip_interface.uninstall(self.name)

