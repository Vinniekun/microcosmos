import pygame
from pygame import *
from stages.AbstractStage import *
from ImageControl import *
from Physics import *
from Point import *
from Enemy import *
from Camera import *
from TerrainSurface import *


class Stage2 (AbstractStage):
    def __init__(self, controller, window, sound, player, sprite, fonts, objects):
        self.sound = sound
        self.control = controller
        self.allObjects = objects

        level_dimensions = (4500, 1500)
        super().__init__(player, window, "Stage2", level_dimensions)
        self.name = "Stage2"
        self.newlevel = (50, 300)
        self.player.newLevel(self.newlevel)
        self.player.definingCheckpoint(self.newlevel)
        self.entities.add(self.player)
        self.stages = ["Intro_3"]
        self.create_terrain("Stage2", 11)
        self.create_background("skin10")
        self.loadSounds()
        self.player.physics = Physics()
        self.define_enemies()

    def loadSounds(self):
        self.sound.soundStage7()

    def define_enemies(self):
        for i in range(0, 8):
            self.create_enemies("bolha", (700 + i * 600, 500 + 20 * i))
            self.create_enemies("bolha", (600 + i * 500, 800 + 20 * i))
            self.create_enemies("bolha", (800 + i * 400, 1200 + 20 * i))
        for i in range(0, 8):
            self.create_enemies("pneumococo", (500 + i * 1000, 700))
            self.create_enemies("pneumococo", (300 + i * 600, 300))
            self.create_enemies("pneumococo", (400 + i * 700, 600))
            self.create_enemies("pneumococo", (700 + i * 840, 550))
            self.create_enemies("pneumococo", (1000 + i * 910, 1000))
            self.create_enemies("pneumococo", (1100 + i * 810, 1300))

    def checkNextStagePosition(self):
        if self.player.point.xy()[0] > self.camera.dimensions[0] - 50:
            self.nextStageKey = self.stages[0]

    def update(self):
        while self.nextStageKey is "Stage2":
            super().update()
            self.checkNextStagePosition()

        if self.nextStageKey == "Reset":
            self.__init__(self.control, self.window, self.sound, self.player, None, None, self.allObjects)
        else:
            return self.nextStageKey, True, self.changeResolution
