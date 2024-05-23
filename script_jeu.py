# JEU DU PENDU

import random
import os
from unicodedata import normalize

def selectionner_mot():             # Fonction de sélection dun mot soit dans un fichier externe ou un fichier par défault

    external_file = input("\nSi vous souhaitez utiliser un fichier de mot externe, ajoutez le au dossier du projet et spécifiez son nom, sinon appuyez sur 'entrer' :\n ")
    chemin_complet = os.path.join(os.path.abspath(os.path.curdir), external_file)   # Détermination du chemin complet jusqu'au fichier externe
    if os.path.isfile(chemin_complet):       # Vérification de l'existance du fichier
        word_file = open(chemin_complet,'r', encoding='utf8')
        word_array = word_file.read().splitlines()
        word = random.choice(word_array)
        word = normalize('NFD',word).encode('ASCII','ignore').decode('utf8')
    else:
        word_file = open("mots.txt",'r', encoding='utf8')
        word_array = word_file.read().splitlines()
        word = random.choice(word_array)
        word = normalize('NFD',word).encode('ASCII','ignore').decode('utf8')
    return word

def afficher_etat_mot(word):  # Fonction affichant l'état d'un mot
    mot = ""
    for l in word:            # On boucle sur chaque lettre du mot pour afficher les lettres trouvées
        mot += l
    print(f" Voici l'état du mot a deviner : {mot}")
    return mot
def verifier_lettre(lettre,mot,word_state,nombre_de_chances):  # Fonction vérifiant la lettre entrée

    bool = False
    for l in range(len(mot)):  # On boucle sur chaque lettre du mot pour vérifier si la lettre entrée est correcte
        if mot[l] == lettre:
            bool = True
            word_state[int(l)] = lettre
    if bool == True:
        print(f"\n Bravo, la lettre '{lettre}' faisait parti du mot !\n")
    else:
        print(f"\n Mince ! la lettre '{lettre}' ne faisait parti du mot, retentez votre chance\n")
        nombre_de_chances -= 1
    return nombre_de_chances

def lancer_jeu(nombre_de_chance = 6):   # Menu
    mot = selectionner_mot()
    word_lenght = len(mot)
    word_state = ["_"] * (word_lenght)
    print(" C'est parti ! ")
    while (nombre_de_chance >= 0):
        if (nombre_de_chance == 1):         # Conditions gérant le nombre de chance restante
            print(" Attention, il vous reste seulement un essai !")
        elif (nombre_de_chance == 0):
            relancer = input(f" \nGame over !! Le mot a trouver était : {mot}. Appuyer sur entrer pour relancer une partie")
            lancer_jeu()
        etat = afficher_etat_mot(word_state)
        if (etat == mot):
            relancer = input(f" \nBravo !! Vous avez gagnez ! Appuyer sur entrer pour relancer une partie \n")
            lancer_jeu()
        lettre = input(" Veuillez choisir une lettre : ")
        nombre_de_chance = verifier_lettre(lettre,mot,word_state,nombre_de_chance)

    return

lancer_jeu()