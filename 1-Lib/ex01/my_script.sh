#! /bin/bash

if [ "$#" -gt 0 ] && [ "$1" = "clean" ]; then
	rm -rf local_lib
	rm -rf venv
	rm -rf install.log
	exit 0
fi

# Create and activate a virtual environment
python3 -m venv venv
. venv/bin/activate

# Create local_lib directory if it doesn't exist (or clean it if it exists)
rm -rf local_lib
mkdir -p local_lib

# Show the pip version
python3 -m pip --version

# Install path.py development version from GitHub into local_lib and save logs
python3 -m pip install --target=local_lib git+https://github.com/jaraco/path.py.git > install.log 2>&1

# Check if installation was successful
if [ $? -eq 0 ]; then
	# Execute the Python program if installation succeeded
	python3 my_program.py
fi

# Deactivate the virtual environment
deactivate

# Clean up virtual environment
rm -rf venv

