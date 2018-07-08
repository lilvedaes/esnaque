import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1200, 700))
screen.fill((0,0,0))
done = False
pressed = pygame.key.get_pressed()

#x = random.randint(10, 1100)
#y = random.randint(10, 800)

x1 = 100
y1 = 100

x2 = 1000
y2= 500

turnos = 1
"""
def checkCollision(sprite1, sprite2):
    col = pygame.sprite.collide_rect(sprite1, sprite2)
    if col == True:
        sys.exit()

        """

pax1right = False
pax1left = False
pay1down = True
pay1up = False

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



    screen.fill((0, 0, 0))
    pressed = pygame.key.get_pressed()
    # pal verde
    if pressed[pygame.K_UP]:  # and pay1down == False:
        pax1right = False
        pax1left = False
        pay1down = False
        pay1up = True

    if pressed[pygame.K_DOWN]:  # and pay1up == False:
        pax1right = False
        pax1left = False
        pay1down = True
        pay1up = False

    if pressed[pygame.K_LEFT]:  # and pax1right == False:
        pax1right = False
        pax1left = True
        pay1down = False
        pay1up = False

    if pressed[pygame.K_RIGHT]:  # and pax1left == False:
        pax1right = True
        pax1left = False
        pay1down = False
        pay1up = False
        # pal azul
    if pressed[pygame.K_w]:  # and pay1down == False:
        pax2right = False
        pax2left = False
        pay2down = False
        pay2up = True

    if pressed[pygame.K_s]:  # and pay1up == False:
        pax2right = False
        pax2left = False
        pay2down = True
        pay2up = False

    if pressed[pygame.K_a]:  # and pax1right == False:
        pax2right = False
        pax2left = True
        pay2down = False
        pay2up = False

    if pressed[pygame.K_d]:  # and pax1left == False:
        pax2right = True
        pax2left = False
        pay2down = False
        pay2up = False

    pygame.draw.rect(screen, (0, 230, 0), pygame.Rect(x1, y1, 30, 30))
    pygame.draw.rect(screen, (0, 50, 255), pygame.Rect(x2, y2, 30, 30))

    pygame.draw.rect(screen,(255, 102, 102), pygame.Rect(0,0,1200,70)) #rectangulo de scores y turnos

    if pax1right == True: x1 += 3
    if pax1left == True: x1 -= 3
    if pay1down == True: y1 += 3
    if pay1up == True: y1 -= 3


    if pay2up==True: y2 -= 3
    if pay2down==True: y2 += 3
    if pax2left==True: x2 -= 3
    if pax2right==True: x2 += 3


#colision

    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    turnfont = pygame.font.SysFont("monospace", 30)

    # render text
    turn = turnfont.render("Turno: "+str(turnos), 1, (255, 255, 255))
    screen.blit(turn, (30, 20))
    if abs(x2-x1)<30  and abs(y2 -y1) < 30:
        turnos += 1

        time.sleep(1)

        x1 = 100
        y1 = 100

        x2 = 1000
        y2 = 500

#para que no choquen la pared
    if x1 < 0: x1 = 0
    if x2 < 0: x2 = 0

    if y1 < 70: y1 = 70
    if y2 < 70: y2 = 70

    if x1 > 1170 : x1 = 1170    #Le restas el ancho del rectangulo, la coordenada se evalua desde la esquina superior izquierda
    if x2 > 1170 : x2 = 1170

    if y1 > 600 : y1 = 600
    if y2 > 600 : y2 = 600

    pygame.display.update()

