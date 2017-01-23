from Entity import *
from EnemiesPaths import *
from ImageControl import *
import random
import pygame

class Enemy(Entity):

    def __init__(self, name, enemy, images, position, sound, inverted, resize):
        Entity.__init__(self, name, images, inverted, resize)
        super().setActualImage(position)

        self.object = enemy
        self.sound = sound
        self.checkIfMoves()
        self.checkIfRotates()
        self.checkIfAnime()
        self.contact = self.object['contact']
        if self.moves:
            self.definingMove()
        if self.rotates:
            self.definingRotation()
        if self.animes:
            self.definingAnimation()
        self.constant = 60
        self.oneRepeat = False
        self.die = False

    def definingMove(self):
        self.path, self.move_step = EnemiesPaths.getEnemyPath(self.object["path"])
        self.speed = self.object['movespeed']
        self.ipath = 0
        self.moved = [0, 0]

    def definingRotation(self):
        self.angles = self.object["rotation"]
        self.angle = int(random.uniform(0, self.object["rotation"][0] - 1))
        self.angledirection = self.object["rotationdirection"]
        self.max_angle = self.object["rotation"]
        self.rotationSpeed = self.object["rotationspeed"]
        self.angleKey = 0

    def definingAnimation(self):
        self.animationTime = self.object["animationTime"]
        self.frame = 0

    def checkIfMoves(self):
        if 'movespeed' in self.object.keys():
            self.moves = True
        else:
            self.moves = False

    def checkIfAnime(self):
        if 'animationTime' in self.object.keys():
            self.animes = True
        else:
            self.animes = False

    def checkIfRotates(self):
        if 'rotation' in self.object.keys():
            self.rotates = True
        else:
            self.rotates = False

    def action(self, fps):
        if self.rotates:
            self.rotate(fps)
        if self.moves:
            self.move(fps)
        if self.animes:
            self.animate()

    def animate(self):
        self.frame += 1
        if self.frame > self.animationTime[self.imgIndex]:
            if self.oneRepeat and self.index == len(self.images[self.imgIndex]) - 1:
                self.die = True
            self.frame = 0
            self.changeImage()

    def collision(self, object):
        if len(self.contact) > 1:
            if self.contact[0] == "slow":
                object.speed -= object.speed * self.contact[1]
            elif self.contact[0] == "buff" and self.imgIndex == 0:
                object.air += self.contact[1]
                object.aux_air += self.contact[1]
                self.imgIndex += 1
                self.index = 0
                self.sound.playSound("pop")
                self.oneRepeat = True
            elif self.contact[0] == "jump" and self.imgIndex == 0:
                object.physics.bubbleJump(self.contact[1])
                self.imgIndex += 1
                self.index = 0
                self.sound.playSound("pop")
                self.oneRepeat = True
            elif self.contact[0] == "life":
                object.life += self.contact[1]
                self.sound.playSound("pop")
                self.die = True
        elif self.contact[0] == "die":
            object.isDead = True
        elif self.contact[0] == "checkpoint":
            object.definingCheckpoint((self.rect.x, self.rect.y))
            print("morreu")
            self.die = True

    def move(self, fps):
        if self.path[self.ipath][0] == self.moved[0] and self.path[self.ipath][1] == self.moved[1]:
            self.ipath = (self.ipath + 1) % len(self.path)
        else:
            self.moved[0] += self.move_step[self.ipath][0]
            self.moved[1] += self.move_step[self.ipath][1]
            self.rect.x += int(self.move_step[self.ipath][0] * self.speed /fps*self.constant)
            self.rect.y += int(self.move_step[self.ipath][1] * self.speed/fps*self.constant)

    def rotate(self, fps):
        if self.max_angle[self.angleKey] > 0:
            if self.angle > self.max_angle[self.angleKey]:
                self.angleKey = (self.angleKey + 1) % len(self.angles)
            else:
                self.angle += self.angledirection[self.angleKey] /fps* self.constant * self.rotationSpeed[self.angleKey]
        else:
            if self.angle < self.max_angle[self.angleKey]:
                self.angleKey = (self.angleKey + 1) % len(self.angles)
            else:
                self.angle += self.angledirection[self.angleKey] /fps * self.constant * self.rotationSpeed[self.angleKey]
