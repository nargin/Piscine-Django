from django.shortcuts import render
from django.conf import settings
from datetime import datetime
import os
from .forms import TextInputForm

def input_history_view(request):
    form = TextInputForm()
    history = []
    
    # Lire l'historique existant du fichier de logs s'il existe
    if os.path.exists(settings.EX02_LOG_FILE):
        with open(settings.EX02_LOG_FILE, 'r') as log_file:
            history = log_file.readlines()
    
    # Si le formulaire est soumis
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            # Récupérer l'entrée de l'utilisateur
            user_input = form.cleaned_data['text_input']
            
            # Générer l'horodatage
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Créer l'entrée formatée
            log_entry = f"[{timestamp}] {user_input}\n"
            
            # Ajouter l'entrée au fichier de logs
            os.makedirs(os.path.dirname(settings.EX02_LOG_FILE), exist_ok=True)
            with open(settings.EX02_LOG_FILE, 'a+') as log_file:
                log_file.write(log_entry)
            
            # Ajouter l'entrée à l'historique pour l'affichage
            history.append(log_entry)
            
            # Réinitialiser le formulaire
            form = TextInputForm()
    
    # Passer le contexte au template
    context = {
        'form': form,
        'history': history,
    }
    
    return render(request, 'input_history.html', context)