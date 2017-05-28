#!/bin/bash

VIRTUAL_ENV_NAME="pip_test"

# Create the virtual env
echo "Creating virtual environment..."
virtualenv -p python3 $VIRTUAL_ENV_NAME > /dev/null
echo "Created virtual environment: " $VIRTUAL_ENV_NAME

# Activate the virtual env
echo "Activating virtual environment..."
source $VIRTUAL_ENV_NAME/bin/activate

# Install the requirements to run the tests in the virtual env
echo "Installing dependencies for tests..."
pip install -r requirements.txt > /dev/null

# Run the tests inside the virtual env and store exit status
echo "Running tests..."
python -m unittest discover -v pipd/tests
EXIT_STATUS=$?

# Deactivate and remove the virtual env
echo "Cleaning up virtual environment..."
rm -rf $VIRTUAL_ENV_NAME

#Exit with the exit status of the tests
exit $EXIT_STATUS
