# -*- coding: utf-8 -*-
"""
HEADER

Objectifs : creer un pendu sous la forme de texte dans une premiere partie
puis avec une interface graphique dans une seconde

Created on Thu Dec  3 08:19:41 2020

@author: Pierre GOSSON 

ToDo : 

"""
from random import randint
from tkinter import Tk, Label, Entry, Canvas, PhotoImage, Button
"""
Cette fonction prend un fichier le trie par nombre de lettre et ordre 
alphabetique puis renvoie une liste avec les éléments triés
"""

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

"""
Test
listSorted = fSortfile("mots_pendu")

print(listSorted)
"""

"""
Fonction qui séléctionne un élément aléatoire de la liste et le renvoie
"""

def fRand(pList) :
    listSorted = fSortfile("mots_pendu")
    i = randint(0,len(listSorted)-1)
    
    return pList[i]
"""
Test
print (fAlea(listSorted)) 
"""

"""
Fonction qui prend un mot et qui rend la premiere lettre de ce dernier et 
des underscore pour le reste des lettres du mot
Crypte le mot pour le pendu
"""

def fReturnCodedWord(pWord) :
    list0 = []
    for element in pWord:
        letter1 = pWord[0]
        if element == letter1 :
            list0.append(element)
        else:
            list0.append("_")
    pCodedWord = ""
    for element in list0 :
        pCodedWord += element
        pCodedWord += ""
      
    return pCodedWord
    
"""
Test
  
print(fRendCryptMot(fAlea(listSorted)))
"""    
      
"""
Fonction pour construire le mot du joueur en jeu
"""

def gameWord(pLetter,pWord,pCodedWord):
    list0 = []
    for element in pWord:
        if element == pLetter or element in pCodedWord:
            list0.append(element)
        else:
            list0.append("_")
    valRen = listIntoWord(list0)
    return valRen

"""
Cette fonction permet de construire un mot à partir d'une liste
"""
def listIntoWord(pList): 
    valRen = ""
    for element in pList:
        valRen += str(element)
    return valRen 
    
    
    
"""
Fonction principale de jeu
"""

def fGame(): 
    global word
    global codedWord
    global userTry
    global listLetter
    word = fRand(fSortfile("mots_pendu"))
    codedWord = fReturnCodedWord(word)
    userTry = 8
    listLetter = []
    valRen = False
    while userTry > 0 and valRen == False:
        print("Le mot : "+codedWord)
        print("Nombre de lettres : "+str(len(word)))
        print("Vie restantes : "+str(userTry))
        if codedWord != word:
            userLetter = fSameLetter(listLetter) 
            listLetter.append(userLetter)
            if userLetter not in word:
                userTry -= 1
                print("Raté :"+userLetter+" n'est pas dans le mot")
            else:
                print(userLetter+" est dans le mot.")
                codedWord = gameWord(userLetter,word,codedWord)
        else:
            valRen = True
    if valRen == True:
        print("Félicitation vous avez réussi à trouver : "+word)
        print("Avec encore "+userTry+" tentatives restantes")
    else:
        print("Perdu, le mot était : "+word)
    
        

    

"""
Fonction qui vérifie l'usage de une seule lettre de l'alphabet
"""

def fOneInput(pUserLetter): 
    if (len(pUserLetter) == 1 and pUserLetter.lower() in "azertyuiopqsdfghjklmwxcvbn"):
        return True
    else:
        return False
    
"""
Fonction qui permet de ne pas avoir deux fois la meme lettre input par l'user
"""

def fSameLetter(pListLetter): 
    UserLetter = ""
    while fOneInput(UserLetter) == False or UserLetter in pListLetter:
        print("Lettres déjà utilisées:")
        print(pListLetter)
        UserLetter = input("Merci d'entrer une unique lettre de l'alphabet, (précédemement non utilisé): ").lower()
    return UserLetter
    
    

fGame()















    
    
    