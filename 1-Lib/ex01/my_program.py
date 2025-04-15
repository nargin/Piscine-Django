import sys
import os

# Add local_lib to Python path
sys.path.append(os.path.abspath("local_lib"))

# Now we can import path from our local installation
from path import Path

# Simple demonstration of path.py usage
def main():
	print(Path.home())

if __name__ == "__main__":
    main()
