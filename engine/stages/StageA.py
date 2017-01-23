import pygame
from pygame import *

from ImageControl import *
from Physics import *
from Point import *
from Camera import *


class TerrainSurface(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../graphics/Stage3/stage3.png").convert_alpha()
        self.image = ImageControl.fixScale(self.image)
        self.rect = self.image.get_rect()


class Stage3:
    def __init__(self, controller, window, sound, player, sprite, fonts):
        self.control = controller
        self.name = "Stage3"
        self.nextStageKey = "Stage3"
        self.window = window
        self.sound = sound

        self.player = player
        self.player.newLevel(50, 400)

        self.sprite = sprite

        level_dimensions = ImageControl.fixValues(4650, 1000)
        self.camera = Camera(self.window.camera, level_dimensions)

        self.entities = pygame.sprite.Group()
        self.entities.add(self.player)

        self.surface_terreno = pygame.Surface(ImageControl.fixValues(1000, 1000))
        self.mask_terreno = None
        self.background = None
        self.loadImages()
        self.player.physics = Physics()

        self.i = True

    def loadImages(self):
        self.background = pygame.image.load("../graphics/Textures/skin3.jpg").convert_alpha()
        self.background = ImageControl.fixScale(self.background)
        self.surface_terreno = TerrainSurface()

        # self.entities.add(self.background)
        self.entities.add(self.surface_terreno)

        self.mask_terreno = pygame.mask.from_surface(self.surface_terreno.image)

    def scene_imgs(self):
        pass
        #ImageControl.setImageAt(self.window, self.background, (0, 0))
        #mageControl.repeatImage(self.window, self.background, True)

    # ImageControl.setImageAt(self.window, self.surface_terreno, (0,0))
    # ImageControl.setImageAt(self.window, self.player.surface_player, (self.player.point.xy()))

    def collision(self):
        # self.mask_terreno.fill()
        collision_pos = self.mask_terreno.overlap(self.player.mask_player, self.player.point.ixy())
        if collision_pos is None:
            # Sem colisao
            pass
        # print(collision_pos)
        if self.player.point.xy()[0] > ImageControl.defineX(4600):  # Se houver colisao com o fim da fase...
            self.nextStageKey = "Stage4"
        elif collision_pos != None:
            # Com colisao
            self.nextStageKey = "Menu"
        # print(collision_pos)

    def update(self):
        while self.nextStageKey is "Stage3":
            self.player.movement(self.control.checkPressed())
            self.player.update()

            self.camera.update(self.player)
            self.scene_imgs()
            for e in self.entities:
                self.window.windowScreen.blit(e.image, self.camera.apply(e))

            pygame.display.flip()
            pygame.time.Clock().tick(60)
            self.window.windowScreen.fill((255, 255, 255))
            self.collision()
        return self.nextStageKey, True, False
