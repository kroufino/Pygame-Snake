import pygame
from pygame.locals import *
from packages import funkce
import random
import time

def choice(šířka_okna,výška_okna,velikost_blocku,okno,bg,font,font_mensi,fps,outline,modra,body_inner,soubor_skóre,obtiznosti):
    easy = [šířka_okna // 5, výška_okna // 3] #Souřadnice blocku reprezentující Easy obtížnost
    medium = [šířka_okna // 2, výška_okna // 3] #Souřadnice blocku reprezentující Mid obtížnost
    hard = [šířka_okna // 1.25, výška_okna // 3] #Souřadnice blocku reprezentující Hard obtížnost
    skore = [4 * velikost_blocku, (výška_okna // 3) * 2 + velikost_blocku * 3] #Souřadnice blocku reprezentující vypsání dosažených hodnot skóre
    reset = [šířka_okna // 1.5, (výška_okna // 3) - velikost_blocku * 3] #Souřadnice blocku reprezentující Možnost resetu hodnot skóre
    popis = [šířka_okna - velikost_blocku * 4, (výška_okna // 3) * 2 + velikost_blocku * 3] #Souřadnice blocku reprezentující Popisky blocků
    #Proměnné
    neměnit_směr = False
    timeout = 0
    zobraz_skore = False
    run = True
    konec_hry = False
    aktualizuj = False
    cekej = 0
    směr = 2
    pomoc = False
    prohra = 0
    start = time.time()
    #Pozice hada uzpůsobené směru vpravo, který je nutný pro toto menu
    pozice_hada = [[int(šířka_okna / 2), int(výška_okna / 2)]]#list pozic blocků + přidání prvního blocku
    pozice_hada.append([int(šířka_okna / 2) - velikost_blocku, int(výška_okna / 2) ])#Druhý block
    pozice_hada.append([int(šířka_okna / 2) -velikost_blocku * 2, int(výška_okna / 2)])#Třetí block
    pozice_hada.append([int(šířka_okna / 2) - velikost_blocku * 3, int(výška_okna / 2)])#Čtvrtý block
    #Začátek Menu
    while run:
        cas = round(time.time() - start, 2)#Výpočet času pro správnou funkci fps
        funkce.vykreslení_okna(okno,bg)
        #Kontrola událostí provedených uživatelem
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and stisk == 0 and neměnit_směr == False:
                if event.key == pygame.K_w and směr != 3:#Pokud stiskneme W a proměnná směr není 3, což by znamenalo že had se pohybuje směrem dolu, tak se změní proměnná směr na 1, což znamená, že pojede nahoru
                    směr = 1
                if event.key == pygame.K_d and směr != 4:#Pokud stiskneme D a proměnná směr není 4, což by znamenalo že had se pohybuje směrem doleva, tak se změní proměnná směr na 2, což znamená, že pojede doprava
                    směr = 2
                if event.key == pygame.K_s and směr != 1:#Pokud stiskneme S a proměnná směr není 1, což by znamenalo že had se pohybuje směrem nahoru, tak se změní proměnná směr na 1, což znamená, že pojede dolu
                    směr = 3
                if event.key == pygame.K_a and směr != 2:#Pokud stiskneme A a proměnná směr není 2, což by znamenalo že had se pohybuje směrem doprava, tak se změní proměnná směr na 1, což znamená, že pojede doleva
                    směr = 4
                stisk += 1
        if zobraz_skore == False:
            funkce.vykresleni_volby(okno,font,šířka_okna)
            if pomoc == True:#Pokud hráč aktivuje nápovědu, tato funkce zobrazí popisky jednotlivých blocků
                funkce.popisky(easy,medium,hard,okno,obtiznosti,font_mensi)
            #Vykreslení blocků pro možnost volby
            pygame.draw.rect(okno, (0, 255, 0), (easy[0], easy[1], velikost_blocku, velikost_blocku))
            pygame.draw.rect(okno, (255, 255, 0), (medium[0], medium[1], velikost_blocku, velikost_blocku))
            pygame.draw.rect(okno, (255, 0, 0), (hard[0], hard[1], velikost_blocku, velikost_blocku))
            pygame.draw.rect(okno, (0, 255, 255), (skore[0], skore[1], velikost_blocku, velikost_blocku))#Block pro volbu zobrazení nejvyššího dosaženého skóre
            pygame.draw.rect(okno, (5, 110, 80), (popis[0], popis[1], velikost_blocku, velikost_blocku))
            #Vykreslení defaultních popisků blocků
            info = "Nápověda"
            info = font_mensi.render(info, True, (255, 255, 255))
            okno.blit(info, (popis[0] - 40, popis[1] + 30))
            info = "Nejvyšší skóre"
            info = font_mensi.render(info, True, (255, 255, 255))
            okno.blit(info, (skore[0] - 64, skore[1] + 30))
            #Kontrola kolize hada s blockem reprezentujícím obtížnost
            if pozice_hada[0] == easy:#[0] je block hlavy hada a jeho pozice, neboli (1, 20) třeba. Pokud se rovná s pozicí jídla, tak se podmínka vykoná
                obtiznost = obtiznosti[0]
                break
            elif pozice_hada[0] == medium:#[0] je block hlavy hada a jeho pozice, neboli (1, 20) třeba. Pokud se rovná s pozicí jídla, tak se podmínka vykoná
                obtiznost = obtiznosti[1]
                break
            elif pozice_hada[0] == hard:#[0] je block hlavy hada a jeho pozice, neboli (1, 20) třeba. Pokud se rovná s pozicí jídla, tak se podmínka vykoná
                obtiznost = obtiznosti[2]
                break
            elif pozice_hada[0] == skore:
                if round(time.time() - timeout, 2) > 0.3:#Pokud hráč aktivuje možnost vykreslení skóre, na 0,3s se block stane nefunkčním, aby se zabránilo nechtěnému aktivování(jednodušeji řečeno, jedná se o odezvu)
                    zobraz_skore = True
                    timeout = time.time()
            elif pozice_hada[0] == popis:
                if round(time.time() - cekej, 2) > 0.3:#Pokud hráč aktivuje možnost nápovědy, na 0,3s se block stane nefunkčním, aby se zabránilo nechtěnému aktivování(jednodušeji řečeno, jedná se o odezvu)
                    cekej = time.time()
                    if pomoc == False:
                        pomoc = True
                    else:
                        pomoc = False
                else:
                    cekej = time.time()
        else:#Menu >>skóre<<
            #Vykreslení možnosti resetování hodnot skóre
            info = "Reset hodnot"
            info = font_mensi.render(info, True, (255, 255, 255))
            okno.blit(info, (reset[0] + 30, reset[1]))
            pygame.draw.rect(okno, (255, 0, 0), (reset[0], reset[1], velikost_blocku, velikost_blocku))
            #vykreslení možnosti exitu
            info = "Exit"
            info = font_mensi.render(info, True, (255, 255, 255))
            okno.blit(info, (skore[0] - 15, skore[1] + 30))
            if round(time.time() - timeout, 2) > 0.3: #Opět odezva
                pygame.draw.rect(okno, (0, 255, 255), (skore[0], skore[1], velikost_blocku, velikost_blocku))
                if pozice_hada[0] == skore: #kontrola kolize hlavy hada s blockem exitu, který je na stejné pozici jako block pro vstup do menu samotného
                    zobraz_skore = False
                    timeout = time.time()
                if pozice_hada[0] == reset: #Vynulování hodnot skóre
                    with open(f"{soubor_skóre}", "w", encoding="utf-8") as file: 
                        file.write("1;0\n2;0\n3;0")
            #Získávání hodnot skóre
            hodnoty = []
            try:
                with open(f"{soubor_skóre}", "r", encoding="utf-8") as file:
                    radky = file.readlines()
                    for i in range(3):
                        try:
                            hodnoty.append(radky[i].split(";")[1].strip())
                        except IndexError:
                            hodnoty.append("0")
            except FileNotFoundError:
                hodnoty = ["0", "0", "0"]
            #Vypsání hodnot skóre na obrazovku  
            for i in range(3):
                hodnota = f"{obtiznosti[i]} : {hodnoty[i]}"
                hodnota = font_mensi.render(hodnota, True, (255, 255, 255))
                okno.blit(hodnota, (50, (výška_okna // 8) * (2 + i)))
                box = Rect(25, (výška_okna // 8) * (2 + i) - 11, 160, 45)
                pygame.draw.rect(okno, (255, 0, 0), box, 2, 3)

        
        if cas > 1 / fps:#logika fps
            aktualizuj = True
            start = time.time()
            stisk = 0
        if konec_hry == False:
            if aktualizuj == True:
                neměnit_směr = False
                #Posunutí hada o jeden block směrem, kterým hledí
                aktualizuj = False
                pozice_hada = pozice_hada[-1:] + pozice_hada[:-1]
                if směr == 1:
                    pozice_hada[0][0] = pozice_hada[1][0]
                    pozice_hada[0][1] = pozice_hada[1][1] - velikost_blocku
                elif směr == 3:
                    pozice_hada[0][0] = pozice_hada[1][0]
                    pozice_hada[0][1] = pozice_hada[1][1] + velikost_blocku
                elif směr == 2:
                    pozice_hada[0][1] = pozice_hada[1][1]
                    pozice_hada[0][0] = pozice_hada[1][0] + velikost_blocku
                elif směr == 4:
                    pozice_hada[0][1] = pozice_hada[1][1]
                    pozice_hada[0][0] = pozice_hada[1][0] - velikost_blocku
                konec_hry = funkce.kontrola_konce_hry(konec_hry, pozice_hada,šířka_okna,výška_okna,velikost_blocku)
        else:
            neměnit_směr = True
            #Efekt, umožňující průchozí strany okna
            if pozice_hada[0][0] > šířka_okna + velikost_blocku * 3:
                pozice_hada = [[0, pozice_hada[0][1]]]
                pozice_hada.append([0 - velikost_blocku, pozice_hada[0][1]])
                pozice_hada.append([0 -velikost_blocku * 2, pozice_hada[0][1]])
                pozice_hada.append([0 - velikost_blocku * 3, pozice_hada[0][1]])
            if pozice_hada[0][0] < 0 - velikost_blocku * 3:
                pozice_hada = [[šířka_okna, pozice_hada[0][1]]]
                pozice_hada.append([šířka_okna + velikost_blocku, pozice_hada[0][1]])
                pozice_hada.append([šířka_okna + velikost_blocku * 2, pozice_hada[0][1]])
                pozice_hada.append([šířka_okna + velikost_blocku * 3, pozice_hada[0][1]])
            if pozice_hada[0][1] > výška_okna + velikost_blocku * 3:
                pozice_hada = [[pozice_hada[0][0], 0]]
                pozice_hada.append([pozice_hada[0][0], 0 - velikost_blocku])
                pozice_hada.append([pozice_hada[0][0], 0 - velikost_blocku * 2])
                pozice_hada.append([pozice_hada[0][0], 0 - velikost_blocku * 3])
            if pozice_hada[0][1] < 0 - velikost_blocku * 3:
                pozice_hada = [[pozice_hada[0][0], výška_okna]]
                pozice_hada.append([pozice_hada[0][0], výška_okna + velikost_blocku])
                pozice_hada.append([pozice_hada[0][0], výška_okna + velikost_blocku * 2])
                pozice_hada.append([pozice_hada[0][0], výška_okna + velikost_blocku * 3])
            konec_hry = False
        hlava = 1#Proměnná, která nám zajistí, že podmínka ve for loopu níže bude splněna pouze jednou, pro získání jiné barvy pro block představující hlavu
        if konec_hry == False or prohra == 0:
            for x in pozice_hada:
                if hlava == 0:#Ostatní blocky mimo hlavu, neboli tělo
                    pygame.draw.rect(okno, outline, (x[0], x[1], velikost_blocku, velikost_blocku))#Vykreslení větší blocku pod menší block, pro získání efektu stínu/obrysu
                    pygame.draw.rect(okno, body_inner, (x[0] + 1, x[1] + 1, velikost_blocku - 2, velikost_blocku - 2))#Vykreslení menšího blocku na větší block, pro uplatnění efektu
                if hlava == 1:#Podmínka za celý for loop proběhne jednou
                    pygame.draw.rect(okno, outline, (x[0], x[1], velikost_blocku, velikost_blocku))#Vykreslení větší blocku pod menší block, pro získání efektu stínu/obrysu
                    pygame.draw.rect(okno, modra, (x[0] + 1, x[1] + 1, velikost_blocku - 2, velikost_blocku - 2))#Vykreslení menšího blocku na větší block, pro uplatnění efektu
                    hlava = 0
        #update displaye
        pygame.display.update()
    return obtiznost, pozice_hada, směr