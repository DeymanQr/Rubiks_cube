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
    bss = [el[0] * math.cos(dx*math.pi/180) - el[2] * math.sin(dx*math.pi/180), el[1],
           el[2] * math.cos(dx*math.pi/180) + el[0] * math.sin(dx*math.pi/180)]
    bss = [bss[0], bss[1] * math.cos(dy*math.pi/180) + bss[2] * math.sin(dy*math.pi/180), bss[2] * math.cos(dy*math.pi/180) - bss[1] * math.sin(dy*math.pi/180)]
    bss = [bss[0] * math.cos(dz*math.pi/180) - bss[1] * math.sin(dz*math.pi/180), bss[1] * math.cos(dz*math.pi/180) + bss[0] * math.sin(dz*math.pi/180), bss[2]]
    return bss
