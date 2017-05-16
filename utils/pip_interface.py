# Utility file to parse various pip commands to retrieve information

import subprocess

# This function is used to parse the contents of pip freeze and return names of all installed python packages
def get_package_names():
    freeze_command = ["pip", "freeze"]
    output = subprocess.check_output(freeze_command).decode()
    installed_packages = set()
    split_output = output.split("\n")
    for line in split_output:
        name = line.split("=")[0].strip()
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
    deps_set = set(dep.strip() for dep in deps.split(","))
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

