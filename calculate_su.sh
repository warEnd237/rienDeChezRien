#!/bin/bash

#Fonction pour vérifier si une valeur est un entier
is_integer() {
	if [[ $1 =~ ^-?[0-9]+$ ]];
	then
		return 0
	else
		return 1
	fi
}

# Vérifier si des arguments ont été fournis
if [ $# -eq 0 ];
then
	echo "Erreur : Aucun nombre fourni."
	exit 1
fi

# Initiliser la somme
Sum=0

# Parcourir les arguments fournis
for num in "$@";
do
	# Vérifier si l'argument est un entier
	if ! is_integer "$num";
	then
		echo "Erreur : '$num' n'est pas un nombre entier valide."
		exit 1
	fi

	# Ajouter le nombre à la somme
	((sum += num))
done

# Afficher la somme
echo "La somme des nombres est : $sum"
