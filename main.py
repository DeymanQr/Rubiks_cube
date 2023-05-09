# import math

import pygame
from settings import *
from camera import Camera
from mouse_handler import MouseHaldler
# from cube import Cube
from rcube import RubiksCube

sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# cubes = [Cube(WIDTH//2, HEIGHT//2, 0, CUBES_W, ('w', 'b', 'o', 'y', 'g', 'r'), -45, -30)]
rcube = RubiksCube(WIDTH//2, HEIGHT//2, HEIGHT//2, RCUBE_W, ('w', 'b', 'o', 'y', 'g', 'r'), -45, -30, 0)
camera = Camera(WIDTH//2, HEIGHT//2, 100-WIDTH, 100)
mhandler = MouseHaldler()

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.MOUSEWHEEL:
            camera.coords[2] += e.y * SPEED_COEF_Z
            camera.plane += e.y * SPEED_COEF_Z
            if camera.coords[2] >= -CUBES_W*5 or camera.coords[2] <= -CUBES_W*15:
                camera.coords[2] -= e.y * SPEED_COEF_Z
                camera.plane -= e.y * SPEED_COEF_Z
    # c.update(0, 1)
    # mhandler.update_cubes(cubes)
    mhandler.update_cubes(rcube)
    camera.update()
    sc.fill(BLACK)
    # for cube in cubes:
    #     cube.render(sc, camera)
    rcube.render(sc, camera)
    pygame.display.update()
    clock.tick(FPS)
