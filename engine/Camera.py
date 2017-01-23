from pygame import *
from ImageControl import *

class Camera:
    def __init__(self, camera_func, dimensions):
        self.camera_func = camera_func
        self.dimensions = dimensions
        self.state = Rect(0, 0, dimensions[0], dimensions[1])

    def apply(self, target):        
        aux = target.rect.copy()
        aux.x = ImageControl.defineX(aux.x)
        aux.y = ImageControl.defineY(aux.y)

        return target.rect.move(self.state.topleft)

    def update(self, target):   
        self.state = self.camera_func(self.state, target.rect)
