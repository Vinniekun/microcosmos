import pygame
from ImageControl import *
from Point import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, name="", objectsLoaded=None, inverted=False, resize=1):
        pygame.sprite.Sprite.__init__(self)
        self.name = name

        self.inverted = inverted
        if objectsLoaded is not None:
            self.definingImages(objectsLoaded, resize)

        self.isDead = False
        self.index = 0
        self.imgIndex = 0

    def changeImage(self):
        self.image = self.actualimages[self.imgIndex][self.index]
        self.index = (self.index + 1) % len(self.images[self.imgIndex])

    def setActualImage(self, pos=[0, 0]):
        self.image = self.actualimages[self.imgIndex][self.index]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def atualizeActualImage(self):
        self.image = self.actualimages[self.imgIndex][self.index]

    def definingImages(self, images, resize=1):
        if self.inverted:
            self.images = []
            for i in range(len(images)):
                self.images.append([])
                for j in range(len(images[i])):
                    self.images[i].append(ImageControl.zoomImage(pygame.transform.flip(images[i][j], False, True), resize))
        else:
            self.images = images

        self.definingOriginalImages()

    def definingOriginalImages(self):
        self.actualimages = []
        for i in range(len(self.images)):
            self.actualimages.append([])
            for j in range(len(self.images[i])):
                self.actualimages[i].append(ImageControl.fixScale(self.images[i][j]))
