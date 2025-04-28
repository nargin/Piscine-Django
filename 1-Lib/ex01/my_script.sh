#! /bin/bash

if [ "$#" -gt 0 ] && [ "$1" = "clean" ]; then
	rm -rf local_lib
	rm -rf install.log
	rm -rf venv
	rm -rf my_folder
	exit 0
fi

python3 -m venv venv
. venv/bin/activate

rm -rf local_lib
mkdir -p local_lib

python3 -m pip --version

# Install path.py development version from GitHub into local_lib and save logs
python3 -m pip install --target=local_lib git+https://github.com/jaraco/path.py.git > install.log 2>&1

# Check if installation was successful
if [ $? -eq 0 ]; then
	python3 my_program.py
fi

# Deactivate the virtual environment
deactivate

rm -rf venv