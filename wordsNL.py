#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 19:30:38 2023

@author: maxdieleman
"""

nederlandse_woordenlijst_makkelijk=['aaien','aambei','aambeeld','aanbod','aanbouw','aandeel',
'aandoen','aanhef','aanleg','aannemen','aanpassen','aanslag','aanzoek','aardappel','aardbei','aardbol',
'aardig','abonnee','absent','absurd','accent','account','achtbaan','achter','actie','acuut','actueel',
'adder','adelaar','adres','adten','advies','afdruk','afgunst','afkomst','afname','afschuw','afspraak',
'afval','afwas','afzien','auteur','augurk','agent','akkoord','akker','alarm','algebra','allemaal','alleen',
'alvast','amandel','ander','ananas','angst','anker','anoniem','appel','apparaat','arbeid','archief','arend',
'aroma','arrest','artiest','asbak','asbest','asfalt','assist','atelier','atlas','audio','attent','autist',
'avond','azijn','baard','badpak','balans','balie','balkon','balsem','balpen','banaan','banket','barbaar',
'barst','bedrag','bedrog','bejaard','bekend','beleid','beroemd','beroerd','besef','beslag','bestaan','bestek',
'betoog','beton','beugel','beurt','bever','bezig','bijbel','bijlage','bijnaam','bikkel','binnen','bloed',
'blind','bloesem','bloem','bloei','blond','bloot','bobbel','blowen','blubber','blues','bodem','boeket',
'boeien','boerin','boeman','boezem','bokser','bokaal','bonbon','bonus','borrel','borstel','botsing',
'braak','bowlen','braam','brand','breed','breekbaar','brief','brommer','brood','budget','buidel','buffel',
'buiten','bunker','burger','camera','casette','categorie','cavia','censuur','centraal','centrum','chaos',
'charme','cheeta','chocola','cilinder','cijfer','citaat','circus','cobra','comfort','concept','compleet',
'contact','contant','correct','corrupt','corvee','couscous','cracker','cowboy','crisis','cursus','daarna',
'daarom','dagboek','dansles','debat','dekbed','dessert','detail','deugd','dicht','dienst','dispuut',
'dochter','docent','doelgroep','domein','dolfijn','domino','dokter','donker','donut','dooier','doorn',
'draad','drama','drank','drempel','droger','droom','druppel''drukte','dubbel','duister','duivel','dummy',
'dwerg','echter','eczeem','edelsteen','eenhoorn','eenzaam','eetlepel','effect','eicel','einde','eiwit',
'elftal','emmer','emotie','engel','enkel','enorm','entree','enter','ernst','etage','ethiek','etmaal','evenaar',
'expres','ezelin','factor','factuur','fagot','fakkel','fakir','fameus','farao','feest','fiets','fiche','figuur',
'filter','finish','flauw','flensje','flink','focus','folder','fonds','formaat','friet','frituur','fruit','fusie',
'gajes','galgje','gammel','garage','gebak','gazon','geheim','gember','gemeente','genoeg','gesprek','getto',
'gevoel','gevolg','geweten','gewoon','gezin','gezond','gierig','gieter','gister','gnoom','graad','graag',
'gracht','gratis','grens','gravin','grimmig','groot','grond','gunst','haaibaai','haard','handbal','handig',
'havik','haver','haven','hecht','heldin','helium','hemel','hengel','herberg','herfst','hertog','heuvel',
'hiphop','hobby','hockey','hoest','hommel','honger','honing','horeca','horizon','horzel','hotdog','hufter',
'hyena','icoon','']

nederlandse_woordenlijst_gemiddeld=['aanvaller','aandacht','aanklacht','aanrecht','aardkorst','aardolie',
'abject','abortus','abrikoos','acceptabel','accijns','accuraat','actief','adoptie','ademnood','afgetraind',
'advertentie','advocaat','afdronk','absoluut','abstract','afleiding','afwijking','afzetter','alcohol','albino',
'albatros','alvleesklier','ansjovis','allergie','andijvie','ambtenaar','apotheek','automaat','badmuts',
'bankstel','barbecue','basketbal','batterij','bedrijf','bewoner','biefstuk','bierbuik','besluit','biologie',
'bioscoop','bliksem','boerderij','boerenkool','boksbal','bofkont','boetiek','bonsai','bospeen','botox',
'botsauto','bovenbouw','bovenbeen','braderie','brandweer','briljant','bromvlieg','browser','brugklas','bruiloft',
'bubbelbad','brigade','burrito','bushalte','calorie','chagrijnig','champagne','carnaval','casino','champignon',
'coffeeshop','commando','commissie','conclusie','concurrent','consument','continent','chauffeur','cyclus',
'coureur','couplet','dahlia','dartbord','decibel','decoratie','dementie','democratie','denksport','depressie',
'designer','diabetes','diagonaal','diadeem','diameter','dictaat','dictator','diploma','dinosaurus','dirigent',
'dobbelsteen','document','doodstraf','doperwt','dossier','download','draaikolk','dominee','dressoir',
'driftkikker','doelpunt','droogkloot','drumstel','duikbril','duizendpoot','eclips','ecologie','edelhert',
'educatie','eekhoorn','eenvoudig','eierdop','eigenaardig','eigenlijk','eikenhout','eindbaas','elastiek',
'elektriciteit','elitair','empathie','erfenis','essentie','etalage','evolutie','evenwicht','everzwijn','excuus',
'exemplaar','faalangst','failliet','faculteit','fanatiek','farmacie','favoriet','fenomeen','fietspad','fetisj',
'festival','fijnstof','filmrol','filosofie','fitness','flacon','flamingo','flipperkast','formulier','fornuis',
'fortuin','fragment','frietsaus','frisdrank','furieus','gadget','galerij','galsteen','gangpad','garantie',
'gasstel','gaspedaal','gazelle','gebarentaal','geniaal','geometrie','geografie','geologie','getuige',
'gevangenis','gewricht','gezondheid','gigantisch','giraffe','glijbaan','globaal','gloeilamp','godsdienst',
'golfclub','goochelaar','gootsteen','gorilla','gotiek','gourmet','grafiek','graffiti','groenteboer','grofvuil',
'grondwet','groothandel','grootvader','hacker','hagedis','hamburger','handbagage','handdoek','handicap',
'hangslot','hardcore','harmonica','harpoen','hartaanval','heerlijk','heimwee','hekserij','herkauwer',
'hindernis','hilarisch','hoefijzer','hoofdgerecht','hoofdrol','hoogleraar','hovenier','huidskleur','huisarrest',
'huwelijk','hypotheek']

nederlandse_woordenlijst_moeilijk=['abominabel','acapella','adequaat','aerobics','acupunctuur','adhesie'
'affiniteit','aftershave','agave','aktetas','allegro','alliage','amputatie','analogie','annexatie',
'anorexia','anticlimax','aquaduct','archeoloog','accordeon','arbitrage','artefact','artisjok','associatie',
'assonantie','autonoom','baarmoeder','babysitter','bachelor','bakermat','bapao','baptist','barricade',
'beeldhouwer','bekrompen','belangrijk','bemoeial','bespioneren','bevoegdheid','bewusteloos',
'bijwerking','biografie','bipolair','bladgoud','blokfluit','boaconstrictor','boeddha','boekhouder',
'boeventronie','boleet','bombastisch','bondscoach','bootcamp','botulisme','braille','brancard','breakdance',
'broeikaseffect','bucketlist','bungalow','cabaret','caleidoscoop','cartografie','carrousel','carpaccio',
'catastrofe','chauvinisme','cholesterol','clementie','cognac','concours','conifeer','cosinus','cyberpesten',
'declaratie','defibrilator','delinquent','delirium','desolaat','detacheren','digestie','doctrine','dompteur',
'draconisch','drankorgel','dreigbrief','dubbelganger','duplex','dwarsfluit','dwarslaesie','dyslexie',
'echoscopie','egards','eindexamen','ejaculatie','emancipatie','encyclopedie','enthousiast','equivalent',
'ergonomie','esthetiek','examinator','executie','fabricaat','fauteuil','felicitatie','filantroop','flauwekul',
'florissant','fouilleren','frequentie','fuchsia','functioneel','fysiotherapie','cocktail','genetica',
'genuanceerd','geranium','geuzennaam','glascontainer','glasvezel','globetroter','goniometrie','goudbruin',
'graftombe','grijpstuiver','guerrilla','guillotine','gymnasium','gynaecoloog','halfpension','halleluja',
'harakiri','herbivoor','hielenlikker','homeopaat','honkbalknuppel','honorair','hyperactief','hypocriet','']














