import pygame
# from rcube import RubiksCube


class MouseHaldler:
    def __init__(self):
        self.mouse = pygame.mouse.get_pos()
        self.sx, self.sy = 0, 0

    def update_cubes(self, obj):
        ms = pygame.mouse.get_pos()
        try:
            for cube in obj:
                cube.update(self.sx, self.sy)
        except TypeError:
            obj.update(self.sx, self.sy, 0)
        if pygame.mouse.get_pressed()[0]:
            self.sx, self.sy = ms[0]-self.mouse[0], ms[1]-self.mouse[1]
        else:
            self.sx *= .9
            self.sy *= .9
        self.mouse = ms
