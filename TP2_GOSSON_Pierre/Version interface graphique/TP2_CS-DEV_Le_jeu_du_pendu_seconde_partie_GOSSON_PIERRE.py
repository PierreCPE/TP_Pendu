# -*- coding: utf-8 -*-
"""
HEADER

Objectifs : creer un pendu sous la forme de texte dans une premiere partie
puis avec une interface graphique dans une seconde

Created on Thu Dec  3 08:19:41 2020

@author: Pierre GOSSON 

ToDo : Ne fonctionne pas une de mes fonctions boucle car elle ne dois pas reconnaitre une autre le TKINTER semble marcher seul en terme d'affichage, 

"""

from random import randint
from tkinter import Tk, Label, Entry, Canvas, PhotoImage, Button, StringVar, IntVar





#Cette fonction prend un fichier le trie par nombre de lettre et ordre 
#alphabetique puis renvoie une liste avec les éléments triés



def fSortfile(pFile) : 
    file = open(pFile+".txt",'rt')
    lWords = file.readlines()
    lWords.sort()
    lWords.sort(key= lambda item:len(item))
    for i,element in enumerate(lWords):
        if "\n" in element:
            lWords[i] = element[:-1]
    file.close()
    return lWords




#Fonction qui séléctionne un élément aléatoire de la liste et le renvoie


def fRand(pList) :
    listSorted = fSortfile("mots_pendu")
    i = randint(0,len(listSorted)-1)
    
    return pList[i]




#Fonction pour construire le mot du joueur en jeu


def fDispGameWord(pWord,pLetterFound):
    list0 = ""
    for i, L in enumerate(pWord) :
        if i==0 or L in pLetterFound :
            list0+=L
        else:
            list0=" _"
    return list0



#Fonctions pour l'input de l'utilisateur:

def fInputUser ():
    letter = input("Merci d'entrer une unique lettre de l'alphabet, (précédemement non utilisé): ").lower()
    return letter


#Fonction pour savoir si l'utilisateur gagne ou non

def fWin(pWord,pLetterFound) :
    i=0
    for pLetter in pWord:
        if pLetter in pLetterFound:
            i+=1
        elif i==len(pWord) :
            return True 



#Fonction pour le meilleur score :
            
def fBestScore(pBestScore):
        score=fGame()
        if score > pBestScore :
            pBestScore = score
            print("le meilleur score est :"+str(pBestScore))
pBestScore = 0



#Vérification de l'input user 

def fCheck(pLetterFound,pWrongLetter,pWord,pLetter,pUserTry) :
    if pLetter in pLetterFound or pLetter in pWrongLetter :
        print("La lettre à déjà été utilisée !")
    elif pLetter in pWord :
        pLetterFound.append(1)
        fDispGameWord(pWord, pLetterFound)
        print("Bravo ! la lettre est dans le mot.")
        
    else :
        pUserTry-=1
        pWrongLetter.append(1)
        print("La lettre est fausse, dommage, chances restantes : ",pUserTry)
        
        
#Fonction principal de jeu : 
        
def fGame():
    global pUserTry
    global pWord
    global pLetterFound
    global pWrongLetter
    
    fDispGameWord(pWord,pLetterFound)
    while pUserTry > 0 :
        pLetter = fInputUser()
        print (pLetter)
            
        fCheck(pLetterFound, pWrongLetter, pWord, pLetter, pUserTry)
        if fWin(pWord, pLetterFound)==True :
            print("Félicitation, vous avez gagné ")
            score = pUserTry
            pUserTry = 0
                
        else :
            print("Raté, il vous reste :",pUserTry,"chances")
                
    if pUserTry==0 and fWin(pWord, pLetterFound) != True :
        print("C'est perdu ! ")
    elif pUserTry == 0:
        valRen=input("rejouer ? o pour oui n'importe quoi d'autre pour non ")
        
        if valRen=="o" :
            return score, fGame()
        else :
            return score
        
#Quelques variables coter editeur :

pUserTry=8
pLetterFound=[]


    #Initialisation du mot
pWord=(fRand(fSortfile("mots_pendu")))

pFoundLetter= pWord[0]
pWrongLetter=[]       
        
        
        
        
 

"""
Partie TKINTER
"""


#Création de la fenetre tkinter 

wind1 = Tk()
wind1.title("Jeu du pendu")



#Création du canvas : 

canvas=Canvas(wind1, height=300, width=300, bg='black')
myMan='bonhomme'+str(pUserTry)+'.gif'
pic = PhotoImage(file=myMan)
item = canvas.create_image(150,150, image = pic )




#Les entry:
pLetter=StringVar()
entButton=Entry(wind1,textvariable=pLetter)
#Le bouton entrée:

inputButton=Button(wind1, text='Proposer', command=fGame())


#Le bouton quitter :

leaveButton=Button(wind1,text='Quitter ?', command=wind1.destroy)

#Les labels:

wantedWord = fDispGameWord(pWord, pLetterFound)
labelWantedWord = Label(wind1, text = wantedWord, fg='black',bg='white')

pUserTry=IntVar()
pUserTry.set(str(pUserTry))
labelUserTry = Label (wind1, textvariable=pUserTry, fg='white', bg='black')



#Agencement de la page TKINTER :



canvas.grid(row=1,column=2,rowspan=6,sticky='ne')
labelWantedWord.grib(row=1,column=1,sticky='n')
labelUserTry.grib(row=2,column=1,sticky='n')
inputButton.grid(row=3,column=1)
leaveButton.grid(row=4)
entButton.grid(row=5)




wind1.mainloop()








