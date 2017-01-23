# Feito por Vinicius Dreifke
import pygame
from ImageControl import *


class Physics2:
    def __init__(self):
        self.gravity = 0.3

        self.vel_x = self.vel_y = self.vel_y_i = 0
        self.maxDistance = 30
        self.fall = False
        self.time = 0
        self.on_air = True
        self.jumpable = False
        self.jump_power = 11
        #self.jump_power = ImageControl.defineY(9, True)
        self.v0 = 0

    def collision(self):
        self.fall = False
        self.on_air = False
        self.jumpable = True
        self.vel_y = 0
        self.vel_y_i = 0

    def check_falling(self):
        if self.vel_y <= 0:
            self.fall = True
        else:
            self.fall = False

    def update_physics(self, fps):
        if self.fall:
            self.jumpable = False
            time = (1/fps)*60
            self.vel_y_i += self.gravity * time

            self.vel_y = self.vel_y_i * time + self.gravity/2 * time**2
            if self.vel_y > self.maxDistance:
                self.vel_y = self.maxDistance

        else:
            self.vel_y = self.vel_y_i = 0
            self.jumpable = True

    def check_falling2(self, player, object):
        player.rect.move_ip((0, 1))
        collisions = pygame.sprite.spritecollide(player, object, False)
        collidable = pygame.sprite.collide_mask
        if not pygame.sprite.spritecollideany(player, collisions, collidable):
            self.fall = True
        player.rect.move_ip((0, -1))

    def get_position(self, player, object):
        if not self.fall:
            self.check_falling2(player, object)
        else:
            self.fall = self.check_collisions((0, self.vel_y), 1, object, player)
        if self.vel_x:
            self.check_collisions((self.vel_x, 0), 0, object, player)

    def jump(self):
        if self.jumpable:
            self.vel_y = -self.jump_power
            self.vel_y_i = -self.jump_power
            self.on_air = True
            self.fall = True

    def bubbleJump(self, jump):
        self.time = 0
        self.vel_y_i = -(self.jump_power+jump)
        self.on_air = True
        self.fall = True


    def check_collisions(self, offset, index, object, player):
        unaltered = True
        player.rect.move_ip(offset)

        while pygame.sprite.spritecollideany(player, object):
            player.rect[index] += (1 if offset[index] < 0 else -1)
            unaltered = False
        return unaltered
