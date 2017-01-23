import pygame
import pygame.freetype
import sys
import functools
from Window import *
from Control import *
from ImageControl import *
from stages.Menu import *
from stages.Stage1 import *
from stages.Stage2 import *
from stages.Stage3 import *
from stages.Intro import *
from stages.Intro_1 import *
from stages.Intro_2 import *
from stages.Intro_3 import *
from stages.Intro_4 import *
from stages.Ameaca_1 import *
from stages.Ameaca_2 import *
from stages.Ameaca_3 import *
from stages.Intro_Stage1 import *
from stages.Intro_Stage2 import *
from stages.Intro_Stage3 import *
from stages.Intro_Bolha import *
from stages.Map import *
from stages.Map2 import *
from stages.Map3 import *
from stages.Options import *
from Fonts import *
from Character import *
from Sprite import *
from Sound import *
from ObjectsLoaded import *


class SceneController:
    def __init__(self):
        self.actualScene = "Menu"
        pygame.init()
        self.window = Window()
        self.controller = Control()
        self.sound = Sound()
        self.player = Character(self.controller, self.sound)
        self.sprite = Sprite()
        self.phases = []
        self.objects = ObjectsLoaded()
        self.fonts = Fonts()
        self.objscene = Menu(self.controller, self.window, self.sound, self.player, self.sprite,
            self.fonts, self.objects)
        self.update()

    def str_to_class(self, str):
        return functools.reduce(getattr, str.split("."), sys.modules[__name__])

    def searchScene(self, word):
        for i in range(0, len(self.phases)):
            if self.phases[i].name == word:
                return i
        return -1

    def update(self):
        while (True):
            proxClass, check_destroy, check_changes = self.objscene.update()
            if proxClass == "Quit":
                sys.exit()
            if (self.searchScene(self.actualScene) < 0 and not check_destroy):
                # adicionando na lista de fases passadas
                self.phases.append(self.objscene)
            aux = self.searchScene(proxClass)
            if (aux >= 0):
                self.objscene = self.phases[aux]
                if check_changes:
                    self.objscene.resizeImages()
            else:
                # instanciando nova classe
                metamorfa = self.str_to_class(proxClass)
                self.objscene = metamorfa(self.controller, self.window, self.sound, self.player, self.sprite,
                                          self.fonts, self.objects)

            # atualizando cena atual
            self.actualScene = proxClass
