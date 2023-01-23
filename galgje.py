#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 14:11:27 2023

@author: antoniebraams
"""

import random
import time
from wordsNL import nederlandse_woordenlijst_makkelijk,nederlandse_woordenlijst_gemiddeld,nederlandse_woordenlijst_moeilijk




def woord_1():
    woord1 = random.choice(nederlandse_woordenlijst_makkelijk)
    return woord1.upper()

def woord_2():
    woord2 = random.choice(nederlandse_woordenlijst_gemiddeld)
    return woord2.upper()

def woord_3():
    woord3 = random.choice(nederlandse_woordenlijst_moeilijk)
    return woord3.upper()
    

def niveau():
    level = input('Op welk leven zou u het spel willen spelen: ')
    return level

def galgje_1(woord):
    woord_in_proces = '_' * len(woord)
    woord_geraden = False
    geraden_letters = []
    geraden_woorden = []
    levens = 6
    print('Laten we beginnen!')
    print(visual_galgje(levens))
    print(woord_in_proces)
    print('\n') #voor extra regels tussen texten
   
    while woord_geraden == False and levens > 0:
        antwoord = input('Geef uw letter of een woord: ').upper()
        time.sleep(0.1)
       
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
        print('toaal:',len(woord),',nog te raden:',list(woord_in_proces).count('_'),',resterende levens:',levens)
        print('geraden letters:',','.join(geraden_letters))
        print('\n')  
    if woord_geraden == True:
        print('Van Harte gefeliciteerd, u heeft het woord geraden')
    else:
        print('Helaas, het is u niet gelukt om het woord te raden. Het antwoord was',woord,)

def galgje_2(woord):
    woord_in_proces = '_' * len(woord)
    woord_geraden = False
    geraden_letters = []
    geraden_woorden = []
    levens = 6
    print('Laten we beginnen!')
    print(visual_galgje(levens))
    print(woord_in_proces)
    # print('\n') #voor extra regels tussen texten
   
    while woord_geraden == False and levens > 0:
        antwoord = input('Geef uw letter of een woord: ').upper()
        time.sleep(0.1)
       
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
                print('U heeft dit woord al geraden:',antwoord)
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
        print('toaal:',len(woord),',nog te raden:',list(woord_in_proces).count('_'),',resterende levens:',levens)
        print('geraden letters:',','.join(geraden_letters))
        print('\n')  
    if woord_geraden == True:
        print('Van Harte gefeliciteerd, u heeft het woord geraden')
    else:
        print('Helaas, het is u niet gelukt om het woord te raden. Het antwoord was',woord,)
        
    
def galgje_3(woord):
    woord_in_proces = '_' * len(woord)
    woord_geraden = False
    geraden_letters = []
    geraden_woorden = []
    levens = 6
    print('Laten we beginnen!')
    print(visual_galgje(levens))
    print(woord_in_proces)
    print('\n') #voor extra regels tussen texten
   
    while woord_geraden == False and levens > 0:
        antwoord = input('Geef uw letter of een woord: ').upper()
        time.sleep(0.1)
       
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
        print('toaal:',len(woord),',nog te raden:',list(woord_in_proces).count('_'),',resterende levens:',levens)
        print('geraden letters:',','.join(geraden_letters))
        print('\n')  
    if woord_geraden == True:
        print('Van Harte gefeliciteerd, u heeft het woord geraden')
    else:
        print('Helaas, het is u niet gelukt om het woord te raden. Het antwoord was',woord,)

def shuffle(woord):
    woord_in_proces = '_' * len(woord)
    woord_geraden = False
    geraden_letters = []
    geraden_woorden = []
    levens = 6
    woord_geshuffled=list(woord)
    random.shuffle(woord_geshuffled)
    woord_= ''.join(woord_geshuffled)
    print('Laten we beginnen!')
    print(visual_galgje(levens))
    print(woord_in_proces)
    print('\n') #voor extra regels tussen texten
   
    while woord_geraden == False and levens > 0:
        antwoord = input('Geef uw letter of een woord: ').upper()
        time.sleep(0.1)
       
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
                
                plekken = [x for x, letter in enumerate(woord_) if letter == antwoord]
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
        print('toaal:',len(woord),',nog te raden:',list(woord_in_proces).count('_'),',resterende levens:',levens)
        print('geraden letters:',','.join(geraden_letters))
        print('\n')  
    if woord_geraden == True:
        print('Van Harte gefeliciteerd, u heeft het woord geraden: ',woord)
    else:
        print('Helaas, het is u niet gelukt om het woord te raden. Het antwoord was',woord,)
                
                
            
        
    
    

def visual_galgje(levens):
    fases = [ 
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
               
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
               
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
              
                """
                   --------
                   |      |
                   |      O
                   |     \\|
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
                """
                
    ]
    return fases[levens]
    




def spelen():
    woord1 = woord_1()
    woord2 = woord_2()
    woord3 = woord_3()
   
    level = int(niveau())
    if level == 1:
        galgje_1(woord1)
        while input('Wilt u nog een keer spelen? (Ja/Nee): ').upper() == 'JA':
            woord = woord_1()
            galgje_1(woord)
    elif level == 2:
        galgje_2(woord2)
        while input('Wilt u nog een keer spelen? (Ja/Nee): ').upper() == 'JA':
            woord = woord_2()
            galgje_2(woord)
    elif level == 3:
        galgje_3(woord3)
        while input('Wilt u nog een keer spelen? (Ja/Nee): ').upper() == 'JA':
            woord = woord_3()
            galgje_3(woord)
    elif level == 4:
        shuffle(woord1)
        while input('Wilt u nog een keer spelen? (Ja/Nee): ').upper() == 'JA':
            woord = woord_1()
            shuffle(woord)
    
    
if __name__ == "__main__":
    spelen()
    