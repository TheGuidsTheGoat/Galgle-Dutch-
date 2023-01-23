#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 19:22:00 2023

@author: maxdieleman
"""

import random
from wordsNL import nederlandse_woordenlijst_makkelijk


def engels_woord():
    woord = random.choice(nederlandse_woordenlijst_makkelijk)
    return woord.upper()

def galgje(woord):
    woord_in_proces = '_' * len(woord)
    woord_geraden = False
    geraden_letters = []
    geraden_woorden = []
    levens = 6
    print('Laten we beginnen!')
    print(visual_galgje(0))
    print(woord_in_proces)
    print('\n') #voor extra regels tussen texten
    while woord_geraden == False and levens > 0:
        antwoord = input('Geef uw letter of een woord: ').upper()
        
       
        if len(antwoord) == 1 and antwoord.isalpha():
            if antwoord in geraden_letters:
                print('U heeft deze letter al geraden',antwoord)
            elif antwoord not in woord:
                print('Helaas,',antwoord,'zit niet in het woord')
                geraden_letters.append(antwoord)
                levens -= 1
            else:
                print('Lekker bezig!',antwoord,'zit in het woord')
                geraden_letters.append(antwoord)
                woord_als_lijst = list(woord_in_proces)
                plekken = [x for x, letter in enumerate(woord) if letter == antwoord]
                for i in plekken:
                    woord_als_lijst[i] = antwoord
                woord_in_proces = ''.join(woord_als_lijst)
                if '_' not in woord_in_proces:
                    woord_geraden = True
        elif len(antwoord) == len(woord) and antwoord.isalpha():
            if antwoord in geraden_woorden:
                print('U heeft dit woord al geraden',antwoord)
            elif antwoord != woord:
                print('Helaas,',antwoord,'is niet het woord')
                print('\n')  
                levens -= 1
                geraden_woorden.append(antwoord)
            elif antwoord == woord:
                woord_geraden = True
                woord_in_proces = woord
        else:
            print('Geen geldige invoer')
        print(visual_galgje(levens))
        print(woord_in_proces)
        print('\n') 
        print('totaal:',len(woord),',nog te raden:',list(woord_in_proces).count('_'),',resterende levens:',levens)
        print('geraden letters:',','.join(geraden_letters))
        print('\n')  
    if woord_geraden == True:
        print('Van Harte gefeliciteerd, u heeft het woord geraden')
    else:
        print('Helaas, het is u niet gelukt om het woord te raden. Het antwoord was',woord,)
                
            
        
    
    

def visual_galgje(levens):
    fases = [ 
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
               
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
               
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
              
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
              
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
              
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
              
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                """
                   
                         
                         
                      
                         
                        
                   
                """
                
    ]
    return fases[levens]
    




def spelen():
    woord = engels_woord()
    galgje(woord)
    while input('Wilt u nog een keer spelen? (Ja/Nee): ').upper() == 'JA':
        woord = engels_woord()
        galgje(woord)
    
if __name__ == "__main__":
        spelen()