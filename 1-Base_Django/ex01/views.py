from django.shortcuts import render

def django_page(request):
    """
    Vue pour la page de présentation de Django
    """
    return render(request, 'django.html')

def affichage_page(request):
    """
    Vue pour la page explicative du processus d'affichage
    """
    return render(request, 'affichage.html')

def templates_page(request):
    """
    Vue pour la page sur les moteurs de templates
    """
    return render(request, 'template.html')