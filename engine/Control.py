import pygame
import sys


class Control:
    def checkKey(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit()

            if pygame.key.get_pressed()[pygame.K_UP]:
                return "up"
            elif (pygame.key.get_pressed()[pygame.K_DOWN]):
                return "down"
            elif (pygame.key.get_pressed()[pygame.K_LEFT]):
                return "left"
            elif (pygame.key.get_pressed()[pygame.K_RIGHT]):
                return "right"
            elif (pygame.key.get_pressed()[pygame.K_RETURN]):
                return "enter"
            elif (pygame.key.get_pressed()[pygame.K_a]):
                return "a"
            elif (pygame.key.get_pressed()[pygame.K_s]):
                return "s"
            elif (pygame.key.get_pressed()[pygame.K_d]):
                return "d"
            elif (pygame.key.get_pressed()[pygame.K_w]):
                return "w"
            elif (pygame.key.get_pressed()[pygame.K_SPACE]):
                return "space"

        return ""

    def checkPressed(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "space"
                elif event.key == pygame.K_RIGHT:
                    return "right"
                elif event.key == pygame.K_LEFT:
                    return "left"
                elif event.key == pygame.K_UP:
                    return "up"
                elif event.key == pygame.K_DOWN:
                    return "down"
                elif event.key == pygame.K_z:
                    return "z"
                    
