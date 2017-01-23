import os, pygame


class Template:
    def __init__(self, className, loadImages=True):
        self.imgs = []
        self.imgsNames = self.get_directory(className)

        if loadImages:
            self.load_images(className)

    def get_directory(self, path):
        return sorted(os.listdir("../graphics/" + path))

    def load_images(self, path):
        for i in range(0, len(self.imgsNames)):
            self.imgs.append(pygame.image.load("../graphics/" + path + "/" + self.imgsNames[i]).convert_alpha())
