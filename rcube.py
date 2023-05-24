import math
from cube import Cube
from settings import SPEED_COEF_X, SPEED_COEF_Y, CUBES_PADDING
from funcs import blacking, rotate


class RubiksCube:
    def __init__(self, centerx, centery, centerz, w, colors, alph, bet, gam):
        self.center = [centerx, centery, centerz]
        self.cubes = [
            Cube(centerx + (w//3+CUBES_PADDING) * (i % 3 - 1), centery + (w//3+CUBES_PADDING) * (i % 9 // 3 - 1),
                 centerz + (w//3+CUBES_PADDING) * (i // 9 - 1), w//3, blacking(colors, i), 0, 0)
            for i in range(27)
        ]
        # self.basis = [
        #     Cube(centerx + (w // 3 + CUBES_PADDING) * (i % 3 - 1),
        #          centery + (w // 3 + CUBES_PADDING) * (i % 9 // 3 - 1),
        #          centerz + (w // 3 + CUBES_PADDING) * (i // 9 - 1), w // 3, blacking(colors, i), 0, 0)
        #     for i in range(27)
        # ]
        self.update(alph * math.pi / SPEED_COEF_X / 180, bet * math.pi / SPEED_COEF_Y / 180, gam * math.pi / 180)

    @staticmethod
    def rtt(x, y, notclockwise=1):
        return -y * (notclockwise * 2 - 1), x * (notclockwise * 2 - 1)

    def rotate_facet(self, direction, num, notclockwise=1):
        if direction == 'x':
            a1, a2 = 0, 1
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
        for cube in self.cubes:
            # bss = [cube.center[i]-self.center[i] for i in range(3)]
            # bss = [cube.center[i] for i in range(3)]
            # bss = [bss[0] * math.cos(dx*SPEED_COEF_X) - bss[2] * math.sin(dx*SPEED_COEF_X), bss[1],
            #        bss[2] * math.cos(dx*SPEED_COEF_X) + bss[0] * math.sin(dx*SPEED_COEF_X)]
            # bss = [bss[0], bss[1] * math.cos(dy*SPEED_COEF_Y) + bss[2] * math.sin(dy*SPEED_COEF_Y),
            #        bss[2] * math.cos(dy*SPEED_COEF_Y) - bss[1] * math.sin(dy*SPEED_COEF_Y)]
            # bss = [bss[0] * math.cos(dz) - bss[1] * math.sin(dz), bss[1] * math.cos(dz) + bss[0] * math.sin(dz), bss[2]]
            # cube.center = [bss[i]+self.center[i] for i in range(3)]
            cube.center = [j + self.center[i] for i, j in enumerate(rotate([cube.center[i]-self.center[i] for i in range(3)], dx*SPEED_COEF_X, dy*SPEED_COEF_Y, dz))]
            # cube.center = bss
            cube.update(dx, dy, dz)

    def render(self, sc, camera):
        # self.cubes.sort(key=lambda cube: -cube.center[2])
        for cube in sorted(self.cubes, key=lambda cube: -cube.center[2])[2:]:
            cube.render(sc, camera)
