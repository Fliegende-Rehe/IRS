import numpy as np
from math import asin, atan2, cos, pi

try: file = open("input.txt")
except FileNotFoundError: from sys import stdin as file

def toMatrix(array):
    matrix = []
    for i in range(0, len(array), int(len(array) ** 0.5)):
        row = []
        for j in range(i, i + int(len(array) ** 0.5)): row.append(array[j])
        matrix.append(row)
    return np.array(matrix)

def getAngles(rm):
    if rm[2][0] != -1 and rm[2][0] != 1:
        y = [asin(rm[2][0]), -pi - asin(rm[2][0])]
        x = [-atan2(rm[2][1] / cos(y[0]), rm[2][2] / cos(y[0])), atan2(rm[2][1] / cos(y[1]), rm[2][2] / cos(y[1]))]
        z = [-atan2(rm[1][0] / cos(y[0]), rm[0][0] / cos(y[0])), atan2(rm[1][0] / cos(y[1]), rm[0][0] / cos(y[1]))]
    else:
        z = 0
        if rm[2][0] == -1: x, y = z + atan2(rm[0][1], rm[0][2]), pi / 2
        else: x, y = -z + atan2(-rm[0][1], -rm[0][2]), -pi / 2
    return [x, y, z]

def write(array, j):
    for i in range(3):
        print(round(array[i][j], 3), end=' ')

tr = toMatrix(list(map(float, file.readline().split())))
tf = toMatrix(list(map(float, file.readline().split())))
tt = np.linalg.inv(tr) @ tf
write(tt, 3)
tt_rm = tt[0:3, 0:3]
angles = getAngles(tt_rm.transpose())
write(angles, 0)
