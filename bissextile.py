#!/usr/bin/python3
# -*-coding:utf-8 -*
annee = input("saisissez une année : ")
while type(annee)!=int :
    try:
        annee= int(annee)
    except:
        print("Erreur lors de la convertion de l'année. Entrez s'il vous plait un nombre entier")
        annee = input("saisissez une année : ") #là on éssaye de lever l'exception
if annee %400==0 or (annee %4==0 and annee%100!=0):
 print ("l'année saisie est bissextile.")
else:
 print ("l'année saisie n'est pas bissextile.")
