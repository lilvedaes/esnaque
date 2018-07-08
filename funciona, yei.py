import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1200, 700))
screen.fill((0,0,0))
done = False
permiso = True
pressed = pygame.key.get_pressed()

#x = random.randint(10, 1100)
#y = random.randint(10, 800)

#decalracion de variables
x1 = 100
y1 = 130

x2 = 1070
y2 = 630

turnos = 9

#COLORES
verde = (0, 230, 0)
azul = (0, 102, 255)
morado = (153, 0, 204)
amarillo = (255, 255, 0)
rosado = (255, 0, 102)
blanco = (255, 255, 255)
negro = (0,0,0)

start = True
menu1 = False
menu2 = False

#start menu

while (start == True):
    screen.fill(verde)
    startfont = pygame.font.SysFont("monospace", 100)
    frase = startfont.render("ESNAQUE", 1, negro)
    buttonfont = pygame.font.SysFont("Arial", 50)
    sbutton = buttonfont.render("Press to Start", 1, negro)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            frase = startfont.render("ESNAQUE", 1, negro)
            start = False
            menu1 = True

    screen.blit(frase, (400, 300))
    screen.blit(sbutton, (500, 400))
    pygame.display.flip()


#color pick menu

while (menu1==True):
    screen.fill(negro)
    myfont = pygame.font.SysFont("monospace", 60)
    nlabel = myfont.render("Player one, pick your color:", 1, blanco)
    #draw rectangles
    botverde = pygame.draw.rect(screen, verde, pygame.Rect(300, 150, 150, 150))
    botazul = pygame.draw.rect(screen, azul, pygame.Rect(300, 320, 150, 150))
    botmorado = pygame.draw.rect(screen, morado, pygame.Rect(300, 490, 150, 150))

    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            if (300 <= pos[0] <= 450) and (150 <= pos[1] <= 300):
                color1 = verde
            elif (300 <= pos[0] <= 450) and (320 <= pos[1] <= 470):
                color1 = azul
            elif (300 <= pos[0] <= 450) and (490 <= pos[1] <= 640):
                color1 = morado
            else:
                color1 = negro
            nlabel = myfont.render("Player one, pick your color:", 1, negro)
            menu1 = False
            menu2 = True
    screen.blit(nlabel, (30, 20))
    pygame.display.flip()

while (menu2 == True):
    screen.fill(negro)
    myfont = pygame.font.SysFont("monospace", 60)
    nlabel = myfont.render("Player two, pick your color:", 1, blanco)
    #rectangulitos
    botamarillo = pygame.draw.rect(screen, amarillo, pygame.Rect(600, 150, 150, 150))
    botrosado = pygame.draw.rect(screen, rosado, pygame.Rect(600, 320, 150, 150))
    botblanco = pygame.draw.rect(screen, blanco, pygame.Rect(600, 490, 150, 150))

    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            posi = pygame.mouse.get_pos()
            print(posi)
            if (600 <= posi[0] <= 750) and (150 <= posi[1] <= 300):
                color2 = amarillo
            elif (600 <= posi[0] <= 750) and (320 <= posi[1] <= 470):
                color2 = rosado
            elif (600 <= posi[0] <= 750) and (490 <= posi[1] <= 640):
                color2 = blanco
            else:
                color2= negro
            nlabel = myfont.render("Player two, pick your color:", 1, negro)
            menu2 = False
    screen.blit(nlabel, (30, 20))
    pygame.display.flip()

screen.fill(negro)

#clase del jugador
class player:
    def __init__(self, name, color, x, y, up, down, left, right):
        self.paxright = False
        self.paxleft = False
        self.paydown = False
        self.payup = False
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def coordenadas(self):
        #print("coord")
        if pressed[self.up]:
            self.paxright = False
            self.paxleft = False
            self.paydown = False
            self.payup = True
            print("up")

        if pressed[self.down]:
            self.paxright = False
            self.paxleft = False
            self.paydown = True
            self.payup = False

            print("down")

        if pressed[self.left]:
            self.paxright = False
            self.paxleft = True
            self.paydown = False
            self.payup = False
            print("left")

        if pressed[self.right]:
            self.paxright = True
            self.paxleft = False
            self.paydown = False
            self.payup = False
            print("right")

        global x1
        global x2
        global y1
        global y2

        if self.paxright == True: self.x += 3
        if self.paxleft == True: self.x -= 3
        if self.paydown == True: self.y += 3
        if self.payup == True: self.y -= 3

    def draw(self):
        pygame.draw.circle(screen, self.color, [self.x, self.y], 15)

#creacion de objetos
# pal verde
player1 = player("one", color1, x1, y1, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

# pal azul
player2 = player("two", color2, x2, y2, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)

if color1 == negro or color2 == negro:
    fooont = pygame.font.SysFont("monospace", 30)
    fooont1 = fooont.render("Elegiste negro, ahora juega con negro", 1, blanco)
    fooont2 = fooont.render("Ahora solo te queda \"cerrar\" el juego :)", 1, blanco)
    fooont3 = fooont.render("#Antibugs", 1, blanco)
    screen.blit(fooont1, (300, 300))
    screen.blit(fooont2, (300, 400))
    screen.blit(fooont3, (300, 500))
    pygame.display.flip()
    permiso = False
    while permiso == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Para cerrar al presionar la equis roja
                permiso = True


#while game is running
while not done and permiso:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Para cerrar al presionar la equis roja
            done = True
    if turnos == -1:
        screen.fill(verde)
        endfont = pygame.font.SysFont("monospace", 100)
        endlabel = endfont.render("GAME OVER", 1, blanco)
        screen.blit(endlabel, (300, 300))
        pygame.display.flip()
        time.sleep(3)
        done = True

    pressed = pygame.key.get_pressed()

    #actualiza las frames
    screen.fill(negro)

    #dibuja rectangulos de arriba
    pygame.draw.rect(screen,(255, 102, 102), pygame.Rect(0,0,1200,70)) #rectangulo de scores y turnos

    #corre la funcion de coordenadas
    player1.coordenadas()
    player2.coordenadas()

    #corre la funcion de dibujar
    player1.draw()
    player2.draw()

#colision
    #escribe turnos
    turnfont = pygame.font.SysFont("monospace", 30)
    turn = turnfont.render("Turnos restantes: "+str(turnos), 1, blanco)
    screen.blit(turn, (30, 20))
    #colsion en si
    if abs(player2.x-player1.x)<30  and abs(player2.y - player1.y) < 30:
        turnos -= 1

        time.sleep(1)

        screen.fill(negro)

        player1.x = 130
        player1.y = 100

        player2.x = 1070
        player1.y = 630

#para que no choquen la pared
    if player1.x < 20: player1.x = 20
    if player2.x < 20: player2.x = 20

    if player1.y < 90: player1.y = 90
    if player2.y < 90: player2.y = 90

    if player1.x > 1180 : player1.x = 1180    #Le restas el ancho del rectangulo, la coordenada se evalua desde la esquina superior izquierda
    if player2.x > 1180 : player2.x = 1180

    if player1.y > 683 : player1.y = 683
    if player2.y > 683 : player2.y = 683

    pygame.display.update()