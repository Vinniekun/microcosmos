import pygame
from ImageControl import *
from stages.AbstractStage import *


class Map2(AbstractStage):
    def __init__(self, controller, window, sound, player, sprite, font, objects):
        self.control = controller
        self.name = "Map2"
        self.sound = sound
        self.control = controller
        level_dimensions = (1280,720)
        super().__init__(player, window, "Map2", level_dimensions)
        self.destination = self.window.windowScreen.get_width() * 0.47
        self.bg_alpha_value = 0
        self.animation_value = 1
        self.shiplocation = (self.window.windowScreen.get_width() * 0.4)
        self.frameCount = 0
        self.time = 0
        self.font = None
        self.font_size = 30
        self.script_text = []
        self.font_name = "../script/fonts/coolvetica rg.ttf"
        self.loadImages()
        self.loadFont()
        self.loadText()
        self.loadSounds()

    def loadSounds(self):
        self.sound.soundMap()

    def loadImages(self):
        self.image_corpo1 = pygame.image.load("../graphics/Imagens/corpo-1.png")
        self.image_corpo2 = pygame.image.load("../graphics/Imagens/corpo-2.png")
        self.image_corpo3 = pygame.image.load("../graphics/Imagens/corpo-3.png")
        self.image_nave = pygame.image.load("../graphics/Sprites/nave1-0.png")


    def loadFont(self):
        pygame.font.init()
        self.font = pygame.font.Font(self.font_name, self.font_size)

    def loadText(self):
        self.continue_text = self.font.render("Pressione a tecla Enter para continuar", True, (255, 255, 255))

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
        self.image_corpo1.set_alpha(self.bg_alpha_value)
        ImageControl.centerImage(self.window, self.image_corpo1)
        if self.time > 0 and self.bg_alpha_value < 255:
            self.bg_alpha_value += 1
        if self.time > 3:
            ImageControl.centerImage(self.window, self.image_corpo2)
        if self.time > 4:
            ImageControl.centerImage(self.window, self.image_corpo3)
        if self.time > 5:
            ImageControl.setImageAt(self.window, self.image_nave, (self.shiplocation, self.window.windowScreen.get_height() * 0.2))
        if self.time >= 5 and self.time%2 is 0:
            ImageControl.setImageAt(self.window, self.continue_text, ((self.window.windowScreen.get_width() // 2) - 200, self.window.windowScreen.get_height() * 0.8))
        if self.time > 6 and self.shiplocation < self.destination:
            self.shiplocation += 1
            if self.shiplocation >= self.destination:
                self.sound.playSound("nextstage")

    def update(self):
        while self.nextStageKey is "Map2":
            fps = super().update_intros()
            self.eventTimer(fps)
            self.screenCinema()
            next = self.player.introControls()
            if next is True:
                self.sound.stopSound("nextstage")
                self.nextStageKey = "Ameaca_2"
        return self.nextStageKey, True, self.changeResolution