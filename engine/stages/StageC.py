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
        self.image = pygame.image.load("../graphics/Stage5/stage5.png").convert_alpha()
        self.image = ImageControl.fixScale(self.image)
        self.rect = self.image.get_rect()


class Stage5:
    def __init__(self, controller, window, sound, player, sprite, fonts):
        self.control = controller
        self.name = "Stage5"
        self.nextStageKey = "Stage5"
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
        self.define_enemies()
        self.i = True

    def define_enemies(self):
        self.create_enemies(ImageControl.fixValues(300, 500), "pelo")
        self.create_enemies(ImageControl.fixValues(700, 500), "pelo")
        self.create_enemies(ImageControl.fixValues(700, -200), "pelo", -1, False, True)
        self.create_enemies(ImageControl.fixValues(700, 300), "bicho", 0, True)
        self.create_enemies(ImageControl.fixValues(1400, 300), "bicho", 1, True)

    def create_enemies(self, pos, object, path=-1, moves=False, inverted=False):
        enemy = Enemy(object, path, moves)

        if not inverted:
            enemy.image = self.enemiesImages[object]
        else:
            enemy.image = pygame.transform.flip(self.enemiesImages[object], False, True)
        enemy.rect = self.enemiesImages[object].get_rect()
        enemy.rect.x = pos[0]
        enemy.rect.y = pos[1]
        self.objects.add(enemy)

    def loadImages(self):
        self.background = pygame.image.load("../graphics/Textures/skin3.jpg").convert_alpha()
        self.background = ImageControl.fixScale(self.background)
        self.surface_terreno = TerrainSurface()
        self.enemiesImages = {"pelo" : pygame.image.load("../graphics/Plataformas/pelo.png").convert_alpha(), "bicho" : pygame.image.load("../graphics/Monsters/bacteria2.png").convert_alpha()}
        for i,j in self.enemiesImages.items():
            j = ImageControl.fixScale(j)
        self.entities.add(self.surface_terreno)
        self.mask_terreno = pygame.mask.from_surface(self.surface_terreno.image)

    def scene_imgs(self):
        #ImageControl.setImageAt(self.window, self.background, (0, 0))
        #ImageControl.repeatImage(self.window, self.background, True)
        for o in self.objects:
            image = pygame.transform.rotate(o.image, o.angle)
            self.window.windowScreen.blit(image, self.camera.apply(o))

        for e in self.entities:
            self.window.windowScreen.blit(e.image, self.camera.apply(e))

    def object_actions(self):
        for o in self.objects:
            o.action()

    def collision_terrain(self):
        collision_pos = self.mask_terreno.overlap(self.player.mask_player, self.player.point.ixy())
        if collision_pos is None:
            # Sem colisao
            #Gravidade
            pass
        # print(collision_pos)
        if self.player.point.xy()[0] > ImageControl.defineX(4600):  # Se houver colisao com o fim da fase...
            self.nextStageKey = "Stage2"
        elif collision_pos is not None:
            # Com colisao
            self.player.onfloor = True
            self.player.physics.fall = False
            # Andar sobre a fase..

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
        while self.nextStageKey is "Stage5":
            self.player.movement(self.control.checkPressed())
            self.player.update()

            self.camera.update(self.player)
            self.scene_imgs()
            self.object_actions()

            pygame.display.flip()
            pygame.time.Clock().tick(30)
            self.window.windowScreen.fill((255, 255, 255))
            self.collision()
        return self.nextStageKey, True, False
