import pygame

defaultWidth = 1280


defaultHeight = 720


widthScale = 1
heightScale = 1


class ImageControl:
    def defineX(x, isFloat=False):
        if isFloat:
            return (x * widthScale)
        return int(x * widthScale)

    def defineY(y, isFloat=False):
        if isFloat:
            return y * heightScale
        return int(y * heightScale)

    def getWidthScale():
        return int(widthScale)

    def getHeightScale():
        return int(heightScale)

    def getWindowResolution():
        return defaultWidth, defaultHeight

    def definePosition(pos, default=False):
        if default:
            return int(int(pos[0]) * widthScale, int(pos[1]) * heightScale)
        return int(pos[0] * widthScale), int(pos[1] * heightScale)

    def setImageAt(window, image, pos):
        window.windowScreen.blit(image, ImageControl.definePosition(pos))

    def getScale():
        return widthScale, heightScale

    def setImageResolution(screenResolution):
        global widthScale
        widthScale = screenResolution[0] / defaultWidth
        global heightScale
        heightScale = screenResolution[1] / defaultHeight

    def zoomImage(image, zoomValue):
        w, h = image.get_size()
        return pygame.transform.scale(image, (int(zoomValue * w), int(zoomValue * h)))

    def centerImage(window, image, x=0, y=0):
        window.windowScreen.blit(image,
                                 ((window.windowScreen.get_width() // 2) - (image.get_width() // 2) + x,
                                  ((window.windowScreen.get_height() // 2) - (image.get_height() // 2) + y)
                                  ))

    def belowcenterImage(window, i, image):
        window.windowScreen.blit(image,
                                 (window.screenResolution[0] // 2 - (image.get_width() // 2),
                                  ((window.windowScreen.get_height() // 2) + 400 * i * image.get_height() // 720)
                                  ))

    def fixValues(x, y, default=False):
        if default:
            return int(ImageControl.defineX(x)), int(ImageControl.defineY(y))
        return ImageControl.defineX(x), ImageControl.defineY(y)

    def fixScale(image):
        w, h = image.get_size()
        return pygame.transform.scale(image, (int(widthScale * w), int(heightScale * h)))

    def fullScreen(window, image):
        w, h = image.get_size()
        x = window.screenResolution[0] / w
        y = window.screenResolution[1] / h
        return pygame.transform.scale(image, (int(w * x), int(h * y)))

    def repeatImage(window, image, getWindow):
        image = ImageControl.fixScale(image)
        if getWindow:
            x, y = window.screenResolution
        else:
            x, y = image.get_size()
        for i in range(0, defaultWidth, x // 2):
            for j in range(0, defaultHeight, y):
                window.windowScreen.blit(image, ImageControl.definePosition((i, j)))