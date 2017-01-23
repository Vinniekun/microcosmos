import pygame

class Animation:


    def __init__(self):
        pass

    def loadImages(self):
        self.image = pygame.image.load("../graphics/Sprites/nave1-0.png").convert_alpha()
        self.mask_player = pygame.mask.from_surface(self.image)
        self.actualimage = pygame.image.load("../graphics/Sprites/nave1-0.png").convert_alpha()
        self.actualimage = self.actualimage