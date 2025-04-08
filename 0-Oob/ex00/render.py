import settings
import sys
import os
import re

def rendered(file_name):
    if not os.path.exists(file_name):
        print(f"File {file_name} does not exist")
        return
    with open(file_name, "r") as file:
        template = file.read()
    # Indent problems u know
    template = "\n".join("        " + line for line in template.split("\n"))
    # Handle empty and bullshit curly braces
    template = re.sub(r"\{([^}]*)\}", lambda match: str(getattr(settings, match.group(1), "")), template)
    person = f"{settings.name} {settings.surname}" if settings.name and settings.surname else "Someone"
    with open("myCV.html", "w") as file:
        file.write(f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <title>CV of {person}</title>
    </head>
    <body>
{template}
    </body>
</html>""")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].endswith(".template"):
        rendered(sys.argv[1])
    else:
        print("Usage: python render.py <template_file>")
