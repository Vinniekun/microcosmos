import pygame
from ImageControl import *


class Options:
    def __init__(self, controller, window, sound, player, sprite, fonts, objects):
        self.name = "Options"
        self.window = window
        self.control = controller
        self.sprite = sprite
        self.sound = sound
        self.fonts = fonts

        self.choiceKey = 0
        self.load_images()
        self.edit_images()
        self.initialKey = self.resolutionsKey

    def load_images(self):
        self.options = [ImageControl.fixScale(
            ImageControl.zoomImage(pygame.image.load("../graphics/Menu/res" + str(i) + ".png").convert_alpha(), .6)) for
                        i in range(1, 4)]
        self.resolutions = [(800, 600), (1024, 768), (1280, 720), (1366, 768), (1600, 900), (1920, 1080), (0, 0)]

        self.resolutionsKey = 0
        self.temp__resolutionsKey = 0

        # ajustar resolutionKey
        for i in range(len(self.resolutions)):
            if self.resolutions[i][0] == self.window.screenResolution[0] and self.resolutions[i][1] == \
                    self.window.screenResolution[1]:
                self.resolutionsKey = self.temp__resolutionsKey = i
                break
        self.background = self.sprite.menuImage

    # função chamada sempre que a classe Options é criada, ou quando a resolução muda
    def edit_images(self):
        self.options[self.choiceKey] = ImageControl.zoomImage(self.options[self.choiceKey], 1.25)
        self.background = ImageControl.fullScreen(self.window, self.background)

    def scene_fonts(self):
        temp__str = ""

        if self.resolutions[self.temp__resolutionsKey] == (0, 0):
            temp__str = "Full Screen"
        else:
            temp__str = str(self.resolutions[self.temp__resolutionsKey])

        temp_resolution = self.fonts.fonts["Font1"].render(temp__str, 1, (255, 255, 255))
        temp_resolution = ImageControl.fixScale(temp_resolution)
        self.window.windowScreen.blit(temp_resolution, ImageControl.definePosition((
            ImageControl.defineX(700), ImageControl.defineY(400))))

        if self.temp__resolutionsKey != self.resolutionsKey:
            temp_resolution = self.fonts.fonts["Font1"].render("Confirmar (Pressione Enter)", 1, (255, 0, 0))
            temp_resolution = ImageControl.zoomImage(temp_resolution, .6)
            temp_resolution = ImageControl.fixScale(temp_resolution)
            self.window.windowScreen.blit(temp_resolution, ImageControl.definePosition((
                ImageControl.defineX(650), ImageControl.defineY(350))))

    def scene_imgs(self):
        ImageControl.centerImage(self.window, self.background)
        for i in range(3):
            ImageControl.setImageAt(self.window, self.options[i], ImageControl.definePosition((100, 400 + 60 * i)))

    # checa se houve mudança de resolução
    def changeResolution(self):
        if self.temp__resolutionsKey != self.resolutionsKey:
            if self.temp__resolutionsKey == 6:
                self.window.setFullScreen()
            self.window.changeDefinedResolution(self.resolutions[self.temp__resolutionsKey])
            self.resolutionsKey = self.temp__resolutionsKey
            self.load_images()
            self.edit_images()

    def update(self):

        while True:
            self.window.windowScreen.fill((255, 255, 255))
            self.scene_imgs()
            self.scene_fonts()
            pygame.display.flip()
            pygame.time.Clock().tick(15)
            aux = self.optionSelection(self.control.checkKey())
            if aux != "":
                if self.initialKey != self.resolutionsKey:
                    return aux, True, True
                return aux, True, False

    def optionSelection(self, action):
        if not action:
            return ""
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if action == "enter":
                    if self.choiceKey == 0:
                        self.changeResolution()
                    elif self.choiceKey == 2:
                        self.sound.playSound("cursor_back")
                        return "Menu"
                    return ""
                if action == "left" or action == "right":
                    self.sound.playSound("cursor_move")
                    if self.choiceKey == 0:
                        if action == "left":
                            self.temp__resolutionsKey -= 1
                            if self.temp__resolutionsKey < 0:
                                self.temp__resolutionsKey = 6
                        elif action == "right":
                            self.temp__resolutionsKey = (self.temp__resolutionsKey + 1) % 7
                    return ""

                self.options[self.choiceKey] = ImageControl.zoomImage(self.options[self.choiceKey], 0.8)

                if action == "up":
                    self.sound.playSound("cursor_move")
                    self.choiceKey -= 1
                    if self.choiceKey < 0:
                        self.choiceKey = 2
                elif action == "down":
                    self.sound.playSound("cursor_move")
                    self.choiceKey = (self.choiceKey + 1) % 3

                self.options[self.choiceKey] = ImageControl.zoomImage(self.options[self.choiceKey], 1.25)
                return ""

    def changeVolume(self):
        pass
