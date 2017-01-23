import pygame
from pygame import *
from stages.AbstractStage import *
from ImageControl import *
from Physics import *
from Point import *
from Enemy import *
from Camera import *
from TerrainSurface import *


class Stage1 (AbstractStage):
    def __init__(self, controller, window, sound, player, sprite, fonts, objects):
        self.sound = sound
        self.control = controller
        self.allObjects = objects

        level_dimensions = (4500, 1000)
        super().__init__(player, window, "Stage1", level_dimensions)
        self.name = "Stage1"
        self.newlevel = (50, 400)

        self.player.newLevel(self.newlevel)
        self.player.definingCheckpoint(self.newlevel)
        self.entities.add(self.player)
        self.stages = ["Intro_Bolha"]
        self.create_terrain("Stage1", 11)
        self.create_background("skin8")
        self.loadSounds()
        self.player.physics = Physics()
        self.define_enemies()

    def defineCheckPoints(self):
        self.checkpoint = [self.newlevel, ()]
        self.checkpointKey = 0


    def define_enemies(self):
        for i in range(0,8):
            self.create_enemies("rinovirus", (500 + i * 1200, 700))
            self.create_enemies("rinovirus", (300 + i * 900, 300))
            #self.create_enemies("rinovirus", (400+i*780, 600))
            self.create_enemies("rinovirus", (700+i*840, 550))
        for i in range(0,8):
            self.create_enemies("pelo", (500 + 500*i, 500))
            self.create_enemies("pelo", (750 + i*500, -300), True)


    def loadSounds(self):
        self.sound.soundStage1()

    def checkNextStagePosition(self):
        if self.player.point.xy()[0] > self.camera.dimensions[0] - 200:
            self.nextStageKey = self.stages[0]

    def update(self):
        while self.nextStageKey is "Stage1":
            super().update()
            self.checkNextStagePosition()

        if self.nextStageKey == "Reset":
            self.__init__(self.control, self.window, self.sound, self.player, None, None, self.allObjects)
        else:
            return self.nextStageKey, True, self.changeResolution
