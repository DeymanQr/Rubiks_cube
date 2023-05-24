import pygame
import math
from settings import SPEED_COEF_X, SPEED_COEF_Y, COLORS
from camera import ThreeD, Camera
from funcs import rotate


class Facet:
    def __init__(self, coords, color):
        self.coords = coords
        self.color = color

    # @property
    def get_dist(self, center, camera: Camera):
        # return (self.coords[0][2] + self.coords[2][2])/2
        return math.sqrt(((self.coords[0][0] + self.coords[2][0]) / 2 + center[0] - camera.coords[0])**2 +
                         ((self.coords[0][1] + self.coords[2][1]) / 2 + center[1] - camera.coords[1])**2 +
                         ((self.coords[0][2] + self.coords[2][2]) / 2 + center[2] - camera.coords[2])**2
                         )

    def update(self, dx, dy, dz):
        dx *= SPEED_COEF_X
        dy *= SPEED_COEF_Y
        for i in range(len(self.coords)):
            # bss = [self.coords[i][0] * math.cos(dx) - self.coords[i][2] * math.sin(dx), self.coords[i][1],
            #        self.coords[i][2] * math.cos(dx) + self.coords[i][0] * math.sin(dx)]
            # bss = [bss[0], bss[1] * math.cos(dy) + bss[2] * math.sin(dy), bss[2] * math.cos(dy) - bss[1] * math.sin(dy)]
            # bss = [bss[0] * math.cos(dz) - bss[1] * math.sin(dz), bss[1] * math.cos(dz) + bss[0] * math.sin(dz), bss[2]]
            self.coords[i] = rotate(self.coords[i], dx, dy, dz)

    def facet_poly(self, center, camera):
        return ThreeD.get2d(camera, [[i[0] + center[0], i[1] + center[1], i[2] + center[2]] for i in self.coords])

    def render(self, center, sc, camera):
        pygame.draw.polygon(sc, COLORS[self.color], self.facet_poly(center, camera))


class Cube:
    rtt = {'x': (0, 1, 3, 4), 'y': (1, 2, 4, 5), 'z': (0, 2, 3, 5)}

    def __init__(self, centerx, centery, centerz, w, colors, alph, bet):
        self.center = [centerx, centery, centerz]
        self.colors = colors
        # self.width = w
        # self.basises = [[w//2, -w//2, -w//2], [w//2, -w//2, w//2], [-w//2, -w//2, w//2], [-w//2, -w//2, -w//2]]
        self.facetes = [
            Facet([[w//2, -w//2, -w//2], [w//2, -w//2, w//2], [-w//2, -w//2, w//2], [-w//2, -w//2, -w//2]], self.colors[0]),
            Facet([[w//2, w//2, -w//2], [w//2, -w//2, -w//2], [-w//2, -w//2, -w//2], [-w//2, w//2, -w//2]], self.colors[1]),
            Facet([[w//2, w//2, w//2], [w//2, -w//2, w//2], [w//2, -w//2, -w//2], [w//2, w//2, -w//2]], self.colors[2]),
            Facet([[w//2, w//2, -w//2], [w//2, w//2, w//2], [-w//2, w//2, w//2], [-w//2, w//2, -w//2]], self.colors[3]),
            Facet([[-w//2, w//2, w//2], [-w//2, -w//2, w//2], [w//2, -w//2, w//2], [w//2, w//2, w//2]], self.colors[4]),
            Facet([[-w//2, w//2, -w//2], [-w//2, -w//2, -w//2], [-w//2, -w//2, w//2], [-w//2, w//2, w//2]], self.colors[5])
        ]
        self.update(alph*math.pi/SPEED_COEF_X/180, bet*math.pi/SPEED_COEF_Y/180, 0)

    # def getcube(self):
        # print(self.basises + [[-j for j in i] for i in self.basises])
        # return ((self.center[0] + basis[0], self.center[1] + basis[1], self.center[2] + basis[2]) for basis in self.basises + [[-j for j in i] for i in self.basises])

    def rotate(self, axis, notclockwise):
        # 1 -> range(1, 4, 1)
        # -1 -> range(3, 0, -1)
        for i in range(3 - 2 * notclockwise, 4 * notclockwise, notclockwise * 2 - 1):
            self.colors[Cube.rtt[axis][i - 1]], self.colors[Cube.rtt[axis][i]] = self.colors[Cube.rtt[axis][i]], \
                                                                                 self.colors[Cube.rtt[axis][i - 1]]

        for i, j in enumerate(self.facetes):
            j.color = self.colors[i]

    def update(self, dx, dy, dz):
        # dx *= SPEED_COEF_X
        # dy *= SPEED_COEF_Y
        # for i in range(len(self.basises)):
        #     bss = [self.basises[i][0] * math.cos(dx) - self.basises[i][2] * math.sin(dx), self.basises[i][1],
        #            self.basises[i][2] * math.cos(dx) + self.basises[i][0] * math.sin(dx)]
        #     bss = [bss[0], bss[1] * math.cos(dy) + bss[2] * math.sin(dy), bss[2] * math.cos(dy) - bss[1] * math.sin(dy)]
        #     self.basises[i] = bss
        for f in self.facetes:
            f.update(dx, dy, dz)

    def render(self, sc, camera):
        # poly = ThreeD.get2d(camera, self.getcube())
        # for i in range(4):
        #     pygame.draw.line(sc, WHITE, poly[(i - 1) % 4], poly[i])
        # for i in range(4, 8):
        #     pygame.draw.line(sc, WHITE, poly[(i - 5) % 4 + 4], poly[i])
        # for i in range(4):
        #     pygame.draw.line(sc, WHITE, poly[i], poly[(i - 6) % 4 + 4])
        for facet in sorted(self.facetes, key=lambda facet: -facet.get_dist(self.center, camera))[3:]:
            facet.render(self.center, sc, camera)
        # for i in range(3):
        #     self.facetes[2-i].render(self.center, sc, camera)
