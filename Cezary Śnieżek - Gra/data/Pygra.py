import pygame
import sys
import time
import random
gamemode = "1"
pygame.init()
FPS = 15
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
Rozmiar_okna_x = 800
Rozmiar_okna_y = 600
tło = pygame.image.load("Plansza.png")
jabko = pygame.image.load("jabłko.png")
diament =  pygame.image.load("diament.png")
kamień = pygame.image.load("kamień.png")
gwiazda = pygame.image.load("gwiazda.png")
Boss = pygame.image.load("Boss.png")
weak = pygame.image.load("weak.png")
info = pygame.image.load("info.png")
om = pygame.mixer.Sound("omnomnom.wav")
hit = pygame.mixer.Sound("Hit.wav")
victory = pygame.mixer.Sound("Victory.wav")
Berserk_my_brother = pygame.mixer.Sound("Berserk 2016 - My Brother Extended.wav")
wonszrzeczny = pygame.mixer.Sound("wonsz_rzeczny.wav")
gameDisplay = pygame.display.set_mode((Rozmiar_okna_x, Rozmiar_okna_y))
pygame.display.set_caption("Wonsz")
icon = pygame.image.load("wonsz.png")
pygame.display.set_icon(icon)
pygame.display.update()
r_wonsza = 10
image = pygame.image.load("wonsz_głowa.png")
image_t = pygame.image.load("wonsz_t.png")
image_z = pygame.image.load("wonsz_z.png")
image_o = pygame.image.load("ogon.png")
image_1 = pygame.image.load("wengosz_głowa.png")
image_t_1 = pygame.image.load("wengosz_t.png")
image_z_1 = pygame.image.load("wengosz_z.png")
image_o_1 = pygame.image.load("ogon_wengorza.png")
clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 25) #... , rozmiar czcionki
def power_up(tab):
    if tab[2] == 1:
        gameDisplay.blit(diament, (tab[0], tab[1]))
    elif tab[2] == 2:
        gameDisplay.blit(kamień, (tab[0], tab[1]))
    elif tab[2] ==3:
        gameDisplay.blit(gwiazda, (tab[0], tab[1]))
def wypis_na_ekran(txt, kolor, X, Y):
    text = font.render(str(txt), True, kolor)
    gameDisplay.blit(text, [X, Y])
def wonysz(r_wonsza, lista_wonsza, kierunek, im_a, im_b, im_c, im_d):
    if kierunek == "G":
        głowa = im_a
    elif kierunek == "D":
        głowa = pygame.transform.rotate(im_a, 180)
    elif kierunek == "P":
        głowa = pygame.transform.rotate(im_a, 270)
    else:
        głowa = pygame.transform.rotate(im_a, 90)
    gameDisplay.blit(głowa, (lista_wonsza[-1][0], lista_wonsza[-1][1]))
    a=1
    if len(lista_wonsza) >= 3:
        for XY in lista_wonsza[1:-1]:
            if lista_wonsza[a][0] == lista_wonsza[a+1][0] + r_wonsza and lista_wonsza[a][1] == lista_wonsza[a+1][1] and lista_wonsza[a][0] == lista_wonsza[a-1][0] - r_wonsza and lista_wonsza[a][1] == lista_wonsza[a-1][1]:
                tułów = pygame.transform.rotate(im_b, 90)
                gameDisplay.blit(tułów, (lista_wonsza[a][0], lista_wonsza[a][1]))
            elif lista_wonsza[a][0] == lista_wonsza[a+1][0] + (-r_wonsza) and lista_wonsza[a][1] == lista_wonsza[a+1][1] and lista_wonsza[a][0] == lista_wonsza[a-1][0] + r_wonsza and lista_wonsza[a][1] == lista_wonsza[a-1][1]:
                tułów = pygame.transform.rotate(im_b, 90)
                gameDisplay.blit(tułów, (lista_wonsza[a][0], lista_wonsza[a][1]))
            elif lista_wonsza[a][0] == lista_wonsza[a+1][0] and lista_wonsza[a][1] == lista_wonsza[a+1][1] + r_wonsza and lista_wonsza[a][0] == lista_wonsza[a-1][0] and lista_wonsza[a][1] == lista_wonsza[a-1][1] - r_wonsza:
                gameDisplay.blit(im_b, (lista_wonsza[a][0], lista_wonsza[a][1]))
            elif lista_wonsza[a][0] == lista_wonsza[a+1][0] and lista_wonsza[a][1] == lista_wonsza[a+1][1] - r_wonsza and lista_wonsza[a][0] == lista_wonsza[a-1][0] and lista_wonsza[a][1] == lista_wonsza[a-1][1] + r_wonsza:
                gameDisplay.blit(im_b, (lista_wonsza[a][0], lista_wonsza[a][1]))

            elif lista_wonsza[a][0] == lista_wonsza[a+1][0] + r_wonsza and lista_wonsza[a][1] == lista_wonsza[a+1][1] and lista_wonsza[a][0] == lista_wonsza[a-1][0] and lista_wonsza[a][1] == lista_wonsza[a-1][1] - r_wonsza:
                obrót = pygame.transform.rotate(im_c, 0)
                gameDisplay.blit(obrót, (lista_wonsza[a][0], lista_wonsza[a][1]))
            elif lista_wonsza[a][0] == lista_wonsza[a+1][0] + r_wonsza and lista_wonsza[a][1] == lista_wonsza[a+1][1] and lista_wonsza[a][0] == lista_wonsza[a-1][0] and lista_wonsza[a][1] == lista_wonsza[a-1][1] + r_wonsza:
                obrót = pygame.transform.rotate(im_c, 270)
                gameDisplay.blit(obrót, (lista_wonsza[a][0], lista_wonsza[a][1]))
            elif lista_wonsza[a][0] == lista_wonsza[a+1][0] - r_wonsza and lista_wonsza[a][1] == lista_wonsza[a+1][1] and lista_wonsza[a][0] == lista_wonsza[a-1][0] and lista_wonsza[a][1] == lista_wonsza[a-1][1] - r_wonsza:
                obrót = pygame.transform.rotate(im_c, 90)
                gameDisplay.blit(obrót, (lista_wonsza[a][0], lista_wonsza[a][1]))
            elif lista_wonsza[a][0] == lista_wonsza[a+1][0] - r_wonsza and lista_wonsza[a][1] == lista_wonsza[a+1][1] and lista_wonsza[a][0] == lista_wonsza[a-1][0] and lista_wonsza[a][1] == lista_wonsza[a-1][1] + r_wonsza:
                obrót = pygame.transform.rotate(im_c, 180) ###########
                gameDisplay.blit(obrót, (lista_wonsza[a][0], lista_wonsza[a][1]))
            elif lista_wonsza[a][0] == lista_wonsza[a+1][0] and lista_wonsza[a][1] == lista_wonsza[a+1][1] - r_wonsza and lista_wonsza[a][0] == lista_wonsza[a-1][0] - r_wonsza and lista_wonsza[a][1] == lista_wonsza[a-1][1]:
                obrót = pygame.transform.rotate(im_c, 90)
                gameDisplay.blit(obrót, (lista_wonsza[a][0], lista_wonsza[a][1]))
            elif lista_wonsza[a][0] == lista_wonsza[a+1][0] and lista_wonsza[a][1] == lista_wonsza[a+1][1] - r_wonsza and lista_wonsza[a][0] == lista_wonsza[a-1][0] + r_wonsza and lista_wonsza[a][1] == lista_wonsza[a-1][1]:
                obrót = pygame.transform.rotate(im_c, 0)
                gameDisplay.blit(obrót, (lista_wonsza[a][0], lista_wonsza[a][1]))
            elif lista_wonsza[a][0] == lista_wonsza[a+1][0] and lista_wonsza[a][1] == lista_wonsza[a+1][1] + r_wonsza and lista_wonsza[a][0] == lista_wonsza[a-1][0] - r_wonsza and lista_wonsza[a][1] == lista_wonsza[a-1][1]:
                obrót = pygame.transform.rotate(im_c, 180)
                gameDisplay.blit(obrót, (lista_wonsza[a][0], lista_wonsza[a][1]))
            elif lista_wonsza[a][0] == lista_wonsza[a+1][0] and lista_wonsza[a][1] == lista_wonsza[a+1][1] + r_wonsza and lista_wonsza[a][0] == lista_wonsza[a-1][0] + r_wonsza and lista_wonsza[a][1] == lista_wonsza[a-1][1]:
                obrót = pygame.transform.rotate(im_c, 270)   ###########
                gameDisplay.blit(obrót, (lista_wonsza[a][0], lista_wonsza[a][1]))
            a+=1
    if len(lista_wonsza) >= 2:
        if lista_wonsza[0][0] == lista_wonsza[1][0] + r_wonsza and lista_wonsza[0][1] == lista_wonsza[1][1]:
            ogon = pygame.transform.rotate(im_d, 90)
        elif lista_wonsza[0][0] == lista_wonsza[1][0] - r_wonsza and lista_wonsza[0][1] == lista_wonsza[1][1]:
            ogon = pygame.transform.rotate(im_d, 270)
        elif lista_wonsza[0][0] == lista_wonsza[1][0] and lista_wonsza[0][1] == lista_wonsza[1][1] + r_wonsza:
            ogon = im_d
        else:
            ogon = pygame.transform.rotate(im_d, 180)
        gameDisplay.blit(ogon, (lista_wonsza[0][0], lista_wonsza[0][1]))
def gra( Rozmiar_okna_x, Rozmiar_okna_y, FPS, r_wonsza, gamemode):
    wonszrzeczny.play(50)
    czoło_x_1 = Rozmiar_okna_x/2
    zmiana_x_1 = 0
    czoło_y_1 = Rozmiar_okna_y/2
    zmiana_y_1 = 0
    dł_wonsza_1 = 1
    lista_wonsza_1 = []
    powerup = [-10, -10, 1]
    zegar = time.clock()
    boss = 1
    Skor_1 = 0
    Skor_2 = 0
    boss_weak_point_x = - 50
    boss_weak_point_y = - 50
    ruch_1 = 0
    boss_zmiana_x = 0
    boss_zmiana_y = 0
    kierunek_1 = "G"
    boss_x = -50
    boss_y = -50
    Jab_X = round(random.randint(10, Rozmiar_okna_x - r_wonsza)/10.0)*10
    Jab_y = round(random.randint(10, Rozmiar_okna_y - r_wonsza)/10.0)*10
    gameExit = False
    if gamemode == "2_v" or gamemode == "2_c":
        czoło_x_2 = Rozmiar_okna_x/2 + 50
        zmiana_x_2 = 0
        czoło_y_2 = Rozmiar_okna_y/2 + 50
        zmiana_y_2 = 0
        dł_wonsza_2 = 1
        lista_wonsza_2 = []
        powerup = [-10, -10, 1]
        kierunek_2 = "G"
        ruch_2 = 0

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ruch_1 -= 1
                elif event.key == pygame.K_RIGHT:
                    ruch_1 += 1

            if gamemode == "2_v" or gamemode == "2_c":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        ruch_2 -= 1
                    elif event.key == pygame.K_d:
                        ruch_2 += 1

        if czoło_x_1 >= Rozmiar_okna_x - 10 or czoło_x_1 < 10 or czoło_y_1 >= Rozmiar_okna_y - 10 or czoło_y_1 < 10:
            hit.play()
            gameExit = True
        if gamemode == "2_v" or gamemode == "2_c":
            if czoło_x_2 >= Rozmiar_okna_x - 10 or czoło_x_2 < 10 or czoło_y_2 >= Rozmiar_okna_y - 10 or czoło_y_2 < 10:
                hit.play()
                gameExit = True
        if Jab_X == czoło_x_1 and Jab_y == czoło_y_1:
            Jab_X = round(random.randint(10, Rozmiar_okna_x - r_wonsza - 30)/10.0)*10
            Jab_y = round(random.randint(10, Rozmiar_okna_y - r_wonsza - 30)/10.0)*10
            dł_wonsza_1 += 2
            Skor_1 += 15*round(FPS/5.0)
            om.play()
            a = random.randint(1,10)
            if a <= 4:
                b = random.randint(1,3)
                if b == 1:
                    powerup[0] = round(random.randint(10, Rozmiar_okna_x - r_wonsza - 10)/10.0)*10
                    powerup[1] = round(random.randint(10, Rozmiar_okna_y - r_wonsza - 10)/10.0)*10
                    powerup[2] = 1
                elif b == 2:
                    powerup[0] = round(random.randint(10, Rozmiar_okna_x - r_wonsza - 10)/10.0)*10
                    powerup[1] = round(random.randint(10, Rozmiar_okna_y - r_wonsza - 10)/10.0)*10
                    powerup[2] = 2
                elif b == 3:
                    powerup[0] = round(random.randint(10, Rozmiar_okna_x - r_wonsza - 10)/10.0)*10
                    powerup[1] = round(random.randint(10, Rozmiar_okna_y - r_wonsza - 10)/10.0)*10
                    powerup[2] = 3
        if gamemode == "2_v" or gamemode == "2_c":
            if Jab_X == czoło_x_2 and Jab_y == czoło_y_2:
                Jab_X = round(random.randint(10, Rozmiar_okna_x - r_wonsza - 10)/10.0)*10
                Jab_y = round(random.randint(10, Rozmiar_okna_y - r_wonsza - 10)/10.0)*10
                dł_wonsza_2 += 2
                Skor_2 += 15*round(FPS/5.0)
                om.play()
                a = random.randint(1,10)
                if a <= 4:
                    b = random.randint(1,3)
                    if b == 1:
                        powerup[0] = round(random.randint(10, Rozmiar_okna_x - r_wonsza - 10)/10.0)*10
                        powerup[1] = round(random.randint(10, Rozmiar_okna_y - r_wonsza) - 10/10.0)*10
                        powerup[2] = 1
                    elif b == 2:
                        powerup[0] = round(random.randint(10, Rozmiar_okna_x - r_wonsza - 10)/10.0)*10
                        powerup[1] = round(random.randint(10, Rozmiar_okna_y - r_wonsza - 10)/10.0)*10
                        powerup[2] = 2
                    elif b == 3:
                        powerup[0] = round(random.randint(10, Rozmiar_okna_x - r_wonsza - 10)/10.0)*10
                        powerup[1] = round(random.randint(10, Rozmiar_okna_y - r_wonsza - 10)/10.0)*10
                        powerup[2] = 3
        if czoło_x_1 == powerup[0] and czoło_y_1 == powerup[1]:
            om.play()
            if powerup[2] == 1:
                Skor_1 += 50*round(FPS/5.0)
                dł_wonsza_1 +=1
                powerup[0] = -10
                powerup[1] = -10
            elif powerup[2] == 2:
                Skor_1 += 100*round(FPS/5.0)
                dł_wonsza_1 +=10
                powerup[0] = -10
                powerup[1] = -10
            elif powerup[2] == 3:
                Skor_1 += 15*round(FPS/5.0)
                dł_wonsza_1 -=5
                powerup[0] = -10
                powerup[1] = -10
        if gamemode == "2_v" or gamemode == "2_c":
            if czoło_x_2 == powerup[0] and czoło_y_2 == powerup[1]:
                om.play()
                if powerup[2] == 1:
                    Skor_2 += 50*round(FPS/5.0)
                    dł_wonsza_2 +=1
                    powerup[0] = -10
                    powerup[1] = -10
                elif powerup[2] == 2:
                    Skor_2 += 100*round(FPS/5.0)
                    dł_wonsza_2 +=10
                    powerup[0] = -10
                    powerup[1] = -10
                elif powerup[2] == 3:
                    Skor_2 += 15*round(FPS/5.0)
                    dł_wonsza_2 -=5
                    powerup[0] = -10
                    powerup[1] = -10

        if ruch_1%4 == 0:
            zmiana_y_1 = -10
            zmiana_x_1 = 0
            kierunek_1 = "G"
        elif ruch_1%4 == 1:
            zmiana_x_1 = 10
            zmiana_y_1 = 0
            kierunek_1 = "P"
        elif ruch_1%4 == 2:
            zmiana_y_1 = 10
            zmiana_x_1 = 0
            kierunek_1 = "D"
        elif ruch_1%4 == 3:
            zmiana_x_1 = -10
            zmiana_y_1 = 0
            kierunek_1 = "L"
        czoło_x_1 +=zmiana_x_1
        czoło_y_1 +=zmiana_y_1
        gameDisplay.blit(tło, (0, 0))
        gameDisplay.blit(jabko, (Jab_X, Jab_y))
        power_up(powerup)
        głowa_1 = []
        głowa_1.append(czoło_x_1)
        głowa_1.append(czoło_y_1)
        lista_wonsza_1.append(głowa_1)
        if gamemode == "2_v" or gamemode == "2_c":
            if ruch_2%4 == 0:
                zmiana_y_2 = -10
                zmiana_x_2 = 0
                kierunek_2 = "G"
            elif ruch_2%4 == 1:
                zmiana_x_2 = 10
                zmiana_y_2 = 0
                kierunek_2 = "P"
            elif ruch_2%4 == 2:
                zmiana_y_2 = 10
                zmiana_x_2 = 0
                kierunek_2 = "D"
            elif ruch_2%4 == 3:
                zmiana_x_2 = -10
                zmiana_y_2 = 0
                kierunek_2 = "L"
            czoło_x_2 +=zmiana_x_2
            czoło_y_2 +=zmiana_y_2
            głowa_2 = []
            głowa_2.append(czoło_x_2)
            głowa_2.append(czoło_y_2)
            lista_wonsza_2.append(głowa_2)
        if len(lista_wonsza_1) > dł_wonsza_1:
            del lista_wonsza_1[0]
        for cokolwiek in lista_wonsza_1[:-1]:
            if cokolwiek == głowa_1:
                hit.play()
                gameExit = True
        if gamemode == "2_v" or gamemode == "2_c":
            if len(lista_wonsza_2) > dł_wonsza_2:
                del lista_wonsza_2[0]
            for cokolwiek in lista_wonsza_2[:-1]:
                if cokolwiek == głowa_2:
                    hit.play()
                    gameExit = True
        if gamemode == "2_v":
            for cokolwiek in lista_wonsza_1[:-1]:
                if cokolwiek == głowa_2:
                    hit.play()
                    gameExit = True
            for cokolwiek in lista_wonsza_2[:-1]:
                if cokolwiek == głowa_1:
                    hit.play()
                    gameExit = True
        if (Skor_1 > 1000 or Skor_2 > 1000) and boss == 1:
            pygame.mixer.stop()
            hit.play(3)
            boss_x = 50
            boss_y = 50
            boss = 2
            time.sleep(2)
            Berserk_my_brother.play()
        elif boss == 2 or boss == 3 or boss == 4:
            gameDisplay.blit(Boss, (boss_x, boss_y))
            gameDisplay.blit(weak, (boss_weak_point_x, boss_weak_point_y))
            if (time.clock() - zegar) >= 4:
                zegar = time.clock()
                boss_weak_point_x = round(random.randint(10, Rozmiar_okna_x - r_wonsza - 10)/10.0)*10
                boss_weak_point_y = round(random.randint(10, Rozmiar_okna_y - r_wonsza - 10)/10.0)*10
            if czoło_x_1 >= boss_x and czoło_x_1 < boss_x + 40 and czoło_y_1 >= boss_y and czoło_y_1 < boss_y + 40:
                hit.play()
                gameExit = True
            if gamemode == "2_v" or gamemode == "2_c":
                if czoło_x_2 >= boss_x and czoło_x_2 < boss_x + 40 and czoło_y_2 >= boss_y and czoło_y_2 < boss_y + 40:
                    hit.play()
                    gameExit = True
            if czoło_x_1 == boss_weak_point_x and czoło_y_1 == boss_weak_point_y:
                boss += 1
                Skor_1 += 100
                boss_weak_point_x = round(random.randint(10, Rozmiar_okna_x - r_wonsza - 10)/10.0)*10
                boss_weak_point_y = round(random.randint(10, Rozmiar_okna_y - r_wonsza - 10)/10.0)*10
                om.play()
            if gamemode == "2_v" or gamemode == "2_c":
                if czoło_x_2 == boss_weak_point_x and czoło_y_2 == boss_weak_point_y:
                    boss += 1
                    Skor_2 += 100
                    boss_weak_point_x = round(random.randint(10, Rozmiar_okna_x - r_wonsza - 10)/10.0)*10
                    boss_weak_point_y = round(random.randint(10, Rozmiar_okna_y - r_wonsza - 10)/10.0)*10
                    om.play()
            if boss_x <= 50:
                boss_zmiana_x = 15
            elif boss_x >= 750:
                boss_zmiana_x = -15
            if boss_y <= 50:
                boss_zmiana_y = 15
            elif boss_y >= 550:
                boss_zmiana_y = -15
            boss_x += boss_zmiana_x
            boss_y += boss_zmiana_y
        elif boss == 5:
            Skor_1 += 1000
            if gamemode == "2_v" or gamemode == "2_c":
                Skor_2 += 1000
            pygame.mixer.stop()
            victory.play()
            wypis_na_ekran("!!Pokonałeś Bossa!!", black, Rozmiar_okna_x/2 - 100, Rozmiar_okna_y/2 - 20)
            pygame.display.update()
            time.sleep(14)
            gameDisplay.blit(tło, (0, 0))
            gameExit = True
        wonysz(r_wonsza, lista_wonsza_1, kierunek_1, image, image_t, image_z, image_o)
        if gamemode == "2_v" or gamemode == "2_c":
            wonysz(r_wonsza, lista_wonsza_2, kierunek_2, image_1, image_t_1, image_z_1, image_o_1)
        wypis_na_ekran("Zdobyte punkty Wonsza: "+str(Skor_1), black, 10,0)
        if gamemode == "2_v" or gamemode == "2_c":
            wypis_na_ekran("Zdobyte punkty Wengorza: "+str(Skor_2), black, 400,0)
        pygame.display.update()
        clock.tick(FPS)

    if boss != 5:
        wypis_na_ekran("Przegrałeś", black, Rozmiar_okna_x/2 - 100, Rozmiar_okna_y/2 - 20)
        wypis_na_ekran("Zdobyte punkty Wonsz:" + str(Skor_1), black, Rozmiar_okna_x/2 - 160, Rozmiar_okna_y/2 +20)
    if gamemode == "2_v" or gamemode == "2_c":
        wypis_na_ekran("Zdobyte punkty Wengorz:" + str(Skor_2), black, Rozmiar_okna_x/2 - 160, Rozmiar_okna_y/2 + 50)
    pygame.display.update()
    if Skor_1 >= Skor_2 and Skor_1 >= int(text):
        open('hajskor.txt', 'w').write(str(Skor_1))
    elif Skor_1 <= Skor_2 and Skor_2 >= int(text):
        open('hajskor.txt', 'w').write(str(Skor_2))
    time.sleep(2)
    pygame.mixer.stop()
    gameExit = True
    if event.type == pygame.KEYDOWN:
        if event.type == pygame.QUIT:
            gameExit = True
            pygame.quit()
            quit()
text = open('hajskor.txt').read()
i="a"

while i != "q":
    pygame.mixer.stop()
    clock.tick(30)
    text = open('hajskor.txt').read()
    x, y = pygame.mouse.get_pos()
    gameDisplay.blit(tło, (0, 0))
    wypis_na_ekran("Info", black, 0, 0)
    wypis_na_ekran("Rozpocznij grę", black, Rozmiar_okna_x/2 - 160, Rozmiar_okna_y/2 - 40)
    wypis_na_ekran("Wybierz poziom trudności", black, Rozmiar_okna_x/2 - 220, Rozmiar_okna_y/2)
    wypis_na_ekran("Wyjdź", black, Rozmiar_okna_x/2 - 110, Rozmiar_okna_y/2 + 30)
    wypis_na_ekran("Highscore: " + str(text), black, 10, 40)
    wypis_na_ekran("Muzyka: " , black, 10, 70)
    wypis_na_ekran("Musics8Bits" , black, 10, 100)
    wypis_na_ekran("Shiro Sagisu" , black, 10, 130)
    if x >= Rozmiar_okna_x/2 - 160 and x <= Rozmiar_okna_x/2 + 10 and y >= Rozmiar_okna_y/2 - 40 and y <= Rozmiar_okna_y/2 - 10:
        wypis_na_ekran("Rozpocznij grę", red, Rozmiar_okna_x/2 - 160, Rozmiar_okna_y/2 - 40)
    elif x >= Rozmiar_okna_x/2 - 220 and x <= Rozmiar_okna_x/2 + 80 and y >= Rozmiar_okna_y/2 and y <= Rozmiar_okna_y/2 + 30:
        wypis_na_ekran("Wybierz poziom trudności", red, Rozmiar_okna_x/2 - 220, Rozmiar_okna_y/2)
    elif x >= Rozmiar_okna_x/2 - 110 and x <= Rozmiar_okna_x/2 - 10 and y >= Rozmiar_okna_y/2 + 30 and y <= Rozmiar_okna_y/2 + 60:
        wypis_na_ekran("Wyjdź", red, Rozmiar_okna_x/2 - 110, Rozmiar_okna_y/2 + 30)
    elif x >= 0 and x <= 70 and y >= 0 and y <= 30:
        wypis_na_ekran("Info", red, 0, 0)
    pygame.display.update()
    for event in pygame.event.get():
        i = "a"
        if event.type == pygame.QUIT:
            i = "q"
            pygame.quit()
            quit()
            break
        if x >= Rozmiar_okna_x/2 - 160 and x <= Rozmiar_okna_x/2 + 10 and y >= Rozmiar_okna_y/2 - 40 and y <= Rozmiar_okna_y/2 - 10 and event.type == pygame.MOUSEBUTTONDOWN:

            while i != "r":
                gameDisplay.blit(tło, (0, 0))
                x, y = pygame.mouse.get_pos()
                wypis_na_ekran("Solo", black, Rozmiar_okna_x/2 - 80, Rozmiar_okna_y/2 - 70)
                wypis_na_ekran("Versus", black, Rozmiar_okna_x/2 - 105, Rozmiar_okna_y/2 - 45)
                wypis_na_ekran("Kooperacja", black, Rozmiar_okna_x/2 - 105, Rozmiar_okna_y/2 - 20)
                wypis_na_ekran("Powrót", black, Rozmiar_okna_x/2 - 90, Rozmiar_okna_y/2 + 5)
                x, y = pygame.mouse.get_pos()
                if x >= Rozmiar_okna_x/2 - 80 and x <= Rozmiar_okna_x/2 + 10 and y >= Rozmiar_okna_y/2 - 70 and y <= Rozmiar_okna_y/2 - 40:
                    wypis_na_ekran("Solo", red, Rozmiar_okna_x/2 - 80, Rozmiar_okna_y/2 - 70)
                elif x >= Rozmiar_okna_x/2 - 105 and x <= Rozmiar_okna_x/2 + 10 and y >= Rozmiar_okna_y/2 - 40 and y <= Rozmiar_okna_y/2 - 10:
                    wypis_na_ekran("Versus", red, Rozmiar_okna_x/2 - 105, Rozmiar_okna_y/2 - 45)
                elif x >= Rozmiar_okna_x/2 - 105 and x <= Rozmiar_okna_x/2 + 30 and y >= Rozmiar_okna_y/2 - 10 and y <= Rozmiar_okna_y/2 + 20:
                    wypis_na_ekran("Kooperacja", red, Rozmiar_okna_x/2 - 105, Rozmiar_okna_y/2 - 20)
                elif x >= Rozmiar_okna_x/2 - 160 and x <= Rozmiar_okna_x/2 + 10 and y >= Rozmiar_okna_y/2 +20 and y <= Rozmiar_okna_y/2 + 50:
                    wypis_na_ekran("Powrót", red, Rozmiar_okna_x/2 - 90, Rozmiar_okna_y/2 + 5)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = "r"
                        pygame.quit()
                        quit()
                    if x >= Rozmiar_okna_x/2 - 80 and x <= Rozmiar_okna_x/2 + 10 and y >= Rozmiar_okna_y/2 - 70 and y <= Rozmiar_okna_y/2 - 40 and event.type == pygame.MOUSEBUTTONDOWN:
                        gamemode = "1"
                        gra( Rozmiar_okna_x, Rozmiar_okna_y, FPS, r_wonsza, gamemode)
                        i = "r"
                        break
                    elif x >= Rozmiar_okna_x/2 - 105 and x <= Rozmiar_okna_x/2 + 10 and y >= Rozmiar_okna_y/2 - 40 and y <= Rozmiar_okna_y/2 - 10 and event.type == pygame.MOUSEBUTTONDOWN:
                        gamemode = "2_v"
                        gra( Rozmiar_okna_x, Rozmiar_okna_y, FPS, r_wonsza, gamemode)
                        i = "r"
                        break
                    elif x >= Rozmiar_okna_x/2 - 105 and x <= Rozmiar_okna_x/2 + 30 and y >= Rozmiar_okna_y/2 - 10 and y <= Rozmiar_okna_y/2 + 20 and event.type == pygame.MOUSEBUTTONDOWN:
                        gamemode = "2_c"
                        gra( Rozmiar_okna_x, Rozmiar_okna_y, FPS, r_wonsza, gamemode)
                        i = "r"
                        break
                    elif x >= Rozmiar_okna_x/2 - 160 and x <= Rozmiar_okna_x/2 + 10 and y >= Rozmiar_okna_y/2 +20 and y <= Rozmiar_okna_y/2 + 50 and event.type == pygame.MOUSEBUTTONDOWN:
                        i ="r"
                        break

        elif x >= Rozmiar_okna_x/2 - 220 and x <= Rozmiar_okna_x/2 + 80 and y >= Rozmiar_okna_y/2 and y <= Rozmiar_okna_y/2 + 30 and event.type == pygame.MOUSEBUTTONDOWN:

            while i!= "s":
                gameDisplay.blit(tło, (0, 0))
                x, y = pygame.mouse.get_pos()
                wypis_na_ekran("łatwy", black, Rozmiar_okna_x/2 + 10, Rozmiar_okna_y/2 - 70)
                wypis_na_ekran("średni", black, Rozmiar_okna_x/2 + 5, Rozmiar_okna_y/2 - 45)
                wypis_na_ekran("trudny", black, Rozmiar_okna_x/2 + 5, Rozmiar_okna_y/2 - 20)
                wypis_na_ekran("bardzo trudny", black, Rozmiar_okna_x/2 - 40, Rozmiar_okna_y/2 + 5)
                wypis_na_ekran("Bóg Wonsza", black, Rozmiar_okna_x/2 - 17, Rozmiar_okna_y/2 + 30)
                wypis_na_ekran("Powrót", black, Rozmiar_okna_x/2 + 20, Rozmiar_okna_y/2 + 55)
                if x >= Rozmiar_okna_x/2 + 10 and x <= Rozmiar_okna_x/2 + 100 and y >= Rozmiar_okna_y/2 - 70 and y <= Rozmiar_okna_y/2 - 40:
                    wypis_na_ekran("łatwy", red, Rozmiar_okna_x/2 + 10, Rozmiar_okna_y/2 - 70)
                elif x >= Rozmiar_okna_x/2 + 5 and x <= Rozmiar_okna_x/2 + 100 and y >= Rozmiar_okna_y/2 - 40 and y <= Rozmiar_okna_y/2 - 10:
                    wypis_na_ekran("średni", red, Rozmiar_okna_x/2 + 5, Rozmiar_okna_y/2 - 45)
                elif x >= Rozmiar_okna_x/2 + 5 and x <= Rozmiar_okna_x/2 + 90 and y >= Rozmiar_okna_y/2 - 10 and y <= Rozmiar_okna_y/2 + 20:
                    wypis_na_ekran("trudny", red, Rozmiar_okna_x/2 + 5, Rozmiar_okna_y/2 - 20)
                elif x >= Rozmiar_okna_x/2 - 40 and x <= Rozmiar_okna_x/2 + 200 and y >= Rozmiar_okna_y/2 +20 and y <= Rozmiar_okna_y/2 + 50:
                    wypis_na_ekran("bardzo trudny", red, Rozmiar_okna_x/2 - 40, Rozmiar_okna_y/2 + 5)
                elif x >= Rozmiar_okna_x/2 - 17 and x <= Rozmiar_okna_x/2 + 200 and y >= Rozmiar_okna_y/2 +50 and y <= Rozmiar_okna_y/2 + 70:
                    wypis_na_ekran("Bóg Wonsza", red, Rozmiar_okna_x/2 + - 17, Rozmiar_okna_y/2 + 30)
                elif x >= Rozmiar_okna_x/2 + 20 and x <= Rozmiar_okna_x/2 + 150 and y >= Rozmiar_okna_y/2 +70 and y <= Rozmiar_okna_y/2 + 100:
                    wypis_na_ekran("Powrót", red, Rozmiar_okna_x/2 + 20, Rozmiar_okna_y/2 + 55)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = "r"
                        pygame.quit()
                        quit()
                    if x >= Rozmiar_okna_x/2 + 10 and x <= Rozmiar_okna_x/2 + 100 and y >= Rozmiar_okna_y/2 - 70 and y <= Rozmiar_okna_y/2 - 40 and event.type == pygame.MOUSEBUTTONDOWN:
                        FPS = 10
                        i ="s"

                    elif x >= Rozmiar_okna_x/2 + 5 and x <= Rozmiar_okna_x/2 + 100 and y >= Rozmiar_okna_y/2 - 40 and y <= Rozmiar_okna_y/2 - 10 and event.type == pygame.MOUSEBUTTONDOWN:
                        FPS = 15
                        i ="s"

                    elif x >= Rozmiar_okna_x/2 + 5 and x <= Rozmiar_okna_x/2 + 100 and y >= Rozmiar_okna_y/2 - 10 and y <= Rozmiar_okna_y/2 + 20 and event.type == pygame.MOUSEBUTTONDOWN:
                        FPS = 25
                        i ="s"

                    elif x >= Rozmiar_okna_x/2 - 40 and x <= Rozmiar_okna_x/2 + 200 and y >= Rozmiar_okna_y/2 +20 and y <= Rozmiar_okna_y/2 + 50 and event.type == pygame.MOUSEBUTTONDOWN:
                        FPS = 35
                        i ="s"

                    elif x >= Rozmiar_okna_x/2 - 17 and x <= Rozmiar_okna_x/2 + 160 and y >= Rozmiar_okna_y/2 +50 and y <= Rozmiar_okna_y/2 + 80 and event.type == pygame.MOUSEBUTTONDOWN:
                        FPS = 50
                        i ="s"

                    elif x >= Rozmiar_okna_x/2 + 20 and x <= Rozmiar_okna_x/2 + 150 and y >= Rozmiar_okna_y/2 +80 and y <= Rozmiar_okna_y/2 + 110 and event.type == pygame.MOUSEBUTTONDOWN:
                        i ="s"
        elif x >= 0 and x <= 70 and y >= 0 and y <= 30 and event.type == pygame.MOUSEBUTTONDOWN:
            gameDisplay.blit(tło, (0, 0))
            gameDisplay.blit(info, (0, 0))
            pygame.display.update()
            time.sleep(10)
        if x >= Rozmiar_okna_x/2 - 110 and x <= Rozmiar_okna_x/2 - 10 and y >= Rozmiar_okna_y/2 + 30 and y <= Rozmiar_okna_y/2 + 60 and event.type == pygame.MOUSEBUTTONDOWN:
            i = "q"
            pygame.quit()
            quit()
    clock.tick(5)
pygame.quit()
quit()
