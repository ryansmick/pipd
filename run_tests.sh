#!/bin/bash

VIRTUAL_ENV_NAME="pip_test"

# Create the virtual env
echo "Creating virtual environment..."
virtualenv -p python3 $VIRTUAL_ENV_NAME > /dev/null
echo "Created virtual environment: " $VIRTUAL_ENV_NAME

# Activate the virtual env
echo "Activating virtual environment..."
source $VIRTUAL_ENV_NAME/bin/activate

# Run the tests inside the virtual env
echo "Running tests..."
python -m unittest discover -v tests

# Deactivate and remove the virtual env
echo "Cleaning up virtual environment..."
rm -rf $VIRTUAL_ENV_NAME
