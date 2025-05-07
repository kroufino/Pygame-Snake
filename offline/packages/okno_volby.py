import pygame
from pygame.locals import *
from packages import funkce,block
import time
import sys

def choice(šířka_okna,výška_okna,velikost_blocku,okno,bg,font,font_mensi,fps,outline,modra,body_inner,soubor_skóre,obtiznosti):
    easy_cords = [šířka_okna // 5, výška_okna // 3] #Souřadnice blocku reprezentující Easy obtížnost
    medium_cords = [šířka_okna // 2, výška_okna // 3] #Souřadnice blocku reprezentující Mid obtížnost
    hard_cords = [šířka_okna // 1.25, výška_okna // 3] #Souřadnice blocku reprezentující Hard obtížnost
    skore_cords = [4 * velikost_blocku, (výška_okna // 3) * 2 + velikost_blocku * 3] #Souřadnice blocku reprezentující vypsání dosažených hodnot skóre
    reset_cords = [šířka_okna // 1.5, (výška_okna // 3) - velikost_blocku * 3] #Souřadnice blocku reprezentující Možnost resetu hodnot skóre
    popis_cords = [šířka_okna - velikost_blocku * 4, (výška_okna // 3) * 2 + velikost_blocku * 3] #Souřadnice blocku reprezentující Popisky blocků
    easy = block.Block(easy_cords[0],easy_cords[1],(0,255,0),okno,velikost_blocku)
    medium = block.Block(medium_cords[0],medium_cords[1],(255,255,0),okno,velikost_blocku)
    hard = block.Block(hard_cords[0], hard_cords[1],(255,0,0),okno,velikost_blocku)
    skore = block.Block(skore_cords[0], skore_cords[1],(0, 255, 255),okno,velikost_blocku)
    reset = block.Block(reset_cords[0], reset_cords[1],(255, 0, 0),okno,velikost_blocku)
    popis = block.Block(popis_cords[0], popis_cords[1],(5, 110, 80),okno,velikost_blocku)
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
                sys.exit()
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
            if pomoc == True:#Pokud hráč aktivuje nápovědu, tato funkce zobrazí popis_cordsky jednotlivých blocků
                funkce.popisky(easy_cords,medium_cords,hard_cords,okno,obtiznosti,font_mensi)
            #Vykreslení blocků pro možnost volby
            easy.vykresli()
            medium.vykresli()
            hard.vykresli()
            skore.vykresli()
            popis.vykresli()
            #Vykreslení defaultních popis_cordsků blocků
            info = "Nápověda"
            info = font_mensi.render(info, True, (255, 255, 255))
            okno.blit(info, (popis_cords[0] - 40, popis_cords[1] + 30))
            info = "Nejvyšší skóre"
            info = font_mensi.render(info, True, (255, 255, 255))
            okno.blit(info, (skore_cords[0] - 64, skore_cords[1] + 30))
            #Kontrola kolize hada s blockem reprezentujícím obtížnost
            if easy.kolize(pozice_hada):
                obtiznost = obtiznosti[0]
                break
            if medium.kolize(pozice_hada):
                obtiznost = obtiznosti[1]
                break
            if hard.kolize(pozice_hada):
                obtiznost = obtiznosti[2]
                break
            if skore.kolize(pozice_hada):
                if round(time.time() - timeout, 2) > 0.3:#Pokud hráč aktivuje možnost vykreslení skóre, na 0,3s se block stane nefunkčním, aby se zabránilo nechtěnému aktivování(jednodušeji řečeno, jedná se o odezvu)
                    zobraz_skore = True
                    proběhlo = False
                    timeout = time.time()
            if popis.kolize(pozice_hada):
                if round(time.time() - cekej, 2) > 0.3:#Pokud hráč aktivuje možnost nápovědy, na 0,3s se block stane nefunkčním, aby se zabránilo nechtěnému aktivování(jednodušeji řečeno, jedná se o odezvu)
                    cekej = time.time()
                    if pomoc == False:
                        pomoc = True
                    else:
                        pomoc = False
                else:
                    cekej = time.time()
        else:#Menu >>skóre<<
            #Vykreslení možnosti reset_cordsování hodnot skóre
            info = "reset_cords hodnot"
            info = font_mensi.render(info, True, (255, 255, 255))
            reset.vykresli()
            #vykreslení možnosti exitu
            info = "Exit"
            info = font_mensi.render(info, True, (255, 255, 255))
            okno.blit(info, (skore_cords[0] - 15, skore_cords[1] + 30))
            if round(time.time() - timeout, 2) > 0.3: #Opět odezva
                skore.vykresli()
                if skore.kolize(pozice_hada): #kontrola kolize hlavy hada s blockem exitu, který je na stejné pozici jako block pro vstup do menu samotného
                    zobraz_skore = False
                    timeout = time.time()
                if reset.kolize(pozice_hada): #Vynulování hodnot skóre
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
                pocet = int(len(list(str(hodnoty[i]))))#Kontrola délky relativního prvku, aby se zamezilo nechtěným problémům
                hodnota = f"{obtiznosti[i]} : {hodnoty[i]}"
                hodnota = font_mensi.render(hodnota, True, (255, 255, 255))
                okno.blit(hodnota, (50, (výška_okna // 8) * (2 + i)))
                box = Rect(25, (výška_okna // 8) * (2 + i) - 11, 150 + pocet * 11, 45)
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