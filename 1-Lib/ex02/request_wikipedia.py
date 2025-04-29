import requests
import json
import os
import sys
import dewiki

def clear_wiki_files(title=None):
    if title:
        os.remove(title)
        return

    count = 0
    files = []
    for filename in os.listdir("."):
        if filename.endswith(".wiki"):
            try:
                os.remove(filename)
                count += 1
                files.append(filename)
            except Exception as e:
                print(f"Error removing {filename}: {e}")
    
    if count > 0:
        print("No .wiki files found")
        return

    print(f"Removed {count}: {', '.join(files)}")

def clean_title(title) -> str:
    title = title.lower().replace("_", " ")
    return title.strip()

def search_filename(title):
    clean_title_str = clean_title(title)
    filename = f"{clean_title_str}.wiki"
    
    if os.path.isfile(filename):
        print(f"File {filename} already exists.")
        return True
    return False

def get_wikipedia_page(title, lang="en"):
    clean_title_str = clean_title(title)
    filename = f"{clean_title_str}.wiki"
    
    if search_filename(clean_title_str):
        clear_wiki_files(clean_title_str)
        
    
    api_url = f"https://{lang}.wikipedia.org/w/api.php"
    
    search_params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": title,
        "srqiprofile": "engine_autoselect",
        "srlimit": 1,
    }
    
    try:
        search_response = requests.get(api_url, params=search_params)
        search_response.raise_for_status()
        search_data = search_response.json()

        # print(json.dumps(search_data, indent=4))

        pageid = search_data["query"]["search"][0]["pageid"]

        page_params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "explaintext": True ,
            "pageids": pageid,
        }

        page_response = requests.get(api_url, params=page_params)
        page_response.raise_for_status()
        page_data = page_response.json()

        # print(json.dumps(page_data, indent=4))

        content = page_data["query"]["pages"][str(pageid)]["extract"]
        content = dewiki.from_string(content)

        with open(filename, "w") as file:
            file.write(content)
        
        print(f"Page content saved to {filename}")

    except requests.RequestException as e:
        print(f"Error fetching search results: {e}")
        return

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1].lower() == "clean":
            clear_wiki_files()
        elif sys.argv[1].lower() == "fr":
            get_wikipedia_page(sys.argv[1], lang="fr")
        else:
            get_wikipedia_page(sys.argv[1])
    elif len(sys.argv) > 2:
        title = " ".join(sys.argv[1:])
        get_wikipedia_page(title)
    else:
        print("Usage: python3 request_wikipedia.py <title>")
        print("       python3 request_wikipedia.py clean (to remove all .wiki files)")