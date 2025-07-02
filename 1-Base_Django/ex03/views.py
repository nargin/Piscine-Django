from django.shortcuts import render

def ex03(request):
    colors = {
        'Noir': (0, 0, 0),
        'Rouge': (255, 0, 0),
        'Bleu': (0, 0, 255),
        'Vert': (0, 255, 0)
    }
    
    rows_data = []
    for i in range(50):
        row = {}
        for color_name, (r, g, b) in colors.items():
            # Intensite de 0.1 à 1.0
            intensity = 0.1 + (i / 49) * 0.9
            
            shade_r = int(r * intensity)
            shade_g = int(g * intensity)
            shade_b = int(b * intensity)
            
            # Conversion en format hexa
            hex_color = f"#{shade_r:02x}{shade_g:02x}{shade_b:02x}"
            row[color_name] = hex_color
        
        rows_data.append(row)
    
    # Template data
    context = {
        'color_names': list(colors.keys()),
        'rows_data': rows_data
    }
    
    return render(request, 'ex03.html', context)