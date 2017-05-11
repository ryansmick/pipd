# Utility file to parse various pip commands to retrieve information

import subprocess
import pip

# This function is used to parse the contents of pip freeze and return names of all installed python packages
def get_package_names():
    installed_packages = [package.project_name for package in pip.get_installed_distributions()]
    return installed_packages

# Take a package name as an argument and return all python packages that it depends on
def get_package_dependencies(package_name):
    try:
        # Obtain package requirements as a string
        deps = get_package_details(package_name)['Requires']
    except KeyError:
        return []

    # Return dependencies in list form
    deps_list = [dep.strip() for dep in deps.split(",")]
    return deps_list

# Function to retrieve all details about the given package and return them as a dictionary
# Package must be installed in order to function correctly
def get_package_details(package_name):
    try:
        # Call pip show on the package
        output = subprocess.check_output(["pip", "show", package_name])
    except subprocess.CalledProcessError:
        return {}
    
    details = {}

    split_output = output.decode().strip().split("\n")
    # Add package info to details dict
    for line in split_output:
        split_line = line.split(":", 1)
        details[split_line[0].strip()] = split_line[1].strip()

    return details

