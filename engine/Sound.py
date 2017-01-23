import pygame


class Sound:
    def __init__(self):
        pygame.mixer.init()
        self.soundVolume = 1.00
        self.soundList = {}

    def str_to_atrib(self, str):
        return functools.reduce(getattr, str.split("."), sys.modules[__name__])

    def playSound(self, soundname):
        track_number = self.soundList[soundname]
        track_number.play()

    def stopSound(self, soundname):
        track_number = self.soundList[soundname]
        track_number.stop()

    def soundMenu(self):
        self.sound_cursor_move = pygame.mixer.Sound("../sound/soundeffect/Menu/cursor_move2.wav")
        self.sound_cursor_back = pygame.mixer.Sound("../sound/soundeffect/Menu/cursor_back2.wav")
        self.sound_game_start = pygame.mixer.Sound("../sound/soundeffect/Menu/game_start2.wav")
        self.sound_game_fail = pygame.mixer.Sound("../sound/soundeffect/fail.wav")
        self.sound_game_quack = pygame.mixer.Sound("../sound/soundeffect/quack.wav")
        self.sound_game_yeah = pygame.mixer.Sound("../sound/soundeffect/yeah.wav")
        self.sound_game_jump = pygame.mixer.Sound("../sound/soundeffect/jump.wav")
        self.soundList["cursor_move"] = self.sound_cursor_move
        self.soundList["cursor_back"] = self.sound_cursor_back
        self.soundList["game_start"] = self.sound_game_start
        self.soundList["fail"] = self.sound_game_fail
        self.soundList["quack"] = self.sound_game_quack
        self.soundList["yeah"] = self.sound_game_yeah
        self.soundList["jump"] = self.sound_game_jump

    def soundStage1(self):
        self.sound_pop = pygame.mixer.Sound("../sound/soundeffect/pop.wav")
        self.soundList["pop"] = self.sound_pop

    def soundStage7(self):
        self.sound_pop = pygame.mixer.Sound("../sound/soundeffect/pop.wav")
        self.soundList["pop"] = self.sound_pop

    def soundIntro_2(self):
        self.sound_engine = pygame.mixer.Sound("../sound/soundeffect/engine.wav")
        self.soundList["engine"] = self.sound_engine

    def soundMap(self):
        self.sound_nextstage = pygame.mixer.Sound("../sound/soundeffect/nextstage.wav")
        self.soundList["nextstage"] = self.sound_nextstage
