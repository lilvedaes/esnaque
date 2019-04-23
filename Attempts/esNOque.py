import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1200, 700))
screen.fill((0,0,0))
done = False
pressed = pygame.key.get_pressed()


#x = random.randint(10, 1100)
#y = random.randint(10, 800)

#Pal verde
x1 = 150
y1 = 175

pax1right = False
pax1left = False
pay1down = True
pay1up = False

#Pal azul
x2 = 1050
y2= 525

pax2right = False
pax2left = False
pay2down = False
pay2up = True




while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #Para cerrar al presionar la equis roja
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:    #Para imprimir coordenada al hacer click
            pos = pygame.mouse.get_pos()
            print(pos)

        if pressed[pygame.K_UP]: pay1up  = True
        if pressed[pygame.K_DOWN]: pay1down = True
        if pressed[pygame.K_LEFT]: pax1left = True
        if pressed[pygame.K_RIGHT]: pax1right = True


    #Pal verde
    """
    if pax1right == True: x1 += 3
    elif pax1left == True: x1 -= 3
    elif pay1down == True: y1 += 3
    elif pay1up == True: y1 -= 3

    #Pal azul
    if pax2right == True: x2 += 3
    elif pax2left == True: x2 -= 3
    elif pay2down == True: y2 += 3
    elif pay2up == True: y2 -= 3
    """


    screen.fill((0, 0, 0))


    if pressed[pygame.K_w]: y2 -= 3
    if pressed[pygame.K_s]: y2 += 3
    if pressed[pygame.K_a]: x2 -= 3
    if pressed[pygame.K_d]: x2 += 3



    if x1 < 0: x1 = 0
    if x2 < 0: x2 = 0

    if y1 < 0: y1 = 0
    if y2 < 0: y2 = 0

    if x1 > 1170 : x1 = 1170    #Le restas el ancho del rectangulo, la coordenada se evalua desde la esquina superior izquierda
    if x2 > 1170 : x2 = 1170

    if y1 > 670 : y1 = 670
    if y2 > 670 : y2 = 670

    #print(x1,y1)
    #print(x2,y2)


    pygame.draw.rect(screen, (0, 102, 0), pygame.Rect(x1, y1, 30, 30))
    pygame.draw.rect(screen, (0, 102, 255), pygame.Rect(x2, y2, 30, 30))

    pygame.display.flip()