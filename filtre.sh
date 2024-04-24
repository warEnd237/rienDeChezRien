#!/bin/bash

# Demander à l'utilisateur de saisir un mot à rechercher
echo "saisissez un mot spécifique à rechercher dans le fichier texte :"

read word

# Utiliser grep pour filtrer les lignes contenant le mot spécifié
grep "$word" donnees.txt
