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
