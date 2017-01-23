import pygame
from ImageControl import *
from stages.AbstractStage import *


class Intro(AbstractStage):
    def __init__(self, controller, window, sound, player, sprite, font, objects):
        self.control = controller
        self.name = "Intro"
        self.window = window
        self.choiceKey = 0
        self.sprite = sprite
        self.bg_alpha_value = 255
        self.animation_value = 1
        self.timer = 0
        self.go = 0
        self.font = None
        self.font_size = 30
        self.script_text = []
        self.script_file = open("../script/textos.txt", 'r')
        self.file_lines = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.font_name = "../script/fonts/coolvetica rg.ttf"
        self.text_render = []
        self.loadImages()
        self.loadFont()
        self.readFile()
        self.loadText()

    def loadImages(self):
        self.background = pygame.Surface(ImageControl.getWindowResolution())
        self.background = ImageControl.fullScreen(self.window, self.background)
        self.background.fill((255, 255, 255))

    def loadFont(self):
        pygame.font.init()
        self.font = pygame.font.Font(self.font_name, self.font_size)

    def pickLines(self, lines):
        return [x for i, x in enumerate(self.script_file) if i in lines]

    def readFile(self):
        self.script_text = (self.pickLines(self.file_lines))

    def loadText(self):
        for i in range(len(self.script_text)):
            self.text_render.append(self.font.render(self.script_text[i][:-1], True, (255, 255, 255)))

    def scene_imgs(self):
        ImageControl.centerImage(self.window, self.background)

    def introSelection(self, action):
        # testa se houve ação ou não
        if not action:
            return ""

        if action is "enter":  # Passa direto a tela de intro
            return "Stage1"

        # if action is "space": #Utilizado para avancar os textos da intro
        #	pass

        return ""

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

    def update(self):
        while True:
            self.window.windowScreen.fill((0, 0, 0))
            self.scene_imgs()
            aux = self.animationPool(self.control.checkKey())
            # aux = self.introSelection(self.control.checkKey())
            pygame.display.flip()
            pygame.time.Clock().tick(30)

            if aux != "":
                return aux, False, False
