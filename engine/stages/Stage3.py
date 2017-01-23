import pygame
from pygame import *

from ImageControl import *
from stages.AbstractStage import *
from Physics import *
from Physics2 import *
from Point import *
from Enemy import *
from Camera import *
from Blocks import *


class Stage3(AbstractStage):
    def __init__(self, controller, window, sound, player, sprite, fonts, objects):
        self.sound = sound
        self.control = controller
        self.allObjects = objects
        self.stage_file = None
        level_dimensions = (1350, 6700)
        super().__init__(player, window, "Stage3", level_dimensions)

        self.newlevel = (140, -40)
        self.player.newLevel(self.newlevel)
        self.player.inShip = False
        self.player.definingCheckpoint(self.newlevel)
        self.stages = ["Menu"]
        self.player.max = 0
        self.player.loadPlayerImages()
        self.name = "Stage3"
        #self.entities = pygame.sprite.Group()
        self.entities.add(self.player)
        self.loadSounds()
        self.player.physics = Physics2()
        self.blocos = pygame.sprite.Group()
        self.define_enemies()
        self.create_background("skin9")
        self.loadStage()
        self.shipPhase = False

    def loadSounds(self):
        self.sound.soundStage7()

    def loadStage(self):
        self.stage_file = open("../graphics/Stage3/stage.txt", 'r')
        self.readFile()
        self.renderBlocks()

    def readFile(self):
        self.matrix = self.stage_file.readlines()

    def renderBlocks(self):
        axis = ImageControl.fixValues(50, 50)
        for y in range(0, 130):
            for x in range(0, 27):
                coord = self.matrix[y][x]
                if coord is not '0':
                    img = coord
                    w = axis[0] * x
                    h = axis[1] * y
                    self.create_blocks((w, h), img, axis)

    def create_blocks(self, location, image, axis):
        block = Blocks(location, image, axis)
        self.blocos.add(block)

    def define_enemies(self):

        self.create_enemies("checkpoint", (1155, 2505))

        self.create_enemies("vida", (1200, 120))
        self.create_enemies("vida", (1200, 3400))
        self.create_enemies("vida", (400, 3100))

        self.create_enemies("sistemaimuno", (1300, 1200))
        self.create_enemies("sistemaimuno", (1000, 2100))
        self.create_enemies("sistemaimuno", (1400, 3320))

        self.create_enemies("bolha", (200, 600))
        self.create_enemies("bolha", (300, 600))
        self.create_enemies("bolha", (400, 600))

        self.create_enemies("bolhamaior", (500, 500))
        self.create_enemies("bolhamaior", (700, 1850))
        self.create_enemies("bolhamaior", (820, 2500))
        self.create_enemies("bolha", (600, 400))
        self.create_enemies("bolha", (600, 300))


        self.create_enemies("bolha", (150, 1100))
        self.create_enemies("bolha", (150, 1200))
        self.create_enemies("bolha", (150, 1300))
        self.create_enemies("bolha", (150, 1400))

        self.create_enemies("bolha", (1150, 1900))
        self.create_enemies("bolha", (1150, 2000))
        self.create_enemies("bolha", (1150, 2100))
        self.create_enemies("bolha", (1150, 2200))
        self.create_enemies("bolha", (1150, 2300))
        self.create_enemies("bolha", (1150, 2400))

        self.create_enemies("bolha", (400, 2350))
        self.create_enemies("bolha", (600, 2500))

        self.create_enemies("bolha", (150, 2900))
        self.create_enemies("bolha", (150, 3000))
        self.create_enemies("bolha", (150, 3100))

        self.create_enemies("bolha", (100, 3300))
        self.create_enemies("bolha", (200, 3300))
        self.create_enemies("bolha", (300, 3300))
        self.create_enemies("bolha", (400, 3300))

        self.create_enemies("bolha", (100, 3400))
        self.create_enemies("bolha", (200, 3400))
        self.create_enemies("bolha", (300, 3400))
        self.create_enemies("bolha", (400, 3400))

        self.create_enemies("bolha", (750, 3300))
        self.create_enemies("bolha", (750, 3400))
        self.create_enemies("bolha", (750, 3500))
        self.create_enemies("bolha", (750, 3600))
        self.create_enemies("bolha", (750, 3700))
        self.create_enemies("bolha", (750, 3800))
        self.create_enemies("bolha", (750, 3900))
        self.create_enemies("bolha", (750, 4000))
        self.create_enemies("bolha", (750, 4100))

        #for i in range(0, 4):
            #self.create_enemies("sistemaimuno", (400 + i * 700, 610))
            #self.create_enemies("sistemaimuno", (700 + i * 840, 550))
        #self.create_enemies("bolha", (700, 600))
        #self.create_enemies("bolha", (700, 800))

    def collision_ending(self):
        if self.player.rect[1] > ImageControl.defineY(6700):
            self.nextStageKey = self.stages[0]

    def update(self):
        while self.nextStageKey is "Stage3":
            super().update()
            self.collision_ending()

        return self.nextStageKey, True, False
