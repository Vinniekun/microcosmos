import pygame


class Sprite:
    def __init__(self):
        self.menuImage = pygame.image.load("../graphics/Menu/menu.jpg").convert_alpha()