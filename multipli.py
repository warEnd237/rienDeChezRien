#!/usr/bin/python3
# -*-conding:utf-8 -*
"""module multipli contenant la fonction table"""
def table(nb, max=10):
    """fontion affichant la table de multiplication par nb de a*nb jusqu'à mas*nb"""
    i=0
    while i<max:
        print(i+1,"*", nb, "=", (i+1) * nb)
        i+=1
if __name__=="__main__":
    table(4)

