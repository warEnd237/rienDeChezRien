#!/usr/bin/python3
# -*-coding:utf-8 -*
# Ce fichier abrite le code du zcasino, un jeu de roulette adapté
from random import randrange
from math import ceil
"""on va se battre à faire un Casino à notre niveau"""
#En fait le jeu c'est la Roulette et le principe c'est de gagner lorsque le numéro choisi est le même que le numéro roulé
porte_monnai= input("Quelle est votre porte monnai : ")
attention= """

Maintenant vous devez choisir le montant à miser. Il doit être inférieur à votre porte monnai.


        """
print(attention)
montant=input ("Veuillez entrer le montant de la mise : ")
while (type(porte_monnai) or type(montant))!= int :
    try:
        porte_monnai= int(porte_monnai)
        montant= int(montant)
    except:
        print ("Vous dever saisir s'il vous plait des nombres entiers en guise de montant")
        porte_monnai= input("Quelle est votre porte monnai : ")
        montant=input ("Veuillez entrer le montant de la mise : ")
if montant > porte_monnai :
    while montant > porte_monnai :
        montant= input ("""Attention, le montant doit être inférieur au porte monnai

        veuillez saisir un autre montant : """)
        while type (montant) != int:
                try :
                    montant= int(montant)
                except :
                    montant=input ("Veuillez entrer le montant de la mise : ")
print("veuillez choisir un nombre compris entre 0 et 49")
nombre= input("Sur quelle nombre souhaitez vous poser votre mise ? Veuillez entrer ce nombre : ")

