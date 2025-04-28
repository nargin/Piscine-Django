import time
import sys
import os

# Add local_lib to Python path
sys.path.append(os.path.abspath("local_lib"))

# Now we can import path from our local installation
from path import Path

# Simple demonstration of path.py usage
def main():
    folder = Path("my_folder")
    if not folder.exists():
        folder.mkdir()

    file = folder / "my_file.txt"
    file.touch()

    with file.open("w") as f:
        f.write(time.ctime())

    with file.open("r") as f:
        content = f.read()
        print(content)

    print(Path.home())
    # Print my_folder path
    print(folder.absolute())

if __name__ == "__main__":
    main()
