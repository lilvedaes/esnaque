import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1200, 700))
screen.fill((0,0,0))
done = False

#x = random.randint(10, 1100)
#y = random.randint(10, 800)

x1 = 100
y1 = 100

x2 = 100
y2= 500

def checkCollision(sprite1, sprite2):
    col = pygame.sprite.collide_rect(sprite1, sprite2)
    if col == True:
        sys.exit()



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #Para cerrar al presionar la equis roja
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:    #Para imprimir coordenada al hacer click
            pos = pygame.mouse.get_pos()
            print(pos)


    screen.fill((0, 0, 0))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y1 -= 3
    if pressed[pygame.K_DOWN] and not pressed[pygame.K_LEFT] and not pressed[pygame.K_RIGHT]: y1 += 3
    if pressed[pygame.K_LEFT]: x1 -= 3
    if pressed[pygame.K_RIGHT]: x1 += 3




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