#!/bin/bash

# Demander à l'utilisateur de saisir un nombre pour commencer le compte à rebours
read -p "Entrez un nombre pour démarrer le compte à rebours :" nombre

# Vérifier si l'entrée est un nombre valide
if ! [[ $nombre =~ ^[0-9]+$ ]]; then
	echo "Erreur : Veuillez entrer un nombre entier positif."
	exit 1
fi

echo "Compte à rebours démarré :"

# Boucle while pour compter à rebours jusqu'à 0
while [ $nombre -ge 0 ]; do
	if [ $nombre -eq 0 ]; then
		echo "Le compte à rebours est terminé !"
	else
		echo "$nombre"
	fi
	nombre=$((nombre-1)) # Décrémenter le nombre à chaque itération
	sleep 1 # Attente dune seconde entre chaque nombre pour ralentir laffichage
	done
