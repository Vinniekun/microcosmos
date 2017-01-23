# Feito por Vinicius Dreifke
import pygame
from ImageControl import *


class Physics:
    def __init__(self):
        self.constantgravity = 0.2
        self.gravity = 0.2
        self.maxDistance = 25
        self.vel_x = self.vel_y = self.vel_y_i = 0
        self.fall = True
        self.constantjump_power = 5
        self.jump_power = 5

    def check_falling(self):
        if self.vel_y < 0:
            self.fall = True
        else:
            self.fall = False

    def update_physics(self, fps):
        if self.fall:
            time = (1/fps)*60
            self.vel_y_i += self.gravity * time
            self.vel_y = self.vel_y_i * time + self.gravity/2 * time**2
            if self.vel_y > self.maxDistance:
                self.vel_y = self.maxDistance
        else:
            self.vel_y = self.vel_y + self.vel_y_i
            self.check_falling()

    def get_position(self):
        if not self.fall:
            self.check_falling()

    def jump(self):
        if self.fall:
            self.vel_y_i = -self.jump_power
            self.vel_y = self.vel_y_i
            self.fall = False
