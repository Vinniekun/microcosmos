import pygame
from pygame.locals import *

from ImageControl import *


class Window:
    def __init__(self):
        pygame.display.set_caption("Microcosmos")
        icon = pygame.image.load("../graphics/icon.jpg")
        pygame.display.set_icon(icon)
        self.getResolution()
        self.setImageResolution()
        self.setWindowScreen()
        self.resolutionChange = False

    def setFullScreen(self):
        pygame.display.toggle_fullscreen()

    def setWindowScreen(self):
        self.windowScreen = pygame.display.set_mode((1280, 720), HWSURFACE | DOUBLEBUF | RESIZABLE)

    def getResolution(self):
        self.screenResolution = (1280, 720)

    def camera(self, camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera

        # retangulo da camera
        l, t, _, _ = -l + self.getHalfWidth() / 2, -t + self.getHalfHeight(), w, h

        # para movimento na esquerda
        l = min(0, l)
        # para movimento na direita
        l = max(-(camera.width - self.screenResolution[0]), l)

        # para movimento embaixo
        t = max(-(camera.height - self.screenResolution[1]), t)

        # para movimento em cima
        t = min(0, t)

        return Rect(l, t, w, h)

    def getHalfWidth(self):
        return self.screenResolution[0] / 2

    def getHalfHeight(self):
        
        return self.screenResolution[1] / 2

    def setImageResolution(self):
        ImageControl.setImageResolution(self.screenResolution)
        self.resolutionChange = True

    def changeResolution(self, event):
        self.windowScreen = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.screenResolution = event.dict['size']
        self.setImageResolution()

    def changeDefinedResolution(self, resolution):
        self.windowScreen = pygame.display.set_mode(resolution, HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.screenResolution = resolution
        self.setImageResolution()