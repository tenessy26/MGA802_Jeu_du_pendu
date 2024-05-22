import random
import os
from unicodedata import normalize

def selectionner_mot():

    external_file = input(" Quel est le nom du fichier ? ")
    chemin_complet = os.path.join(os.path.abspath(os.path.curdir), external_file)
    print(chemin_complet)

    print(os.path.isfile(chemin_complet))
    if os.path.isfile(chemin_complet):
        word_file = open("mots.txt",'r', encoding='utf8')
        word_array = word_file.readlines()
        word = random.choice(word_array)
        word = word[:-1]
        word = normalize('NFD',word).encode('ASCII','ignore').decode('utf8')
    else:
        word_file = open("mots.txt",'r', encoding='utf8')
        word_array = word_file.readlines()
        word = random.choice(word_array)
        word = word[:-1]
        word = normalize('NFD',word).encode('ASCII','ignore').decode('utf8')
        print(word)
    return word

def afficher_etat_mot(word):
    mot = ""
    for l in word:
        mot += l
    print(f" Voici l'état du mot a deviner : {mot}")
    return mot
def verifier_lettre(lettre,mot,word_state,nombre_de_chances):

    bool = False
    for l in range(len(mot)):
        if mot[l] == lettre:
            bool = True
            word_state[int(l)] = lettre
    if bool == True:
        print(f" Bravo, la lettre '{lettre}' faisait parti du mot !\n")
    else:
        print(f" Mince ! la lettre '{lettre}' ne faisait parti du mot, retentez votre chance\n")
        nombre_de_chances -= 1
    return nombre_de_chances

def lancer_jeu(nombre_de_chance = 6):
    mot = selectionner_mot()
    word_lenght = len(mot)
    word_state = ["_"] * (word_lenght)
    print(" C'est parti ! ")
    while (nombre_de_chance >= 0):
        if (nombre_de_chance == 1):
            print(" Attention, il vous reste seulement un essai !")
        elif (nombre_de_chance == 0):
            relancer = input(f" Game over !! Le mot a trouver était : {mot} Appuyer sur entrer pour relancer une partie")
            lancer_jeu()
        etat = afficher_etat_mot(word_state)
        if (etat == mot):
            relancer = input(f" Bravo !! Vous avez gagnez ! \n Appuyer sur entrer pour relancer une partie \n")
            lancer_jeu()
        lettre = input(" Veuillez choisir une lettre : ")
        nombre_de_chance = verifier_lettre(lettre,mot,word_state,nombre_de_chance)

    return

lancer_jeu()