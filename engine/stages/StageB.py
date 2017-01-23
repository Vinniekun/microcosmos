import pygame
from pygame import *

from ImageControl import *
from Physics import *
from Point import *
from Enemy import *
from Camera import *


class TerrainSurface(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../graphics/Stage4/stage4.png").convert_alpha()
        self.image = ImageControl.fixScale(self.image)
        self.rect = self.image.get_rect()


class Stage4:
    def __init__(self, controller, window, sound, player, sprite, fonts):
        self.control = controller
        self.name = "Stage4"
        self.nextStageKey = "Stage4"
        self.window = window
        self.sound = sound
        self.player = player
        self.player.newLevel(50, 400)
        self.sprite = sprite

        level_dimensions = ImageControl.fixValues(4650, 1000)
        self.camera = Camera(self.window.camera, level_dimensions)

        self.entities = pygame.sprite.Group()
        self.entities.add(self.player)

        self.objects = pygame.sprite.Group()

        self.surface_terreno = pygame.Surface(ImageControl.fixValues(1000, 1000))
        self.mask_terreno = None
        self.background = None
        self.loadImages()

        self.player.physics = Physics()
        #self.define_enemies()
        self.i = True

    def define_enemies(self):
        self.create_enemies(ImageControl.fixValues(300, 500))
        self.create_enemies(ImageControl.fixValues(700, 500))
        self.create_enemies(ImageControl.fixValues(700, -200), True)

    def create_enemies(self, pos, inverted=False):
        enemy = Enemy("pelo")

        if not inverted:
            enemy.image = self.peloimage
        else:
            enemy.image = pygame.transform.flip(self.peloimage, False, True)
        enemy.rect = self.peloimage.get_rect()
        enemy.rect.x = pos[0]
        enemy.rect.y = pos[1]
        self.objects.add(enemy)


    def loadImages(self):
        self.background = pygame.image.load("../graphics/Textures/skin3.jpg").convert_alpha()
        self.background = ImageControl.fixScale(self.background)
        self.surface_terreno = TerrainSurface()
        self.peloimage = pygame.image.load("../graphics/Plataformas/pelo.png").convert_alpha()
        self.peloimage = ImageControl.fixScale(self.peloimage)
        # self.entities.add(self.background)
        self.entities.add(self.surface_terreno)
        self.player.loadImages()
        self.mask_terreno = pygame.mask.from_surface(self.surface_terreno.image)

    def scene_imgs(self):
        for o in self.objects:
            image = pygame.transform.rotate(o.image, o.angle)
            self.window.windowScreen.blit(image, self.camera.apply(o))

        for e in self.entities:
            self.window.windowScreen.blit(e.image, self.camera.apply(e))
        #ImageControl.setImageAt(self.window, self.background, (0, 0))
        #ImageControl.repeatImage(self.window, self.background, True)

    def object_actions(self):
        for o in self.objects:
            o.action()

    def collision_terrain(self):
        collision_pos = self.mask_terreno.overlap(self.player.mask_player, self.player.point.ixy())
        if collision_pos is None:
            # Sem colisao
            pass
        # print(collision_pos)
        if self.player.point.xy()[0] > ImageControl.defineX(4600):  # Se houver colisao com o fim da fase...
            self.nextStageKey = "Stage5"
        elif collision_pos != None:
            # Com colisao
            self.nextStageKey = "Menu"

    def collision(self):

        for o in self.objects:
            collision_pos = pygame.sprite.collide_mask(o, self.player)
            if collision_pos == None:
                #nao houve colisao
                pass
            else:
                self.player.speed = 2


        self.collision_terrain()




    def update(self):
        while self.nextStageKey is "Stage4":
            self.player.movement(self.control.checkPressed())
            self.player.update()

            self.camera.update(self.player)
            self.scene_imgs()
            self.object_actions()

            pygame.display.flip()
            pygame.time.Clock().tick(60)
            self.window.windowScreen.fill((255, 255, 255))
            self.collision()
        return self.nextStageKey, True, False
