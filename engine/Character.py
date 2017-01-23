import pygame

import sys
from ImageControl import *
from Physics import *
from Point import *
from Entity import *
from Animation import *


class Character(Entity):

    def __init__(self, control, sound):

        Entity.__init__(self)
        self.direction = 1
        self.sound = sound
        self.defaultspeed = 10
        self.speed = self.defaultspeed
        self.char_speed = 5
        self.defineShipSize(80, 49)
        self.onfloor = False
        self.control = control


        self.inShip = True
        self.loadLifes()
        self.isDead = False
        self.physics = None
        self.life = 3
        self.air = 0
        self.aux_air = 0
        self.constantSpeed = 30
        self.definingMovespeed(60)
        self.loadShipImages()
        self.max = 0
        self.order = 1
        self.frameOrder = 1
        self.frameShipAnimation = [3, 3, 3]
        self.frameAnimation = [20, 5, 10, 20, 5, 10]
        self.framecount = 0
        self.move_vector = (0, 0)

    def definingCheckpoint(self, pos):
        self.checkpoint = pos

    def definingMovespeed(self, fps):
        self.move_map = {pygame.K_LEFT: (-self.constantSpeed/fps, 0),
        pygame.K_RIGHT: (self.constantSpeed/fps, 0),
            pygame.K_UP: (0, -self.constantSpeed/fps),
            pygame.K_DOWN: (0, self.constantSpeed/fps)}

    def loadShipImages(self):
        self.shipAnimes = False
        self.images = [[pygame.image.load("../graphics/Sprites/nave" + str(i) + "-0.png").convert_alpha() for i in range(1,4)],
        [pygame.transform.flip(pygame.image.load("../graphics/Sprites/nave" + str(i) + "-0.png").convert_alpha(), True, False) for i in range(1,4)]]

        self.actualimages = [[ImageControl.fixScale(pygame.image.load("../graphics/Sprites/nave" + str(i) + "-0.png").convert_alpha())\
         for i in range(1,4)],
        [ImageControl.fixScale(pygame.transform.flip(pygame.image.load("../graphics/Sprites/nave" + str(i) + "-0.png").convert_alpha(), True, False))\
         for i in range(1,4)]]
        self.image = self.actualimages[0][0]

    def loadPlayerImages(self):
        self.defineShipSize(50, 95)
        self.defineRect()
        self.images = [
            [pygame.image.load("../graphics/Sprites/protagonista/stand" + str(i) + ".png").convert_alpha() for i in range(1, 4)],
            [pygame.image.load("../graphics/Sprites/protagonista/run" + str(i) + ".png").convert_alpha() for i in range(1, 5)],
            [pygame.image.load("../graphics/Sprites/protagonista/jump" + str(i) + ".png").convert_alpha() for i in range(1, 3)],
            [pygame.transform.flip(pygame.image.load("../graphics/Sprites/protagonista/stand" + str(i) + ".png").convert_alpha(), True, False) for i in range(1, 4)],
            [pygame.transform.flip(pygame.image.load("../graphics/Sprites/protagonista/run" + str(i) + ".png").convert_alpha(), True, False) for i in range(1, 5)],
            [pygame.transform.flip(pygame.image.load("../graphics/Sprites/protagonista/jump" + str(i) + ".png").convert_alpha(), True, False) for i in range(1, 3)]
             ]
        self.actualimages = [
            [ImageControl.fixScale(pygame.image.load("../graphics/Sprites/protagonista/stand" + str(i) + ".png").convert_alpha())
             for i in range(1, 4)],
            [ImageControl.fixScale(pygame.image.load("../graphics/Sprites/protagonista/run" + str(i) + ".png").convert_alpha())
             for i in range(1, 5)],
            [ImageControl.fixScale(pygame.image.load("../graphics/Sprites/protagonista/jump" + str(i) + ".png").convert_alpha())
             for i in range(1, 3)],
            [ImageControl.fixScale(pygame.transform.flip(pygame.image.load("../graphics/Sprites/protagonista/stand" + str(i) + ".png").convert_alpha(), True, False))
             for i in range(1, 4)],
            [ImageControl.fixScale(pygame.transform.flip(pygame.image.load("../graphics/Sprites/protagonista/run" + str(i) + ".png").convert_alpha(), True, False))
             for i in range(1, 5)],
            [ImageControl.fixScale(pygame.transform.flip(pygame.image.load("../graphics/Sprites/protagonista/jump" + str(i) + ".png").convert_alpha(), True, False))
             for i in range(1, 3)]
        ]

        self.image = self.actualimages[0][0]
        self.face = 1
        self.status = ["stand", "run", "runleft", "jumpright", "jumpleft", "fallright", "fallleft"]
        self.statusKey = 0

    def loadLifes(self):
        self.reallifeImage = pygame.image.load("../graphics/Monsters/vida/vida1.png").convert_alpha()
        self.lifeImage = ImageControl.fixScale(pygame.image.load("../graphics/Monsters/vida/vida1.png").convert_alpha())
        self.realbubbleImage = pygame.image.load("../graphics/Monsters/bolha/bolha1.png").convert_alpha()
        self.bubbleImage = ImageControl.fixScale(pygame.image.load("../graphics/Monsters/bolha/bolha1.png").convert_alpha())

    def newLevel(self, pos):
        self.defineStartPosition(pos[0], pos[1])
        self.defineRect()

    def defineShipSize(self, w, h):
        self.size = w, h

    def defineStartPosition(self, x, y):
        self.point = Point(x, y)
        self.pos = self.point.xy()

    def defineRect(self):
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def change_Direction(self):
        self.image = pygame.transform.flip(self.actualimages[0][0], True, False)

    def introControls(self):
        pressed = pygame.key.get_pressed()
        for e in pygame.event.get():
            if e.type == pygame.KEYUP and pressed[pygame.K_RETURN]:
                return True
            if e.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
                sys.exit()
        return False

    #STAGES
    def movement(self, action):
        pressed = pygame.key.get_pressed()
        if action == "space":
            self.physics.jump()
        self.move_vector = (0, 0)

        #determinando o vetor de movimento
        for m in (self.move_map[key] for key in self.move_map if pressed[key]):
            self.move_vector = list(map(sum, zip(self.move_vector, m)))
        self.rotatePlayer(self.move_vector)

        # normalize movement vector if necessary
        if sum(map(abs, self.move_vector)) == 2:
            self.move_vector = [p / 1.4142 for p in self.move_vector]

        #aplicando velocidade
        self.move_vector = [self.speed * p for p in self.move_vector]

        #atualizando posição do personagem
        self.move_vector = self.move_vector

        self.pos = list(map(sum, list(zip(self.pos, self.move_vector))))
        self.point.x = self.pos[0]
        self.point.y += self.physics.vel_y

        self.rect.topleft = (self.point.x, self.point.y)

        if pressed[pygame.K_RIGHT]:
            self.shipAnimation("right")
        elif pressed[pygame.K_LEFT]:
            self.shipAnimation("left")
        else:
            self.shipAnimation("stand")
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

        self.image = self.actualimages[self.imgIndex][self.index]

    def shipAnimation(self, side):
        if side == "right":
            if self.direction == -1 and not self.shipAnimes:
                self.direction = 1
                self.max = 0
                self.shipAnimes = True

        elif side == "left" :
            if self.direction == 1 and not self.shipAnimes:
                self.direction = -1
                self.max = 0
                self.shipAnimes = True

        if self.shipAnimes:
            self.framecount += 1
            if self.framecount == self.frameShipAnimation[self.imgIndex]:
                self.framecount = 0
                self.changeShipImage()

    def changeShipImage(self):
        self.index = (self.index + 1) % len(self.images[self.imgIndex])
        if self.index == 0:
            self.imgIndex = (self.imgIndex + 1) % 2
            self.shipAnimes = False

    #STAGE 7
    def movement_char(self, action, fps):
        pressed = pygame.key.get_pressed()
        if action == "space":
            if self.physics.jumpable is True:
                self.sound.playSound("jump")
                self.physics.jump()

        self.physics.vel_x = 0

        if pressed[pygame.K_RIGHT]:
            self.playerAnimation("right")
            self.physics.vel_x += self.char_speed / fps * 60
        elif pressed[pygame.K_LEFT]:
            self.playerAnimation("left")
            self.physics.vel_x -= self.char_speed / fps * 60
        else:
            self.playerAnimation("stand")

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

    def playerAnimation(self, move):
        auxIndex = self.imgIndex
        if move == "right":
            if self.physics.fall:
                self.imgIndex = 2
            else:
                self.imgIndex = 1
            self.direction = 1
        elif move == "left":
            if self.physics.fall:
                self.imgIndex = 5
            else:
                self.imgIndex = 4
            self.direction = -1
        elif move == "stand":
            if self.direction == 1:
                if self.physics.fall:
                    self.imgIndex = 2
                else:
                    self.imgIndex = 0
            else:
                if self.physics.fall:
                    self.imgIndex = 5
                else:
                    self.imgIndex = 3

        if auxIndex != self.imgIndex:
                self.framecount = 0
                self.frameOrder = 1
                self.index = 0

        if self.physics.fall:
            if self.index == 0:
                self.framecount += 1
                if self.framecount == self.frameAnimation[self.imgIndex]:
                    self.changePlayerImage()
                    self.framecount = 0

        else:
            self.framecount += 1
            if self.framecount == self.frameAnimation[self.imgIndex]:
                self.changePlayerImage()
                self.framecount = 0

        self.image = self.actualimages[self.imgIndex][self.index]

    def changePlayerImage(self):
        self.index += self.frameOrder

        if self.index == len(self.images[self.imgIndex]) - 1:
            self.frameOrder *= -1
        elif self.index == 0:
            self.frameOrder *= -1

    def collision(self, object):
        self.physics.get_position(self, object)

    def update(self, fps):
        self.definingMovespeed(fps)
        self.physics.update_physics(fps)
        self.rotatePlayer(self.move_vector)
        self.checkSpeed()
        self.checkIfLife()

    def checkIfLife(self):
        if self.aux_air == 10:
            self.aux_air = 0
            self.life += 1
            #self.sound.playSound()

    def checkSpeed(self):
        if self.speed < self.defaultspeed:
            self.speed += 1

    def updateWindow(self):
        try:
            self.physics.jump_power = ImageControl.defineY(self.physics.constantjump_power, True)
            self.physics.gravity = ImageControl.defineY(self.physics.constantgravity, True)
        except:
            pass

    def rotatePlayer(self, move_vector):
        # se houver movimento no x, rotaciona o player para determinado grau
        if self.inShip:
            if move_vector[0] > 0:
                if self.max > -30:
                    self.max -= 1
            elif move_vector[0] < 0:
                if self.max < 15:
                    self.max += 1
            # se nao houver movimento nox, volta ao grau 0
            elif move_vector[0] == 0:
                if (self.max > 0):
                    self.max -= 1
                elif self.max < 0:
                    self.max += 1
            self.image = pygame.transform.rotate(self.actualimages[self.imgIndex][self.index], self.max)


    def death(self):
        self.life -= 1
        self.isDead = False
        if self.life > 0:
            return "Reset"
        else:
            self.__init__(self.control, self.sound)
            return "Menu"
