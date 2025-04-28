import requests
import json
import os, sys
import dewiki

def search_filename(title):
    title = clean_title(title)
    
    # Check if the file already exists
    if os.path.isfile(f"{title}.wiki"):
        print(f"File {title}.wiki already exists.")
        return

def clean_title(title):
    """
    Cleans the title by removing unwanted characters and formatting.
    """
    # Remove unwanted characters and to lowercase
    title = title.lower().replace("_", " ")
    # Remove any leading or trailing underscores
    title = title.strip("_")
    return title

def get_wikipedia_page(title):
    # print(f"Fetching Wikipedia page for: {clean_title(title)}")
    print(f"Filename: {title}.wiki")

if __name__ == "__main__":
    # Check if the script is being run directly
    if len(sys.argv) == 2:
        get_wikipedia_page(sys.argv[1])
    elif len(sys.argv) > 2:
        title = " ".join(sys.argv[1:])
        get_wikipedia_page(title)
    else:
        print("Usage: python3 request_wikipedia.py <title>")