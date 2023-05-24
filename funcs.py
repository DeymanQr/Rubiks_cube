import math


def blacking(colors, i):
    return [
        (colors[0], '', '')[i % 9 // 3],
        (colors[1], '', '')[i // 9],
        ('', '', colors[2])[i % 3],
        ('', '', colors[3])[i % 9 // 3],
        ('', '', colors[4])[i // 9],
        (colors[5], '', '')[i % 3],
    ]


def rotate(el, dx, dy, dz):
    bss = [el[0] * math.cos(dx) - el[2] * math.sin(dx), el[1],
           el[2] * math.cos(dx) + el[0] * math.sin(dx)]
    bss = [bss[0], bss[1] * math.cos(dy) + bss[2] * math.sin(dy), bss[2] * math.cos(dy) - bss[1] * math.sin(dy)]
    bss = [bss[0] * math.cos(dz) - bss[1] * math.sin(dz), bss[1] * math.cos(dz) + bss[0] * math.sin(dz), bss[2]]
    return bss
