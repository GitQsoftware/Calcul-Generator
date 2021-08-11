#!/usr/bin/env python3
from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror, askyesno
import math 
from random import randint
import pygame 
import sys
import os

#fenêtre 
root = Tk()
root.title("Générateur de calcul | 1.0 | Gratuit ")
root.geometry('240x340')
root.config(bg='#FF7D68')
try:
    root.iconbitmap('icon.ico')
except:
    img = PhotoImage(file='icon.png')
    root.iconphoto(True, img)

#musique !
pygame.mixer.init()
pygame.mixer.music.load("tic_tac.ogg")
while pygame.mixer.get_busy():
    pass
pygame.mixer.music.play(10,0.0)
























"""
*********************************************************************************
*********************************************************************************

Mise en place de l'interface mais sans le contenu

*********************************************************************************
*********************************************************************************
"""

# une frame juste pour aligner horizontalement
frame = Frame(root, bg='#FF7D68')
frame.pack(side=TOP, pady=10)

# un label pour afficher la question
questionLabel = Label(
    frame, text='', bg='#FF7D68', font=('Book Antiqua', 20))
questionLabel.pack(side=LEFT, padx=10)

# le champ d'entrée pour mettre le résultat
resultEntry = Entry(frame, font=("Comic", 20))
resultEntry.pack(side=LEFT, padx=10)

# Bouton pour vérifier le résultat
verifResultButton = Button(root, text="verifier", bg='#FF7D68', font=('Book Antiqua', 20))
verifResultButton.pack(pady=10)

# un label pour afficher le score
scoreLabel = Label(root, text='', bg='#FF7D68', font=('Book Antiqua', 20))
scoreLabel.pack(side=BOTTOM)

















"""
*********************************************************************************
*********************************************************************************

Les variables globales dont le programme aura besoin

*********************************************************************************
*********************************************************************************
"""

minVal = 2
maxVal = 10
firstNumber = 0
secondNumber = 0
calculText = ''
correctResult = 0
score = 0
nb_questions = 0

























"""
*********************************************************************************
*********************************************************************************

Les fonctions

*********************************************************************************
*********************************************************************************
"""

def newValues():
    """
    calcule de nouvelles valeurs pour une nouvelle question
    """
    global firstNumber, secondNumber, calculText, correctResult

    firstNumber = randint(minVal, maxVal)
    secondNumber = randint(minVal, maxVal)

    test = randint(1, 4)
    print('1 = +, 2 = -, 3 = * (x = fois), 4 = / (division)')
    print('chiffre du calcul : ' + str(test))
    if test == 1:
        calculText = "+"
        correctResult = firstNumber + secondNumber
    elif test == 2:
        calculText = "-"
        correctResult = firstNumber - secondNumber
    elif test == 3:
        calculText = "x"
        correctResult = firstNumber * secondNumber
    elif test == 4:
        calculText = ":"
        # on intervertit le résultat et le premier nombre
        # pour avoir des entiers
        correctResult = firstNumber
        pivot = firstNumber * secondNumber
        firstNumber = pivot
    resultEntry.delete(0, END)

def updateUI():
    """
    met à jour l'interface du jeu
    """
    question = '{0} {1} {2} = '.format(firstNumber, calculText, secondNumber)
    questionLabel.config(text=question)
    scoreLabel.config(text='Score : {0}'.format(score))

#Vérification du résultat :
#raccourci clavier :
def verif_result2(event):
    do('verif_result')

def verif_result():
    do('verif_result')

"""
*********************************************************************************
*********************************************************************************

La fonction qui gère tout en fonction de l'état du jeu

*********************************************************************************
*********************************************************************************
"""

def do(state='init'):
    global score, nb_questions
    if state == 'init':
        nb_questions = 5
        score = 10
        newValues()
        updateUI()
    elif state == 'verif_result':
        userResult = resultEntry.get()
        try:
            userResult = int(resultEntry.get())
            if correctResult == userResult:
                showinfo('Bravo !', "Tu as réussi tu es le meilleur ! Tu augmentes ton score.")
                nb_questions -=1
                score += 1
                print(score)
                if nb_questions > 0 :
                    newValues()
            else:
                showerror('Raté !', "Révise tes leçons")
                score -= 1
                newValues()
                print(score)
                
        except:
            showwarning('Caractère Incorect', 'Seul les chiffres sont autoriser !')
            score -= 1
            print(score)
        updateUI()

        if nb_questions<1:
            do('nb_questions')
    elif state =='nb_questions':
        if askyesno('Série de questions finie.','Voulez-vous rejouez ?' ):
            nb_questions = 5                
            newValues()
            updateUI()
        else :
            root.quit()    
#Raccourci clavier pour vérifier
root.bind('<Return>', verif_result2)
verifResultButton.config(command=verif_result)

# on lance le jeu
do('init')


#affichage
root.mainloop()

