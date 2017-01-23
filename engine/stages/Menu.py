import pygame
from ImageControl import *
from stages.AbstractStage import *
from Character import *


class Menu(AbstractStage):
    def __init__(self, controller, window, sound, player, sprite, fonts, objects):
        self.control = controller
        self.name = "Menu"
        self.window = window
        self.sound = sound
        self.change = False
        self.control = controller
        self.choiceOptions = ["Intro_1", "Options", "Quit"]
        self.choiceKey = 0
        self.sprite = sprite
        self.loadImages()
        objects.loadEnemies()
        self.loadSounds()
        self.resizeImages()
        self.music = pygame.mixer.music.load("../sound/BGM/menu.mp3")
        #pygame.mixer.music.play(1)

    def loadImages(self):
        self.options = [pygame.image.load("../graphics/Menu/opt" + str(i) + ".png").convert_alpha() for i in
                        range(1, 4)]
        self.fixoptions = []
        for i in range(3):
            self.fixoptions.append(ImageControl.fixScale(self.options[i]))

    def loadSounds(self):
        self.sound.soundMenu()

    def resizeImages(self):
        # imagem do menu
        self.sprite.menuImage = ImageControl.fullScreen(self.window, self.sprite.menuImage)

        # opções de escolha
        for i in range(0, 3):
            self.fixoptions[i] = ImageControl.fixScale(self.options[i])
        self.fixoptions[0] = ImageControl.zoomImage(self.options[0], 1.25)

    def scene_imgs(self):
        ImageControl.centerImage(self.window, self.sprite.menuImage)
        ImageControl.centerImage(self.window, self.fixoptions[0])
        ImageControl.belowcenterImage(self.window, 1, self.fixoptions[1])
        ImageControl.belowcenterImage(self.window, 5, self.fixoptions[2])

    def update(self):
        while True:
            self.scene_imgs()
            pygame.display.flip()
            pygame.time.Clock().tick(15)
            aux = self.menuSelection(self.checkPressed())
            if self.window.resolutionChange:
                self.fixResolution()
            if aux != "":
                if aux != "Quit" and aux != "Options":
                    self.player = Character(self.control, self.sound)
                return aux, False, self.change

    def fixResolution(self):
        self.player.updateWindow()
        self.resizeImages()
        self.window.resolutionChange = False
        self.change = True  # caso mude de cena, atualizará a resolução das imagens

    def checkPressed(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit()
            elif event.type == VIDEORESIZE:
                self.window.changeResolution(event)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    return "enter"
                elif event.key == pygame.K_UP:
                    return "up"
                elif event.key == pygame.K_DOWN:
                    return "down"
                elif event.key == pygame.K_p:
                    self.sprite.menuImage = pygame.image.load("../graphics/Menu/pedro.jpg")
                    self.sprite.menuImage = ImageControl.fullScreen(self.window, self.sprite.menuImage)
                    self.sound.playSound("yeah")
                    pass
                elif event.key == pygame.K_r:
                    self.sprite.menuImage = pygame.image.load("../graphics/Menu/rafael.jpg")
                    self.sprite.menuImage = ImageControl.fullScreen(self.window, self.sprite.menuImage)
                    self.sound.playSound("yeah")
                    pass
                elif event.key == pygame.K_o:
                    self.sprite.menuImage = pygame.image.load("../graphics/Menu/otavio.jpg")
                    self.sprite.menuImage = ImageControl.fullScreen(self.window, self.sprite.menuImage)
                    self.sound.playSound("yeah")
                    pass
                elif event.key == pygame.K_v:
                    self.sprite.menuImage = pygame.image.load("../graphics/Menu/vini.jpg")
                    self.sprite.menuImage = ImageControl.fullScreen(self.window, self.sprite.menuImage)
                    self.sound.playSound("yeah")
                    pass
                elif event.key == pygame.K_j:
                    self.sprite.menuImage = pygame.image.load("../graphics/Menu/joao.jpg")
                    self.sprite.menuImage = ImageControl.fullScreen(self.window, self.sprite.menuImage)
                    self.sound.playSound("yeah")
                    pass
                elif event.key == pygame.K_c:
                    self.sprite.menuImage = pygame.image.load("../graphics/Menu/cassi1.jpg")
                    self.sprite.menuImage = ImageControl.fullScreen(self.window, self.sprite.menuImage)
                    self.sound.playSound("yeah")
                    pass
                elif event.key == pygame.K_x:
                    self.sprite.menuImage = pygame.image.load("../graphics/Menu/cassi2.jpg")
                    self.sprite.menuImage = ImageControl.fullScreen(self.window, self.sprite.menuImage)
                    self.sound.playSound("yeah")
                    pass
                elif event.key == pygame.K_t:
                    self.sprite.menuImage = pygame.image.load("../graphics/Menu/raul.jpg")
                    self.sprite.menuImage = ImageControl.fullScreen(self.window, self.sprite.menuImage)
                    self.sound.playSound("yeah")
                    pass
                elif event.key == pygame.K_m:
                    self.sprite.menuImage = pygame.image.load("../graphics/Menu/menu.jpg")
                    self.sprite.menuImage = ImageControl.fullScreen(self.window, self.sprite.menuImage)
                    pass


    def menuSelection(self, action):
        # testa se houve ação ou não
        if not action:
            return ""

        if action == "enter":
            self.sound.playSound("game_start")
            return self.choiceOptions[self.choiceKey]

        if action != "up" and action != "down":
            return ""

        self.fixoptions[self.choiceKey] = ImageControl.zoomImage(self.options[self.choiceKey], 0.8)

        if action == "up":
            self.sound.playSound("cursor_move")
            self.choiceKey -= 1
            if self.choiceKey < 0:
                self.choiceKey = 2

        elif action == "down":
            self.sound.playSound("cursor_move")
            self.choiceKey = (self.choiceKey + 1) % 3

        self.fixoptions[self.choiceKey] = ImageControl.zoomImage(self.options[self.choiceKey], 1.25)

        return ""
