import pygame
from pygame.locals import *
from packages import okno_volby
from packages import funkce
import time
import mysql.connector
import getpass
#Získání uživatelského jména pro srozumitelnější ukládání hodnot skóre jednotlivých uživatelů
user = getpass.getuser()
#Hodnoty pro napojení se na databázi
host = "<uri>"
username = "<username>"
password = "<passwd>"
database = "<db>"
#Samotné napojení se na databázi
mydb = mysql.connector.connect(
    host = host
    ,user = username
    ,password = password
    ,database = database
)
mycursor = mydb.cursor()
#Kontrola Existence Table Score
nove_hodnoty = False
try:
    mycursor.execute(f"""SELECT * FROM `Score`""")
    myresult = mycursor.fetchall() 
except mysql.connector.errors.ProgrammingError: 
    mycursor.execute("""CREATE TABLE `Score`(
        username text,
        Easy int,
        Medium int,
        Hard int
    )""")
    mydb.commit()
#Kontrola Existence Hodnot pro aktuálního uživatele
try:
    mycursor.execute(f"""SELECT * FROM `Score` WHERE username = '{user}'""")
    myresult = mycursor.fetchall()
    if myresult == []:
        nove_hodnoty = True
except mysql.connector.errors.ProgrammingError: 
    nove_hodnoty = True
if nove_hodnoty == True:#Vytvoření nových hodnot
    mycursor.execute(f"""INSERT INTO `Score`
(username, Easy, Medium, Hard) VALUES
('{user}', 0, 0, 0);
""")
    mydb.commit()
#inicializace
pygame.init()
#Okno
šířka_okna = 600
výška_okna = 600
okno = pygame.display.set_mode((šířka_okna, výška_okna))
pygame.display.set_caption("Had")
#Proměnné
sloupce = ["Easy", "Medium", "Hard"]#Názvy sloupců, které se nacházející se v databázi pod těmito názvy reprezentující obtížnosti  
kliknuto = False
fps = 10
run = True
prohra = 0
stisk = 0
obtiznosti = ["Snadná", "Střední", "Obtížná"]
aktualizuj = False
velikost_blocku = 20#pixely na jednen block ve hře
směr = 1#1 je nahoru, 2 vpravo, 3 dolu a 4 vlevo
score = 0
konec_hry = False
run = True
prohra = 0
stisk = 0
start = time.time()
tlačítko = Rect(šířka_okna // 2 - 90, výška_okna // 2, 180, 45)
#Snake
pozice_hada = [[int(šířka_okna / 2), int(výška_okna / 2)]]#list pozic blocků + přidání prvního blocku
pozice_hada.append([int(šířka_okna / 2), int(výška_okna / 2) + velikost_blocku])#Druhý block
pozice_hada.append([int(šířka_okna / 2), int(výška_okna / 2) + velikost_blocku * 2])#Třetí block
pozice_hada.append([int(šířka_okna / 2), int(výška_okna / 2) + velikost_blocku * 3])#Čtvrtý block
#jídlo
jidlo = [0, 0]
nove_jidlo = True
prodlouzeny_block = [0, 0]
#font
font = pygame.font.SysFont(None, 40)
font_mensi = pygame.font.SysFont(None, 33)
#Barvy
bg = (0, 0, 0)
body_inner = (255, 255, 255)
outline = (100, 100, 200)
modra = (0, 0, 255)
#Volba obtížnosti
obtiznost, pozice_hada, směr = okno_volby.choice(šířka_okna,výška_okna,velikost_blocku,okno,bg,font,font_mensi,fps,outline,modra,body_inner,obtiznosti,mycursor,mydb,user,sloupce,host,username,password,database)
#Zahájení odpočtu času
start = time.time()
#Začátek hry
while run:
    cas = round(time.time() - start, 2)#Výpočet času pro správnou funkci fps
    funkce.vykreslení_okna(okno,bg)
    funkce.vykreslení_score(score,obtiznosti,okno,obtiznost,font,šířka_okna)
    funkce.vykreslení_obtížnosti(obtiznost,font,okno,šířka_okna,výška_okna,obtiznosti)
    #Kontrola událostí provedených uživatelem
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and stisk == 0:
            if event.key == pygame.K_w and směr != 3:#Pokud stiskneme W a proměnná směr není 3, což by znamenalo že had se pohybuje směrem dolu, tak se změní proměnná směr na 1, což znamená, že pojede nahoru
                směr = 1
            if event.key == pygame.K_d and směr != 4:#Pokud stiskneme D a proměnná směr není 4, což by znamenalo že had se pohybuje směrem doleva, tak se změní proměnná směr na 2, což znamená, že pojede doprava
                směr = 2
            if event.key == pygame.K_s and směr != 1:#Pokud stiskneme S a proměnná směr není 1, což by znamenalo že had se pohybuje směrem nahoru, tak se změní proměnná směr na 1, což znamená, že pojede dolu
                směr = 3
            if event.key == pygame.K_a and směr != 2:#Pokud stiskneme A a proměnná směr není 2, což by znamenalo že had se pohybuje směrem doprava, tak se změní proměnná směr na 1, což znamená, že pojede doleva
                směr = 4
            stisk += 1
    #tvorba jídla
    if nove_jidlo == True:
        nove_jidlo = False
        jidlo = funkce.vytvoření_jídla(obtiznost,obtiznosti,velikost_blocku,šířka_okna,výška_okna,jidlo,okno)
    jidlo.vykresli()
    #Kolize s jídlem
    if jidlo.kolize(pozice_hada):
        nove_jidlo = True
        #Prodloužení hada
        prodlouzeny_block = list(pozice_hada[-1])
        if směr == 1:
            prodlouzeny_block[1] += velikost_blocku#Pokud se had pohybuje nahoru, prodlouží se o velikost velikost_blocku na y souřadnici, což reprezentuje jeden block
        elif směr == 3:
            prodlouzeny_block[1] -= velikost_blocku#Pokud se had pohybuje dolu, zmenší se o velikost velikost_blocku na y souřadnici, což reprezentuje jeden block
        elif směr == 2:
            prodlouzeny_block[0] -= velikost_blocku#Pokud se had pohybuje doleva, zmenší se o velikost velikost_blocku na x souřadnici, což reprezentuje jeden block
        if směr == 4:
            prodlouzeny_block[0] += velikost_blocku#Pokud se had pohybuje doprava, zvětší se o velikost velikost_blocku na x souřadnici, což reprezentuje jeden block
        #Připojení blocku za sebrání jídla k hadovi
        pozice_hada.append(prodlouzeny_block)
        score += 1 #Přidání score
    #Logika fps
    if cas > 1 / fps:
        aktualizuj = True
        start = time.time()
        stisk = 0
    if konec_hry == False:
        if aktualizuj == True:
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
            konec_hry = funkce.kontrola_konce_hry(konec_hry, pozice_hada,výška_okna,šířka_okna, velikost_blocku)
    else:
        prohra += 1
        if prohra == 1:
            pygame.time.delay(2000)
            změna = funkce.zápis_score(score,obtiznosti,obtiznost,mycursor,mydb,user,sloupce)
        okno.fill((0, 0, 0))
        funkce.vykresleni_konce_hry(font,okno,šířka_okna,výška_okna,změna,tlačítko,font_mensi)
        funkce.vykreslení_score(score,obtiznosti,okno,obtiznost,font,šířka_okna)
        
        if event.type == pygame.MOUSEBUTTONDOWN and kliknuto == False:#Kliknutní
            kliknuto = True
        if event.type == pygame.MOUSEBUTTONUP and kliknuto == True:#Upuštění
            kliknuto = False
        #Jen pro kontrolu, jestli uživatel skutečně kliknul, a nedrží jen tlačítko myši
            pos = pygame.mouse.get_pos()
            if tlačítko.collidepoint(pos):
                #Restart Proměnných
                pozice_hada = [[int(šířka_okna / 2), int(výška_okna / 2)]]
                pozice_hada.append([int(šířka_okna / 2), int(výška_okna / 2) + velikost_blocku])
                pozice_hada.append([int(šířka_okna / 2), int(výška_okna / 2) + velikost_blocku * 2])
                pozice_hada.append([int(šířka_okna / 2), int(výška_okna / 2) + velikost_blocku * 3])
                směr = 1
                aktualizuj = False
                jidlo = [0, 0]
                nove_jidlo = True
                prodlouzeny_block = [0, 0]
                score = 0
                stisk = 0
                prohra = 0
                konec_hry = False
                obtiznost, pozice_hada, směr = okno_volby.choice(šířka_okna,výška_okna,velikost_blocku,okno,bg,font,font_mensi,fps,outline,modra,body_inner,obtiznosti,mycursor,mydb,user,sloupce,host,username,password,database)
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
pygame.quit()
mycursor.close()
mydb.close()
