import pygame
import math
from settings import COLORS
from camera import ThreeD, Camera
from funcs import rotate, blacking


class Facet:
    def __init__(self, coords, color):
        self.coords = coords
        self.color = color

    # @property
    def get_dist(self, center, angles, camera: Camera):
        # return (self.coords[0][2] + self.coords[2][2])/2
        rect = [rotate(j, *angles) for j in self.coords]
        return math.sqrt(((rect[0][0] + rect[2][0]) / 2 + center[0] - camera.coords[0])**2 +
                         ((rect[0][1] + rect[2][1]) / 2 + center[1] - camera.coords[1])**2 +
                         ((rect[0][2] + rect[2][2]) / 2 + center[2] - camera.coords[2])**2
                         )

    # def update(self, dx, dy, dz):
    #     for i in range(len(self.coords)):
    #         self.coords[i] = rotate(self.coords[i], dx*math.pi/180, dy*math.pi/180, dz*math.pi/180)

    def facet_poly(self, center, angles, camera):
        return ThreeD.get2d(camera, [[i[0] + center[0], i[1] + center[1], i[2] + center[2]] for i in tuple(rotate(j, *angles) for j in self.coords)])

    def render(self, center, angles, sc, camera):
        pygame.draw.polygon(sc, COLORS[self.color], self.facet_poly(center, angles, camera))


class Cube:
    rtt = {'x': (0, 1, 3, 4), 'y': (1, 2, 4, 5), 'z': (0, 5, 3, 2)}

    def __init__(self, centerx, centery, centerz, w, colors, i, alph, bet, gam):
        self.center = [centerx, centery, centerz]
        self.i = i
        self.colors = blacking(colors, i)
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
        self.angles = [alph, bet, gam]

    # def getcube(self):
        # print(self.basises + [[-j for j in i] for i in self.basises])
        # return ((self.center[0] + basis[0], self.center[1] + basis[1], self.center[2] + basis[2]) for basis in self.basises + [[-j for j in i] for i in self.basises])

    def update(self, dx, dy, dz):
        self.angles = [(self.angles[0] + dx) % 360, (self.angles[1] + dy) % 360, (self.angles[2] + dz) % 360]
        # for f in self.facetes:
        #     f.update(dx, dy, dz)

    def rotate(self, axis, notclockwise):
        # 1 -> range(1, 4, 1)
        # -1 -> range(3, 0, -1)
        for i in range(3-2*notclockwise, 4*notclockwise, notclockwise*2-1):
            self.colors[Cube.rtt[axis][i-1]], self.colors[Cube.rtt[axis][i]] = self.colors[Cube.rtt[axis][i]], self.colors[Cube.rtt[axis][i-1]]

        for i, j in enumerate(self.facetes):
            j.color = self.colors[i]

    def render(self, sc, center, angles, camera):
        # poly = ThreeD.get2d(camera, self.getcube())
        # for i in range(4):
        #     pygame.draw.line(sc, WHITE, poly[(i - 1) % 4], poly[i])
        # for i in range(4, 8):
        #     pygame.draw.line(sc, WHITE, poly[(i - 5) % 4 + 4], poly[i])
        # for i in range(4):
        #     pygame.draw.line(sc, WHITE, poly[i], poly[(i - 6) % 4 + 4])
        for facet in sorted(self.facetes, key=lambda facet: -facet.get_dist(self.center, self.angles, camera))[3:]:
            facet.render([j + center[i] for i, j in enumerate(rotate([self.center[i]-center[i] for i in range(3)], *angles))],
                         self.angles, sc, camera)
        # for i in range(3):
        #     self.facetes[2-i].render(self.center, sc, camera)
