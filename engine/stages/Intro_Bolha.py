import pygame
from ImageControl import *
from stages.AbstractStage import *
import sys


class Intro_Bolha(AbstractStage):
    def __init__(self, controller, window, sound, player, sprite, font, objects):
        self.control = controller
        self.name = "Intro_Bolha"
        self.sound = sound
        self.control = controller
        level_dimensions = (1280,720)
        super().__init__(player, window, "Intro_Bolha", level_dimensions)

        self.bg_alpha_value = 255
        self.animation_value = 1
        self.frameCount = 0
        self.time = 0
        self.font = None
        self.font_size = 30
        self.script_text = []
        self.script_file = open("../script/textos.txt", 'r')
        self.file_lines = [26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
        self.font_name = "../script/fonts/coolvetica rg.ttf"
        self.text_render = []
        self.loadImages()
        self.loadFont()
        self.readFile()
        self.loadText()

    def loadImages(self):
        self.image = []
        self.actualImage = 0
        for i in range(1, 6):
            self.image.append(pygame.image.load("../graphics/Monsters/bolha/bolha" + str(i) + ".png"))

    def loadFont(self):
        pygame.font.init()
        self.font = pygame.font.Font(self.font_name, self.font_size)

    def pickLines(self, lines):
        return [x for i, x in enumerate(self.script_file) if i in lines]

    def readFile(self):
        self.script_text = (self.pickLines(self.file_lines))

    def loadText(self):
        self.continue_text = self.font.render("Pressione a tecla Enter para continuar", True, (255, 255, 255))
        for i in range(len(self.script_text)):
            self.text_render.append(self.font.render(self.script_text[i][:-1], True, (255, 255, 255)))

    def animationPool(self, action):
        if self.animation_value is 1:
            self.bg_alpha_value -= 5
            self.background.set_alpha(self.bg_alpha_value)
            if self.bg_alpha_value is 0:
                self.animation_value += 1
        elif self.animation_value is 2:
            self.timer += 1
            if self.timer is 50:
                self.timer = 0
                self.animation_value += 1

        elif self.animation_value is 3:
            self.timer += 1
            ImageControl.setImageAt(self.window, self.text_render[0], (50, 50))
            if action is "space":  # Utilizado para avancar os textos da intro
                self.go = 1
            if self.go == 1:
                self.timer = 0
                self.animation_value = 1
                self.bg_alpha_value = 255
                return "Stage1"
            if self.timer > 100:
                ImageControl.setImageAt(self.window, self.text_render[1], (50, 150))
            if self.timer > 200:
                ImageControl.setImageAt(self.window, self.text_render[2], (50, 250))
            if self.timer > 300:
                ImageControl.setImageAt(self.window, self.text_render[3], (50, 350))
            if self.timer > 400:
                ImageControl.setImageAt(self.window, self.text_render[4], (50, 450))
            if self.timer > 500:
                ImageControl.setImageAt(self.window, self.text_render[5], (50, 550))
            # if self.timer >600:
            # if action is "space": #Utilizado para avancar os textos da intro
            #	self.go = 1

        return ""

    def eventTimer(self, fps):
        try:
            self.frameCount += 1.7 / fps * 60
        except ZeroDivisionError:
            print("Divisao por zero")
            self.frameCount = 0

        if self.frameCount >= 100:
            self.time += 1 #tempo em segundos
            self.frameCount = 0

    def screenCinema(self):
        ImageControl.centerImage(self.window, self.image[self.actualImage])
        if self.time >= 3:
            ImageControl.setImageAt(self.window, self.text_render[0], (50, 50))
        if self.time >= 6:
            ImageControl.setImageAt(self.window, self.text_render[1], (50, 100))
        if self.time >= 9:
            ImageControl.setImageAt(self.window, self.text_render[2], (50, 150))
        if self.time >= 12:
            ImageControl.setImageAt(self.window, self.text_render[3], (50, 200))
        if self.time >= 15:
            ImageControl.setImageAt(self.window, self.text_render[4], (50, 250))
        if self.time >= 18:
            ImageControl.setImageAt(self.window, self.text_render[5], (50, 300))
        if self.time >= 21:
            ImageControl.setImageAt(self.window, self.text_render[6], (50, 350))
        if self.time >= 24:
            ImageControl.setImageAt(self.window, self.text_render[7], (50, 400))
        if self.time >= 27:
            ImageControl.setImageAt(self.window, self.text_render[8], (50, 450))
        if self.time >= 30:
            ImageControl.setImageAt(self.window, self.text_render[9], (50, 500))
        if self.time >= 4 and self.time%2 is 0:
            ImageControl.setImageAt(self.window, self.continue_text, ((self.window.windowScreen.get_width() // 2) - 200, self.window.windowScreen.get_height() * 0.8))



    def update(self):
        while self.nextStageKey is "Intro_Bolha":
            fps = super().update_intros()
            self.eventTimer(fps)
            self.screenCinema()
            next = self.player.introControls()
            if next is True:
                self.nextStageKey = "Map2"
        return self.nextStageKey, True, self.changeResolution