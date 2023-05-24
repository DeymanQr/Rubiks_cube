# import math
from cube import Cube
from settings import CUBES_PADDING
from funcs import blacking, rotate


class RubiksCube:
    def __init__(self, centerx, centery, centerz, w, colors, alph, bet, gam):
        self.center = [centerx, centery, centerz]
        self.cubes = [
            Cube(centerx + (w//3+CUBES_PADDING) * (i % 3 - 1), centery + (w//3+CUBES_PADDING) * (i % 9 // 3 - 1),
                 centerz + (w//3+CUBES_PADDING) * (i // 9 - 1), w//3, colors, i, alph, bet, gam)
            for i in range(27)
        ]
        # self.basis = [
        #     Cube(centerx + (w // 3 + CUBES_PADDING) * (i % 3 - 1),
        #          centery + (w // 3 + CUBES_PADDING) * (i % 9 // 3 - 1),
        #          centerz + (w // 3 + CUBES_PADDING) * (i // 9 - 1), w // 3, blacking(colors, i), 0, 0)
        #     for i in range(27)
        # ]
        self.angles = [alph, bet, gam]

    @staticmethod
    def rtt(x, y, notclockwise=1):
        return -y*(notclockwise*2-1), x*(notclockwise*2-1)

    def rotate_facet(self, direction, num, notclockwise=1):
        if direction == 'x':
            a1, a2 = 0, 1
            for _ in range(3):
                b1, b2 = self.rtt(a1, a2, notclockwise)
                self.cubes[(a2 + 1) * 9 + (a1 + 1) * 3 + (num + 1)], self.cubes[(b2 + 1) * 9 + (b1 + 1) * 3 + (num + 1)]\
                    = self.cubes[(b2 + 1) * 9 + (b1 + 1) * 3 + (num + 1)], self.cubes[(a2 + 1) * 9 + (a1 + 1) * 3 + (num + 1)]
                for i in range(3):
                    self.cubes[(a2 + 1) * 9 + (a1 + 1) * 3 + (num + 1)].center[i], self.cubes[
                        (b2 + 1) * 9 + (b1 + 1) * 3 + (num + 1)].center[i] \
                        = self.cubes[(b2 + 1) * 9 + (b1 + 1) * 3 + (num + 1)].center[i], self.cubes[
                        (a2 + 1) * 9 + (a1 + 1) * 3 + (num + 1)].center[i]
                self.cubes[(a2 + 1) * 9 + (a1 + 1) * 3 + (num + 1)].rotate(direction, notclockwise)
                a1, a2 = b1, b2
            self.cubes[(a2 + 1) * 9 + (a1 + 1) * 3 + (num + 1)].rotate(direction, notclockwise)

            a1, a2 = 1, 1
            for _ in range(3):
                b1, b2 = self.rtt(a1, a2, notclockwise)
                self.cubes[(a2 + 1) * 9 + (a1 + 1) * 3 + (num + 1)], self.cubes[(b2 + 1) * 9 + (b1 + 1) * 3 + (num + 1)] \
                    = self.cubes[(b2 + 1) * 9 + (b1 + 1) * 3 + (num + 1)], self.cubes[
                    (a2 + 1) * 9 + (a1 + 1) * 3 + (num + 1)]
                for i in range(3):
                    self.cubes[(a2 + 1) * 9 + (a1 + 1) * 3 + (num + 1)].center[i], self.cubes[
                        (b2 + 1) * 9 + (b1 + 1) * 3 + (num + 1)].center[i] \
                        = self.cubes[(b2 + 1) * 9 + (b1 + 1) * 3 + (num + 1)].center[i], self.cubes[
                        (a2 + 1) * 9 + (a1 + 1) * 3 + (num + 1)].center[i]
                self.cubes[(a2 + 1) * 9 + (a1 + 1) * 3 + (num + 1)].rotate(direction, notclockwise)
                a1, a2 = b1, b2
            self.cubes[(a2 + 1) * 9 + (a1 + 1) * 3 + (num + 1)].rotate(direction, notclockwise)
        if direction == 'y':
            a1, a2 = 0, 1
            for _ in range(3):
                b1, b2 = self.rtt(a1, a2, notclockwise)
                self.cubes[(a2 + 1) * 9 + (num + 1) * 3 + (a1 + 1)], self.cubes[(b2 + 1) * 9 + (num + 1) * 3 + (b1 + 1)]\
                    = self.cubes[(b2 + 1) * 9 + (num + 1) * 3 + (b1 + 1)], self.cubes[(a2 + 1) * 9 + (num + 1) * 3 + (a1 + 1)]
                for i in range(3):
                    self.cubes[(a2 + 1) * 9 + (num + 1) * 3 + (a1 + 1)].center[i], self.cubes[
                        (b2 + 1) * 9 + (num + 1) * 3 + (b1 + 1)].center[i] \
                        = self.cubes[(b2 + 1) * 9 + (num + 1) * 3 + (b1 + 1)].center[i], self.cubes[
                        (a2 + 1) * 9 + (num + 1) * 3 + (a1 + 1)].center[i]
                self.cubes[(a2 + 1) * 9 + (num + 1) * 3 + (a1 + 1)].rotate(direction, notclockwise)
                a1, a2 = b1, b2
            self.cubes[(a2 + 1) * 9 + (num + 1) * 3 + (a1 + 1)].rotate(direction, notclockwise)

            a1, a2 = 1, 1
            for _ in range(3):
                b1, b2 = self.rtt(a1, a2, notclockwise)
                self.cubes[(a2 + 1) * 9 + (num + 1) * 3 + (a1 + 1)], self.cubes[(b2 + 1) * 9 + (num + 1) * 3 + (b1 + 1)] \
                    = self.cubes[(b2 + 1) * 9 + (num + 1) * 3 + (b1 + 1)], self.cubes[
                    (a2 + 1) * 9 + (num + 1) * 3 + (a1 + 1)]
                for i in range(3):
                    self.cubes[(a2 + 1) * 9 + (num + 1) * 3 + (a1 + 1)].center[i], self.cubes[
                        (b2 + 1) * 9 + (num + 1) * 3 + (b1 + 1)].center[i] \
                        = self.cubes[(b2 + 1) * 9 + (num + 1) * 3 + (b1 + 1)].center[i], self.cubes[
                        (a2 + 1) * 9 + (num + 1) * 3 + (a1 + 1)].center[i]
                self.cubes[(a2 + 1) * 9 + (num + 1) * 3 + (a1 + 1)].rotate(direction, notclockwise)
                a1, a2 = b1, b2
            self.cubes[(a2 + 1) * 9 + (num + 1) * 3 + (a1 + 1)].rotate(direction, notclockwise)
        if direction == 'z':
            a1, a2 = 0, 1
            for _ in range(3):
                b1, b2 = self.rtt(a1, a2, notclockwise)
                self.cubes[(num + 1) * 9 + (a2 + 1) * 3 + (a1 + 1)], self.cubes[(num + 1) * 9 + (b2 + 1) * 3 + (b1 + 1)]\
                    = self.cubes[(num + 1) * 9 + (b2 + 1) * 3 + (b1 + 1)], self.cubes[(num + 1) * 9 + (a2 + 1) * 3 + (a1 + 1)]
                for i in range(3):
                    self.cubes[(num + 1) * 9 + (a2 + 1) * 3 + (a1 + 1)].center[i], self.cubes[
                        (num + 1) * 9 + (b2 + 1) * 3 + (b1 + 1)].center[i] \
                        = self.cubes[(num + 1) * 9 + (b2 + 1) * 3 + (b1 + 1)].center[i], self.cubes[
                        (num + 1) * 9 + (a2 + 1) * 3 + (a1 + 1)].center[i]
                self.cubes[(num + 1) * 9 + (a2 + 1) * 3 + (a1 + 1)].rotate(direction, notclockwise)
                a1, a2 = b1, b2
            self.cubes[(num + 1) * 9 + (a2 + 1) * 3 + (a1 + 1)].rotate(direction, notclockwise)

            a1, a2 = 1, 1
            for _ in range(3):
                b1, b2 = self.rtt(a1, a2, notclockwise)
                self.cubes[(num + 1) * 9 + (a2 + 1) * 3 + (a1 + 1)], self.cubes[(num + 1) * 9 + (b2 + 1) * 3 + (b1 + 1)] \
                    = self.cubes[(num + 1) * 9 + (b2 + 1) * 3 + (b1 + 1)], self.cubes[
                    (num + 1) * 9 + (a2 + 1) * 3 + (a1 + 1)]
                for i in range(3):
                    self.cubes[(num + 1) * 9 + (a2 + 1) * 3 + (a1 + 1)].center[i], self.cubes[
                        (num + 1) * 9 + (b2 + 1) * 3 + (b1 + 1)].center[i] \
                        = self.cubes[(num + 1) * 9 + (b2 + 1) * 3 + (b1 + 1)].center[i], self.cubes[
                        (num + 1) * 9 + (a2 + 1) * 3 + (a1 + 1)].center[i]
                self.cubes[(num + 1) * 9 + (a2 + 1) * 3 + (a1 + 1)].rotate(direction, notclockwise)
                a1, a2 = b1, b2
            self.cubes[(num + 1) * 9 + (a2 + 1) * 3 + (a1 + 1)].rotate(direction, notclockwise)

    def update(self, dx, dy, dz):
        self.angles = [(j + (dx, dy, dz)[i]) % 360 for i, j in enumerate(self.angles)]
        for cube in self.cubes:
            # cube.center = [j + self.center[i] for i, j in enumerate(rotate([cube.center[i]-self.center[i] for i in range(3)], dx*math.pi/180, dy*math.pi/180, dz*math.pi/180))]
            cube.update(dx, dy, dz)

    def render(self, sc, camera):
        # self.cubes.sort(key=lambda cube: -cube.center[2])
        for cube in sorted(self.cubes, key=lambda cube: -([j + self.center[i] for i, j in enumerate(rotate([cube.center[i]-self.center[i] for i in range(3)], *self.angles))][2]))[2:]:
            cube.render(sc, self.center, self.angles, camera)
