import pygame
from pygame.locals import *
import sys
def otazka(user,okno,šířka_okna,výška_okna,font_mensi,povolené_znaky):
    run = True
    kliknuto = False
    tlačítko_Ano = Rect(šířka_okna // 2 - 93, výška_okna // 2, 70, 40) #Tlačítko reprezentující volbu ano
    tlačítko_Ne = Rect(šířka_okna // 2 + 69, výška_okna // 2, 50, 40) #Tlačítko reprezentující volbu ne
    input_box = pygame.Rect(šířka_okna //2 - 90, výška_okna //2 , 180, 32) #Box pro uživatelský input
    input_box_stín = pygame.Rect(šířka_okna //2 - 90, výška_okna //2 - 1 , 182, 34) #Box pro stín uživatelského inputu
    zadany_text = ""
    zadat = False
    while run:          
        okno.fill((0,0,0))      
        #Kontrola událostí provedených uživatelem
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()   
            if event.type == pygame.MOUSEBUTTONDOWN: #Kontrola kolizí myši s tláčitky ANO/NE
                if input_box.collidepoint(event.pos): 
                    aktivní = True
                else: 
                    aktivní = False 
            if zadat == True: 
                if event.type == pygame.KEYDOWN: #Kontrola stisknutých kláves v případě nutného uživatelského inputu
                    if event.key == pygame.K_BACKSPACE: #funkce mazání textu
                        zadany_text = zadany_text[:-1] #Odebrání posledního prvku v listu obsahující uživatelský input, pro plnou funkci BACKSPACE
                    elif event.key == pygame.K_RETURN: #Enter, neboli potvrzení zadaného vstupu
                        run = False
                        user = zadany_text
                    else: 
                        if max(180, text_zobrazeno.get_width()+10) == 180: #Pokud je box nutné zdelšit, protože se do něj již nevejde uživateslký input, tak se input nepropíše
                            if event.unicode in povolené_znaky:
                                zadany_text += event.unicode

        if zadat == False: #Volba ANO/NE na dotaz 
            dotaz_text = f"Je nickname '{user}' správný"
            dotaz = font_mensi.render(dotaz_text, True, (255, 255, 255))
            okno.blit(dotaz, (šířka_okna // 2 - len(dotaz_text)*5, výška_okna // 2 - 58))
            Ano = "Ano"
            Ne = "Ne"
            Ano = font_mensi.render(Ano, True, (255, 255, 255))
            Ne = font_mensi.render(Ne, True, (255, 255, 255))
            pygame.draw.rect(okno, (255, 0, 0), tlačítko_Ano, 2, 3)
            pygame.draw.rect(okno, (255, 0, 0), tlačítko_Ne, 2, 3)
            okno.blit(Ano, (šířka_okna // 2 - 80, výška_okna // 2 + 10))
            okno.blit(Ne, (šířka_okna // 2 + 80, výška_okna // 2 + 10))
            if event.type == pygame.MOUSEBUTTONDOWN and kliknuto == False:#Kliknutní
                kliknuto = True
            if event.type == pygame.MOUSEBUTTONUP and kliknuto == True:#Upuštění
                kliknuto = False
            #Jen pro kontrolu, jestli uživatel skutečně kliknul, a nedrží jen tlačítko myši
                pos = pygame.mouse.get_pos()
                if tlačítko_Ano.collidepoint(pos):
                    run = False
                elif tlačítko_Ne.collidepoint(pos):
                    zadat = True
        else: #Zadávání volitelného nickname
            okno.fill((0,0,0))      
            postup_text = f"Zadej svůj nickname(ENTER pro potvrzení):"
            postup = font_mensi.render(postup_text, True, (255, 255, 255))
            okno.blit(postup, (šířka_okna // 2 - len(postup_text)*5, výška_okna // 2 - 58))
            info = "Povolené znaky: A-z,0-9 a mezera"
            info2 = "Povolená délka: do velikosti boxu"
            info = font_mensi.render(info, True, (255, 255, 255))
            info2 = font_mensi.render(info2, True, (255, 255, 255))
            okno.blit(info, (5, výška_okna - 60))
            okno.blit(info2, (5, výška_okna - 30))
            #Menší efekt, pro simulaci odezvy na proklik
            barva_aktivní = (1, 92, 25)
            barva_neaktivní = (2, 250, 68)
            barva = barva_neaktivní 
            if aktivní: 
                barva = barva_aktivní 
            else: 
                barva = barva_neaktivní 
            #Vykreslování
            pygame.draw.rect(okno, barva, input_box) 
            pygame.draw.rect(okno, (255,255,255), input_box_stín, 2, 3) 
            text_zobrazeno = font_mensi.render(zadany_text, True, (255, 255, 255))
            if max(180, text_zobrazeno.get_width()+10) != 180: 
                zadany_text = zadany_text[:-1] 
            okno.blit(text_zobrazeno, (input_box.x+5, input_box.y+5)) 
            pygame.display.flip() 
        pygame.display.update()
    return user