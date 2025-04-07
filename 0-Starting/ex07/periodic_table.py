import sys

def parse_element(line):
    name, properties = line.strip().split(' = ')
    props = {}
    props['name'] = name
    for prop in properties.split(', '):
        key, value = prop.split(':')
        props[key] = value
    return props

def create_css():
    return """
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        td {
            border: 1px solid black;
            padding: 10px;
            width: 5.5%;
            text-align: center;
        }
        .empty {
            border: none;
        }
        h4 {
            margin: 4px 0;
        }
        ul {
            list-style-type: none;
            padding: 0;
            margin: 4px 0;
            font-size: 12px;
            text-align: left;
        }
    </style>
    """

def create_element_cell(element):
    return f"""
    <td>
        <h4>{element['name']}</h4>
        <ul>
            <li>No {element['number']}</li>
            <li>{element['small']}</li>
            <li>{element['molar']}</li>
            <li>{element['electron'].replace(' ', ' ')} electron</li>
        </ul>
    </td>
    """

def create_empty_cell():
    return '<td class="empty"></td>'

def generate_periodic_table(elements):
    # Create a 2D grid (7 rows x 18 columns) for the main table
    grid = [[None for _ in range(18)] for _ in range(7)]
    
    # Place elements in the grid based on their position
    for element in elements:
        pos = int(element['position'])
        if pos < 18:  # Only place elements in positions 0-17
            row = 0
            # Determine row based on atomic number
            if int(element['number']) <= 2:
                row = 0
            elif int(element['number']) <= 10:
                row = 1
            elif int(element['number']) <= 18:
                row = 2
            elif int(element['number']) <= 36:
                row = 3
            elif int(element['number']) <= 54:
                row = 4
            elif int(element['number']) <= 86:
                row = 5
            else:
                row = 6
            grid[row][pos] = element

    # Generate HTML with added language attribute and title
    html = [
        '<!DOCTYPE html>', 
        '<html lang="en">', 
        '<head>', 
        '<meta charset="UTF-8">', 
        '<title>Periodic Table</title>',
        create_css(), 
        '</head>', 
        '<body>', 
        '<table>'
    ]
    
    # Generate table rows
    for row in grid:
        html.append('<tr>')
        for element in row:
            if element:
                html.append(create_element_cell(element))
            else:
                html.append(create_empty_cell())
        html.append('</tr>')
    
    html.extend(['</table>', '</body>', '</html>'])
    return '\n'.join(html)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python periodic_table.py <file>")
        sys.exit(1)

    elements = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            elements.append(parse_element(line))
    
    # Generate and save HTML file
    html_content = generate_periodic_table(elements)
    with open('periodic_table.html', 'w') as f:
        f.write(html_content)
