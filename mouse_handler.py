import pygame
from settings import SPEED_COEF_X, SPEED_COEF_Y
# from rcube import RubiksCube


class MouseHaldler:
    def __init__(self):
        self.mouse = pygame.mouse.get_pos()
        self.sx, self.sy = 0, 0

    def update_cubes(self, obj):
        ms = pygame.mouse.get_pos()
        try:
            for cube in obj:
                cube.update(self.sx*SPEED_COEF_X, self.sy*SPEED_COEF_Y, 0)
        except TypeError:
            obj.update(self.sx*SPEED_COEF_X, self.sy*SPEED_COEF_Y, 0)
        if pygame.mouse.get_pressed()[0]:
            self.sx, self.sy = ms[0]-self.mouse[0], ms[1]-self.mouse[1]
        else:
            self.sx *= .9
            self.sy *= .9
        self.mouse = ms
