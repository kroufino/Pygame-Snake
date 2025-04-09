import pygame
from pygame.locals import *
import random
import time
import os
def vykreslení_okna(okno,bg):#Výplň okna
    okno.fill(bg) 
def vykreslení_obtížnosti(obtiznost,font,okno,šířka_okna,výška_okna,obtiznosti):#Vykreslení zvolené obtížnosti
    text_obtiznosti = f"Obtížnost: {obtiznost}"
    if obtiznost == obtiznosti[0]:
        barva = (0, 255, 0)
    elif obtiznost == obtiznosti[1]:
        barva = (255, 255, 0)
    else:
        barva = (255, 0, 0)
    obtiznost_okno = font.render(text_obtiznosti, True, barva)
    okno.blit(obtiznost_okno, ((šířka_okna * 0.3), výška_okna - 33))
def vykreslení_score(score,obtiznosti,okno,obtiznost,font,šířka_okna):#Vykreslení dosaženého skóre
    text = f"Skóre: {score}"
    if obtiznost == obtiznosti[0]:
        barva = (0, 255, 0)
    elif obtiznost == obtiznosti[1]:
        barva = (255, 255, 0)
    else:
        barva = (255, 0, 0)
    skóre = font.render(text, True, barva)
    okno.blit(skóre, ((šířka_okna * 0.42), 3))
def kontrola_konce_hry(konec_hry, pozice_hada,výška_okna,šířka_okna,velikost_blocku):#Kontrola podímnek pro ukončení hry
    #Kontrola kolize hada s jeho tělem
    cislo_blocku = 0
    for segment in pozice_hada:
        if pozice_hada[0] == segment and cislo_blocku > 0: #Vynechá hlavu
            konec_hry = True #kolize hlavy s ostatními částmi
        cislo_blocku += 1
    #kontrola jestli je had mimo pole
    if pozice_hada[0][0] < 0 or pozice_hada[0][0] > šířka_okna - velikost_blocku or pozice_hada[0][1] < 0 or pozice_hada[0][1] > výška_okna - velikost_blocku:
        konec_hry = True
    return konec_hry
def vykresleni_volby(okno,font,šířka_okna):#Vykreslení textu pro volbu
    text = f"Zvol si obtížnost:"
    volba = font.render(text, True, (255, 255, 255))
    okno.blit(volba, ((šířka_okna * 0.33), 3))
def vykresleni_konce_hry(font,okno,šířka_okna,výška_okna,změna,tlačítko,font_mensi):#Vykreslení konečné obrazovky
    konec = "! Konec hry !"
    konec = font.render(konec, True, (255, 255, 255))
    pygame.draw.rect(okno, (255, 0, 0), (šířka_okna // 2 - 100, výška_okna // 2 - 70, 200, 50), 2, 3)
    okno.blit(konec, (šířka_okna // 2 - 85, výška_okna // 2 - 58))
    znovu = "Hrát znovu?"
    znovu = font.render(znovu, True, (255, 255, 255))
    pygame.draw.rect(okno, (255, 0, 0), tlačítko, 2, 3)
    okno.blit(znovu, (šířka_okna // 2 - 80, výška_okna // 2 + 10))
    info = "<--- klikni" #Popisek tlačíka
    info = font_mensi.render(info, True, (0, 255, 0))
    okno.blit(info, (šířka_okna // 2 + 100, výška_okna // 2 + 10))
    if změna == True: #Pokud se provedla změna skóre v souboru pro ukládání skóre, tak se na obrazovce zobrazí popisek infromující o dosažení nového skoŕe
        info = "|i| Dosáhl jsi nového nejlepšího skóre |i|"
        info = font_mensi.render(info, True, (255, 255, 255))
        okno.blit(info, (0 + šířka_okna // 6, výška_okna - výška_okna // 5))


#Zapisování nejlepšího výsledku skóre uživatelem dosaženého
def zápis_score(score,soubor_skóre,obtiznosti,obtiznost):
    #  Struktura souboru pro high score:
    #  1;10 
    #  2;8
    #  3;12
    # čísla značí obtížnost, to po ";" jsou hodnoty nejlepšího skóre pro individuální level obtížnosti 
    high_score = []
    working = score #pracovní proměná pro lepší orientaci
    vytvoř = False
    změna = False
    #čtení hodnot
    try:
        with open(f"{soubor_skóre}", "r", encoding="utf-8") as file:
            radky = file.readlines()
            try:
                for i in range(3):
                    hlavni = radky[i].strip()
                    try:
                        if int(hlavni.split(";")[0]) == i + 1:
                            try:
                                cislo = hlavni.split(";")[1]
                                try:
                                    cislo = int(cislo)
                                    high_score.append(cislo)
                                except ValueError:
                                    high_score.append("0")
                            except IndexError:
                                high_score.append("0")
                        else:
                            vytvoř = True
                    except ValueError:
                        vytvoř = True
                        high_score = ["0", "0", "0"]
            except IndexError:
                vytvoř = True
                high_score = ["0", "0", "0"]
    except FileNotFoundError:
        vytvoř = True
        high_score = ["0", "0", "0"]
    if vytvoř == True: #Pokud je to třeba, je vytvořen nový soubor, pro ukládání skóre
        high_score[obtiznosti.index(obtiznost)] = working
        radky = []
        pocet = 0
        for obsah in high_score:
            pocet += 1
            if pocet == 3:
                radky.append(f"{pocet};{obsah}")
            else:
                radky.append(f"{pocet};{obsah}\n")
        with open(f"{soubor_skóre}", "w", encoding="utf-8") as file:
            file.writelines(radky)
        if working != 0:
            změna = True
    if int(high_score[obtiznosti.index(obtiznost)]) < working:#Kontrola dosažení nového skóre
        high_score[obtiznosti.index(obtiznost)] = working
        radky = []
        pocet = 0
        for obsah in high_score:
            pocet += 1
            if pocet == 3:
                radky.append(f"{pocet};{obsah}")
            else:
                radky.append(f"{pocet};{obsah}\n")
        with open(f"{soubor_skóre}", "w", encoding="utf-8") as file:
            file.writelines(radky) 
        změna = True #nyní se splní podmínka v vykresleni_konce_hry() a vykreslí se popisek infromující uživatele o dosažení nové hodnoty skóre

    return změna
def popisky(easy,medium,hard,okno,obtiznosti,font_mensi):#Popisky k blockům obtížnosti(volitelné)
    moznosti = [easy, medium, hard]
    for i in range(3):
        info = f"{obtiznosti[i]}"
        block = moznosti[i]
        info = font_mensi.render(info, True, (255, 255, 255))
        okno.blit(info, (block[0] + 30, block[1]))
def vytvoření_jídla(obtiznost,obtiznosti,velikost_blocku,šířka_okna,výška_okna,jidlo):#Tvorba blocku, který bude reprezentovat jídlo
    if obtiznost == obtiznosti[0]: #easy obtížnost(blocky nebudou nikdy na okraji obrazovky)
        jidlo[0] = velikost_blocku * random.randint(2, round(šířka_okna / velikost_blocku) - 2) #Generování náhodného čísla reprezentující pozici x, pro block jídla, který nebude na okraji obrazovky
        jidlo[1] = velikost_blocku * random.randint(2, round(výška_okna / velikost_blocku) - 2) #Generování náhodného čísla reprezentující pozici y, pro block jídla, který nebude na okraji obrazovky
    elif obtiznost == obtiznosti[1]: #medium obtížnost(pozice blocku na okraji je 1 ku 2)
        nahodne = random.randint(0, 1)
        if nahodne == 1: #jídlo bude na okraji
            osa = random.choice(["x", "y"])
            strana = random.randint(0,1)
            if osa == "y":
                jidlo[0] = velikost_blocku * random.randint(0, round(šířka_okna / velikost_blocku) - 1) #Generování náhodného čísla reprezentující pozici x, pro block jídla
                if strana == 1:
                    jidlo[1] = 0
                else:
                    jidlo[1] = výška_okna - velikost_blocku
            elif osa == "x":
                if strana == 1:
                    jidlo[0] = 0
                else:
                    jidlo[0] = šířka_okna - velikost_blocku
                jidlo[1] = velikost_blocku * random.randint(0, round(výška_okna / velikost_blocku) - 1) #Generování náhodného čísla reprezentující pozici y, pro block jídla
        else: #jídlo nebude na okraji
            jidlo[0] = velikost_blocku * random.randint(2, round(šířka_okna / velikost_blocku) - 2) #Generování náhodného čísla reprezentující pozici x, pro block jídla
            jidlo[1] = velikost_blocku * random.randint(2, round(výška_okna / velikost_blocku) - 2) #Generování náhodného čísla reprezentující pozici y, pro block jídla
    elif obtiznost == obtiznosti[2]: #hard obtížnost, neboli jídlo je vždy na okraji obrazovky
            osa = random.choice(["x", "y"])
            strana = random.randint(0,1)
            if osa == "y":
                jidlo[0] = velikost_blocku * random.randint(0, round(šířka_okna / velikost_blocku) - 1) #Generování náhodného čísla reprezentující pozici x, pro block jídla
                if strana == 1:
                    jidlo[1] = 0
                else:
                    jidlo[1] = výška_okna - velikost_blocku
            elif osa == "x":
                if strana == 1:
                    jidlo[0] = 0
                else:
                    jidlo[0] = šířka_okna - velikost_blocku
                jidlo[1] = velikost_blocku * random.randint(0, round(výška_okna / velikost_blocku) - 1) #Generování náhodného čísla reprezentující pozici y, pro block jídla
    return jidlo