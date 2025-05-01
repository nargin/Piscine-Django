#!/bin/bash

set -e

if [ "$#" -gt 0 ] && [ "$1" = "clean" ]; then
    rm -rf django_venv
    exit 0
fi

if [ -d "django_venv" ]; then
    echo "Le virtualenv django_venv existe déjà. Suppression en cours..."
    rm -rf django_venv
fi

echo "Création du virtualenv django_venv..."
python3 -m venv django_venv

echo "Activation du virtualenv..."
. django_venv/bin/activate

echo "Installation des dépendances depuis requirements.txt..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Vérification de l'installation de Django..."
python3 -m django --version

echo "Installation terminée. Le virtualenv django_venv est activé."