class Options:
    def __init__(self):
        pass

    def load_images(self):
        self.options = [pygame.image.load("../graphics/Menu/res" + str(i) + ".png").convert_alpha() for i in
                        range(1, 4)]

    def changeResolution(self):
        pass

    def update(self):
        pass

    def changeVolume(self):
        pass
