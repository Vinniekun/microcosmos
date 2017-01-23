import pygame.freetype
import sys, os
from ImageControl import *


class Fonts:
    def __init__(self):
        self.fontdir = os.path.split(os.path.dirname(os.path.abspath(__file__)))
        self.fontdir = os.path.join(self.fontdir[0], "fonts", "Thempo New St.ttf")
        self.fontsize = 40
        self.fonts = {"Font1": pygame.font.Font(self.fontdir, self.fontsize)}

    def changeFontSize(self, string):
        fontsize = ImageControl.defineX(newsize)
        self.fonts[string] = pygame.font.Font(self.fontdir, fontsize)
