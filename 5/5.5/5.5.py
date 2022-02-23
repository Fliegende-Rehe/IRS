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

x, y, z = hm[0][3], hm[1][3], hm[2][3]

n = int(file.readline())
zones = []
for i in range(n):
    zone = list(map(float, file.readline().split()))
    if zone[1] <= x <= zone[4] and zone[2] <= y <= zone[5] and zone[3] <= z <= zone[6]: zones.append(zone)

print(len(zones))

for i in range(len(zones)): print(int(zones[i][0]), end=" ")
