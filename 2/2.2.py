from math import sin, cos, pi
from numpy import set_printoptions, array

set_printoptions(precision=3, suppress=True)

try: file = open("input.txt")
except FileNotFoundError: from sys import stdin as file

def rotation_matrix(ax, an):
    an *= pi / 180
    if ax == 'x': m = [[1, 0, 0, 0], [0, cos(an), -sin(-an), 0], [0, sin(-an), cos(an), 0], [0, 0, 0, 1]]
    elif ax == 'y': m = [[cos(an), 0, sin(an), 0], [0, 1, 0, 0], [-sin(an), 0, cos(an), 0], [0, 0, 0, 1]]
    else: m = [[cos(an), -sin(-an), 0, 0], [sin(-an), cos(an), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    return array(m)

def transition_matrix(ax, dis):
    m = [[1, 0, 0, dis if ax == 'x' else 0],
         [0, 1, 0, dis if ax == 'y' else 0],
         [0, 0, 1, dis if ax == 'z' else 0],
         [0, 0, 0, 1]]
    return array(m)

rmd = list(map(int, file.readline().split()))
rma = ['z', 'y', 'y', 'x', 'y', 'x']

tmd = [25, 400, 560, 35, 515, 80]
tma = ['x', 'z', 'x', 'z', 'x', 'x']

hm = rotation_matrix(rma[0], rmd[0]) @ transition_matrix(tma[0], tmd[0])
for i in range(1, 6): hm = hm @ transition_matrix(tma[i], tmd[i]) @ rotation_matrix(rma[i], rmd[i])

for i in range(3): print(int(hm[i][3]), end=' ')

xx, yy, zz = 0, 0, 0
for j in range(6):
    if rma[j] == 'x': xx += rmd[j]
    elif rma[j] == 'y': yy += rmd[j]
    else: zz += rmd[j]
print(-xx, yy if yy == 0 else yy - 1, -zz)
