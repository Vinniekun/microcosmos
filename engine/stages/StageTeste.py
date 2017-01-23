import pygame
from pygame import *
from stages.AbstractStage import *
from ImageControl import *
from Physics import *
from Point import *
from Enemy import *
from Camera import *
from TerrainSurface import *


class StageTeste (AbstractStage):
    def __init__(self, controller, window, sound, player, sprite, fonts, objects):
        self.sound = sound
        self.control = controller
        self.allObjects = objects
        self.allObjects.loadEnemies()
        level_dimensions = (4650, 1000)
        super().__init__(player, window, "StageTeste", level_dimensions)

        self.player.newLevel((50, 400))
        self.entities.add(self.player)
        self.surface_terrain = pygame.Surface((1000, 1000))
        self.create_background("skin3")
        self.loadSounds()
        self.player.physics = Physics()
        self.define_enemies()

    def define_enemies(self):
        self.create_enemies("azul", (400, 600))

    def collision_terrain(self):
        collision_pos = self.surface_terrain.mask.overlap(self.player.mask_player, self.player.point.ixy())

        if self.player.point.xy()[0] > ImageControl.defineX(self.camera.dimensions[0]):
            self.nextStageKey = "Stage2"
        elif collision_pos is not None:
            # Com colisao
            self.nextStageKey = "Menu"

    def loadSounds(self):
        self.sound.soundStage1()

    def collisions(self):
        self.collision_terrain()

    def update(self):
        while self.nextStageKey is "StageTeste":
            #self.collisions()
            super().update()

        return self.nextStageKey, True, self.changeResolution
