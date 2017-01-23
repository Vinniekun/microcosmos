import pygame
from pygame import *
from ImageControl import *


class TerrainSurface(pygame.sprite.Sprite):
    def __init__(self, stage, img):
        pygame.sprite.Sprite.__init__(self)
        self.realimage = pygame.image.load("../graphics/Stages/" + stage + "/" + img + ".png").convert_alpha()
        self.image = ImageControl.fixScale(self.realimage)
        self.rect = self.image.get_rect()

    def setPosition(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
