
import pygame
import random
import time
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 700))
screen.fill((0,0,0))
done = False
permiso = True
pressed = pygame.key.get_pressed()

historiadoble = []

pygame.display.set_caption('Esnaque')

c = 1

score1 = 0
score2 = 0


#x = random.randint(10, 1100)
#y = random.randint(10, 800)

#decalracion de variables
x1 = 100
y1 = 130

x2 = 1070
y2 = 630

turnos = 2
bulletspeed = 3

randfoodx = random.randint(300, 800)
randfoody = random.randint(300, 500)

#COLORES
verde = (0, 230, 0,255)
azul = (0, 102, 255,255)
morado = (153, 0, 204,255)
amarillo = (255, 255, 0,255)
rosado = (255, 0, 102,255)
blanco = (255, 255, 255,255)
negro = (0,0,0,255)
rojo = (255,0,0,255)

speed = 4

start = True
menu1 = False
menu2 = False

timer = 0
temp = 0

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
    def __init__(self, name, color, x, y, up, down, left, right, shoot):
        self.paxright = False
        self.paxleft = False
        self.paydown = False
        self.payup = False
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.coord = (x,y)
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.shoot = shoot
        self.body = []
        self.esnaquelargo = 1
        self.timer = 0
        self.bullet = False
        self.bx = 0
        self.by = 0
        self.bulletdirection = False
        self.direction = False
        self.hit = False

    def coordenadas(self):
        #print("coord")
        if pressed[self.up]:
            self.paxright = False
            self.paxleft = False
            self.paydown = False
            self.payup = True
            self.direction = "up"

        if pressed[self.down]:
            self.paxright = False
            self.paxleft = False
            self.paydown = True
            self.payup = False
            self.direction = "down"

        if pressed[self.left]:
            self.paxright = False
            self.paxleft = True
            self.paydown = False
            self.payup = False
            self.direction = "left"

        if pressed[self.right]:
            self.paxright = True
            self.paxleft = False
            self.paydown = False
            self.payup = False
            self.direction = "right"


        if self.paxright == True: self.x += speed
        if self.paxleft == True: self.x -= speed
        if self.paydown == True: self.y += speed
        if self.payup == True: self.y -= speed



        global c
        if c<3:
            self.body.append(self.coord)
            c = c+1

        self.coord = (self.x, self.y)

        if self.body[-1] != (self.coord):
            self.body.append(self.coord) #historial de coordenadas
        #self.esnaquebody.append(self.body)


    def draw(self):
        pygame.draw.circle(screen, self.color, (self.coord), 15)
        if self.hit == True:
            time.sleep(0.1)
            if self == player1:
                self.color = color1
            elif self == player2:
                self.color = color2
            self.hit = False

    def esnaquegrow(self):
        global largoesnaque
        global historiadoble
        if self.hit == True:
            self.color = negro

        for xy in self.body[:-2]:
            pygame.draw.circle(screen, self.color, xy, 15)
            if len(self.body) > self.esnaquelargo:
                self.body.pop(0)
            historiadoble = historiadoble + self.body
            if self.coord in self.body[:-1]:
                colision(self)
                break
            elif self.coord in historiadoble[:-2]:
                colision(self)
                break

            historiadoble = []

    def shootfun(self):
        if pressed[self.shoot]:
            global blanco
            self.bullet = True
            self.bx = self.x
            self.by = self.y
            # self.timer +=1
            # if self.timer == 50:
            #   self.timer = 0
            self.bulletdirection = self.direction
            pygame.draw.rect(screen, blanco, pygame.Rect(self.bx, self.by, 5, 5))

        if self.bullet == True:
            global bulletspeed
            if self.bulletdirection == "right": self.bx += bulletspeed
            if self.bulletdirection == "left": self.bx -= bulletspeed
            if self.bulletdirection == "down": self.by += bulletspeed
            if self.bulletdirection == "up": self.by -= bulletspeed
            pygame.draw.rect(screen, blanco, pygame.Rect(self.bx, self.by, 5, 5))


            if screen.get_at((self.bx+6,self.by+6)) == other(self).color:
                global temp
                global timer
                self.bullet = False
                other(self).esnaquelargo -= 10
                temp = other(self).color
                other(self).color = negro
                timer += 1
                if timer >20:
                    timer = 0
                    other(self).color = temp

            if self.esnaquelargo < 1:
                colision(self)

            if self.bx < 20 or self.bx > 1180: self.bullet = False
            if self.by < 90 or self.by > 683: self.bullet = False

def other(self):
    if self == player1:
        return player2
    elif self == player2:
        return player1

def food(self):
    global randfoody
    global randfoodx
    if abs(randfoodx-self.x)<20 and abs(randfoody-self.y)<20:
        randfoodx = random.randint(20, 1000)
        randfoody = random.randint(90, 680)
        self.esnaquelargo += 10
    pygame.draw.circle(screen, rojo, (randfoodx, randfoody), 10)

def colision(perdedor):
    global turnos
    global c
    global player1
    global player2
    global historiadoble

    global score1
    global score2

    if perdedor == player2:
        score1 += 1
    elif perdedor == player1:
        score2 += 1

    turnos -= 1
    time.sleep(1)
    screen.fill(negro)
    # reiniciar todo
    """
    self.body = []
    historiadoble = []
    c = 0
    player1.x = 130
    player1.y = 100
    player2.x = 1070
    player2.y = 630
    self.paxright = False
    self.paxleft = False
    self.paydown = False
    self.payup = False
    """
    player1 = player("one", color1, x1, y1, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_v)
    player2 = player("two", color2, x2, y2, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE)
    historiadoble = []
    c = 0

def chocarpared(self):
    if self.x < 20 or  self.x > 1180:
        colision(self)
    if self.y < 90 or self.y > 683: colision(self) #Le restas el ancho del rectangulo, la coordenada se evalua desde la esquina superior izq


#creacion de objetos
# pal verde
player1 = player("one", color1, x1, y1, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_v)

# pal azul
player2 = player("two", color2, x2, y2, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE)

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
            sys.exit()
    if turnos < 0:
        screen.fill(verde)
        endfont = pygame.font.SysFont("monospace", 100)
        winnerfont = pygame.font.SysFont("monospace", 70)
        endlabel = endfont.render("GAME OVER", 1, blanco)
        if score1>score2:
            winnerlabel = winnerfont.render("Player 1 won",1, blanco)
        if score2>score1:
            winnerlabel = winnerfont.render("Player 2 won",1, blanco)
        if score1==score2:
            winnerlabel = winnerfont.render("You both won",1, blanco)
        screen.blit(endlabel, (300, 300))
        screen.blit(winnerlabel, (310, 500))
        pygame.display.flip()
        time.sleep(3)
        done = True

    pressed = pygame.key.get_pressed()

    #actualiza las frames
    screen.fill(negro)

    #dibuja rectangulos de arriba
    pygame.draw.rect(screen,(255, 102, 102), pygame.Rect(0,0,1200,70)) #rectangulo de scores y turnos

    food(player1)
    food(player2)

    #corre la funcion de coordenadas
    player1.coordenadas()
    player2.coordenadas()

    #corre la funcion de dibujar
    player1.esnaquegrow()
    player2.esnaquegrow()

    player1.draw()
    player2.draw()

    player1.shootfun()
    player2.shootfun()

    #escribe turnos
    turnfont = pygame.font.SysFont("monospace", 30)
    turn = turnfont.render("Turnos restantes: "+str(turnos), 1, blanco)
    scoreplayer1 = turnfont.render("Score player 1: " + str(score1), 1, blanco)
    scoreplayer2 = turnfont.render("Score player 2: " + str(score2), 1, blanco)
    screen.blit(turn, (30, 20))
    screen.blit(scoreplayer1, (700, 7))
    screen.blit(scoreplayer2, (700, 36))

    # colision entre si
    if abs(player2.x - player1.x) < 30 and abs(player2.y - player1.y) < 30:
        colision(None)
        colision(None)

    chocarpared(player1)
    chocarpared(player2)


#para que no choquen la pared


    pygame.display.update()