from django.shortcuts import render

def markdown_cheatsheet(request):
    """
    Vue qui affiche la page Markdown Cheatsheet
    """
    return render(request, 'index.html')