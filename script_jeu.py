import random

def selectionner_mot():
    word_file = open("mots.txt",'r', encoding='utf8')
    word_array = word_file.readlines()
    word = random.choice(word_array)
    print(word)
    return word

def afficher_etat_mot(word):
    mot = ""
    for l in word:
        mot += l
    print(f" Voici l'état du mot a deviner : {mot}")
    return
def verifier_lettre(lettre,mot,word_state):

    bool = False
    for l in range(len(mot)):
        if mot[l] == lettre:
            bool = True
            word_state[int(l)] = lettre
    if bool == True:
        print(f" Bravo, la lettre '{lettre}' faisait parti du mot !\n")
    else:
        print(f" Mince ! la lettre '{lettre}' ne faisait parti du mot, retentez votre chance\n")
    return

def lancer_jeu(nombre_de_chance = 6):
    mot = selectionner_mot()
    word_lenght = len(mot)
    word_state = ["_"] * (word_lenght-1)

    while (nombre_de_chance > 0):
        if (nombre_de_chance == 1):
            print("Attention, il vous reste seulement un essai !")
        afficher_etat_mot(word_state)
        lettre = input(" Veuillez choisir une lettre : ")
        verifier_lettre(lettre,mot,word_state)
        nombre_de_chance -= 1

    return

lancer_jeu()