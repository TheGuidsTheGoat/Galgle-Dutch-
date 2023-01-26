#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 16:37:27 2023

@author: antoniebraams
"""

import random #hier importeren we twee bibliotheken om wat meer codes te kunnen gebruiken
import time

#In de volgende drie functies worden random woorden van verschillende niveau's gekozen uit de woordenlijst

def woord_1():  
    woord1 = random.choice(nederlandse_woordenlijst_makkelijk)
    return woord1.upper()

def woord_2():
    woord2 = random.choice(nederlandse_woordenlijst_gemiddeld)
    return woord2.upper()

def woord_3():
    woord3 = random.choice(nederlandse_woordenlijst_moeilijk)
    return woord3.upper()
    
#De functie genaamd 'niveau' wordt afgespeeld als we willen weten welk niveau de gebruiker het spel wil spelen
    
def niveau():
    level = input('Op welk level zou u het spel willen spelen: ')
    return level

#In de functie 'galgje1' speelt zicht galgje af op niveau 1, hetzelfde geldt voor de andere galgje functies maar dan op de andere niveaus

def galgje_1(woord):
    woord_in_proces = '_' * len(woord) #creeren string van lege balkjes ter lengte van het woord
    woord_geraden = False #initiële waarde van de variabele die naar True gaat als het woord is geraden
    geraden_letters = [] #lijst waar alle geraden letters in bewaard worden
    geraden_woorden = [] #lijst waar alle geraden woorden in bewaard worden
    levens = 6 #het spel begint met 6 levens en daar begint de variabele ook mee
    
    print('Laten we beginnen!')
    
    print(visual_galgje(levens)) #laat de galg in het scherm zien door uit de juiste levens in te vullen bij de functie: 'visual galgje'
    
    print(woord_in_proces) #laat de streepjesbalk waar het woord geraden wordt zien in beeld, deze is in het begin nog leeg
    
    print('\n') #voor extra regels tussen teksten
   
    while woord_geraden == False and levens > 0: #een loop die doorgaat totdat de levens op zijn of het woord geraden is
        antwoord = input('Geef uw letter of een woord: ').upper() #vraagt zolang de loop doorgaat de speler om een input in de vorm van een letter of een woord
        time.sleep(0.1) #zet een kleine pauze op de code, dit vonden we er wat mooier uitzien
       
        if len(antwoord) == 1 and antwoord.isalpha(): #kijkt of de input van de gebruiker wel geldig is en of het in het woord voorkomt 
            if antwoord in geraden_letters:
                print('U heeft deze letter al geraden',antwoord)
            elif antwoord not in woord:
                print('Helaas,',antwoord,'zit niet in het woord')
                geraden_letters.append(antwoord) #voegt geraden letter toe aan lijst met geraden letters
                levens -= 1 
            else:
                print('Lekker bezig!',antwoord,'zit in het woord')
                geraden_letters.append(antwoord)
                woord_als_lijst = list(woord_in_proces)
                plekken = [x for x, letter in enumerate(woord) if letter == antwoord] #hier kijken we op welke indexen de geraden letter allemaal voorkomt 
                for i in plekken: #hier vervangen we met hulp van de indexen alle plekken waar eerst nog een balkje stond nu met de geraden letter
                    woord_als_lijst[i] = antwoord
                woord_in_proces = ''.join(woord_als_lijst)
                if '_' not in woord_in_proces: #als alle balkjes verdwenen zijn, verandert onze variabele die we initieel als False hadden gezet in True en zal onze loop stoppen
                    woord_geraden = True
        elif len(antwoord) == len(woord) and antwoord.isalpha(): #voor het geval als de gebruiker een heel woord als input geeft word er hier gekeken of het wel geldige invoer is en dezelfde lengte heeft als het woord
            if antwoord in geraden_woorden:
                print('U heeft dit woord al geraden',antwoord)
            elif antwoord != woord:
                print('Helaas,',antwoord,'is niet het woord')
                print('\n')  
                levens -= 1
                geraden_woorden.append(antwoord) #als het woord fout is word het woord in de lijst gezet in de lijst met alle geraden woorden
            elif antwoord == woord:
                woord_geraden = True # als het woord klopt word de variabele die initieel als False stond verandert in True
                woord_in_proces = woord
        else:
            print('Geen geldige invoer') #als er geen geldige invoer was dan laten we dat hiermee weten aan de gebruiker
        print(visual_galgje(levens))
        print(woord_in_proces)
        print('\n') 
        print('totaal:',len(woord),',nog te raden:',list(woord_in_proces).count('_'),',resterende levens:',levens) #dit wordt getoond aan de gebruiker tijdens het spel om te kunnen zien hoeveel letters er in totaal zijn, hoeveel nog te gaan en welke letters er al geraden zijn
        print('geraden letters:',','.join(geraden_letters))
        print('\n')  
    if woord_geraden == True: #dit is weer buiten de while loop en als onze variabele veranderd is in True weet de code dat de gebruiker het woord heeft geraden
        print('Van Harte gefeliciteerd, u heeft het woord geraden')
    else: #zo niet, dan weet de code dat de gebruiker het woord niet heeft geraden 
        print('Helaas, het is u niet gelukt om het woord te raden. Het antwoord was',woord,)

#in de volgende drie functies zijn alleen de niveaus anders en verschillen dus eigenlijk alleen de woorden met de code van galgje1       
#daarom is er alleen commentaar bij stukjes code die afwijken van galgje1        

def galgje_2(woord):
    woord_in_proces = '_' * len(woord)
    woord_geraden = False
    geraden_letters = []
    geraden_woorden = []
    levens = 6
    print('Laten we beginnen!')
    print(visual_galgje(levens))
    print(woord_in_proces)
    
   
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
        print('totaal:',len(woord),',nog te raden:',list(woord_in_proces).count('_'),',resterende levens:',levens)
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
    print('\n') 
   
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
        print('totaal:',len(woord),',nog te raden:',list(woord_in_proces).count('_'),',resterende levens:',levens)
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
    random.shuffle(woord_geshuffled) #hier worden de letters van het woord in een random volgorde gezet
    woord_= ''.join(woord_geshuffled)
    print('Laten we beginnen!')
    print(visual_galgje(levens))
    print(woord_in_proces)
    print('\n') #voor extra regels tussen teksten
   
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
        print('totaal:',len(woord),',nog te raden:',list(woord_in_proces).count('_'),',resterende levens:',levens)
        print('geraden letters:',','.join(geraden_letters))
        print('\n')  
    if woord_geraden == True:
        print('Van Harte gefeliciteerd, u heeft het woord geraden: ',woord)
    else:
        print('Helaas, het is u niet gelukt om het woord te raden. Het antwoord was',woord,)
                
                
            
        
#in de functie visual_galgje worden de verschillende plaatjes die tijdens het aan de gebruiker worden getoond opgeslagen     
    

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
    


#de functie spelen is de hoofdfunctie van de code waar alle andere functies zich bevinden en worden gereguleerd

def spelen():
    
    #hier worden de woorden uit de woordenlijst gekozen
    woord1 = woord_1()
    woord2 = woord_2()
    woord3 = woord_3()
   
    level = niveau() #hier wordt er in een variabele opgeslagen op welk niveau de gebruiker wilt spelen, deze geeft de gebruiker als input
    
    #in het volgende stukje wordt galgje gespeeld op het juiste niveau en in een loop waardoor de gebruiker kan blijven spelen zolang ze ja zeggen op de vraag 
    if int(level) == 1:
        galgje_1(woord1)
        while input('Wilt u nog een keer spelen? (Ja/Nee): ').upper() == 'JA':
            woord = woord_1()
            galgje_1(woord)
    elif int(level) == 2:
        galgje_2(woord2)
        while input('Wilt u nog een keer spelen? (Ja/Nee): ').upper() == 'JA':
            woord = woord_2()
            galgje_2(woord)
    elif int(level) == 3:
        galgje_3(woord3)
        while input('Wilt u nog een keer spelen? (Ja/Nee): ').upper() == 'JA':
            woord = woord_3()
            galgje_3(woord)
    elif int(level) == 4:
        shuffle(woord1)
        while input('Wilt u nog een keer spelen? (Ja/Nee): ').upper() == 'JA':
            woord = woord_1()
            shuffle(woord)
    
   
    
if __name__ == "__main__":
    print('1 - makkelijk')
    print('2 - gemiddeld')
    print('3 - moeilijk')
    print('4 - shuffle (heel moeilijk)')
    spelen()
