# Utility file to parse various pip commands to retrieve information

import subprocess
import re

# This function is used to parse the contents of pip freeze and return names of all installed python packages
def get_package_names():
    freeze_command = ["pip", "list"]
    output = subprocess.check_output(freeze_command, stderr=subprocess.DEVNULL).decode()
    installed_packages = set()
    split_output = output.split("\n")
    for line in split_output:
        name = re.split("[ \t]", line)[0].strip()
        if name:
            installed_packages.add(name)
    return installed_packages

# Take a package name as an argument and return all python packages that it depends on
# Raises ValueError if package not installed
def get_package_dependencies(package_name):
    try:
        # Obtain package requirements as a string
        deps = get_package_details(package_name)['Requires']
    except KeyError:
        raise ValueError("Invalid package name: " + package_name)
    except ValueError:
        raise

    # Return dependencies in list form
    deps_set = set(dep.strip() for dep in deps.split(",") if dep.strip() != '')
    return deps_set

# Function to retrieve all details about the given package and return them as a dictionary
# Package must be installed, otherwise will raise ValueError
def get_package_details(package_name):
    try:
        # Call pip show on the package
        output = subprocess.check_output(["pip", "show", package_name])
    except subprocess.CalledProcessError:
        raise ValueError("Invalid package name: " + package_name)
    
    details = {}

    split_output = output.decode().strip().split("\n")
    # Add package info to details dict
    for line in split_output:
        split_line = line.split(":", 1)
        details[split_line[0].strip()] = split_line[1].strip()

    return details

# Function to uninstall a given package from pip
def uninstall(package_name):
    try:
        # Call pip uninstall on the package
        uninstall_command = ["pip", "uninstall", package_name]
        ps = subprocess.Popen(("echo", "y"), stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        subprocess.check_call(uninstall_command, stdin=ps.stdout, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        #ps.wait()
        ps.wait()
    except subprocess.CalledProcessError:
        raise ValueError("Invalid package name: " + package_name)
