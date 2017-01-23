import pygame
from ImageControl import *
from Entity import *

class Blocks(Entity):

    def __init__(self, location, image, axis):
        pygame.sprite.Sprite.__init__(self)
        location = ImageControl.fixValues(location[0],location[1])
        self.rect = pygame.Rect((location[0],location[1]), (axis[0], axis[1]))
        self.block_surface = pygame.Surface((axis[0], axis[1]))
        self.define_img(image)
        self.image = ImageControl.fixScale(self.image)
        self.text = []
        #self.block_mask = pygame.mask.from_surface(self.block_surface)

    def define_img(self, image):
            self.image = pygame.image.load("../graphics/Plataformas/blocks/" + image + ".png").convert_alpha()

    def defineImg(self):
        pass

    def loadText(self):
        for i in range(len(self.text)):
            return(self.text[i])

    def renderBlocks(self):

        self.defineImg()