from math import sin, cos

try: file = open("input.txt")
except FileNotFoundError: from sys import stdin as file

def intersection(p0, p1):
    x, y = 0, 1
    s1, s2 = [p0[1][x] - p0[0][x], p0[1][y] - p0[0][y]], [p1[1][x] - p1[0][x], p1[1][y] - p1[0][y]]
    s = (s1[x] * (p0[0][y] - p1[0][y]) - s1[y] * (p0[0][x] - p1[0][x])) / (s1[x] * s2[y] - s2[x] * s1[y])
    t = (s2[x] * (p0[0][y] - p1[0][y]) - s2[y] * (p0[0][x] - p1[0][x])) / (s1[x] * s2[y] - s2[x] * s1[y])
    if 0 <= s <= 1 and 0 <= t <= 1: return [p0[0][x] + (t * s1[x]), p0[0][y] + (t * s1[y])]
    return []

def getHinges(N):
    h = [[0, 0]]
    slope = 0
    for i in range(N):
        length, angle = list(map(float, file.readline().split()))
        angle += slope
        h.append([h[i][0] + length * cos(angle), h[i][1] + length * sin(angle)])
        slope = angle
    return h

def getIntersection(hinges):
    points = []
    for i in range(len(hinges) - 1):
        s0 = [[hinges[i][0], hinges[i][1]], [hinges[i + 1][0], hinges[i + 1][1]]]
        for j in range(i + 2, len(hinges) - 1):
            if j == i: continue
            s1 = [[hinges[j][0], hinges[j][1]], [hinges[j + 1][0], hinges[j + 1][1]]]
            int_point = intersection(s0, s1)
            if int_point: points.append(list(map(float, int_point)))
    return points

N = int(file.readline())
hinges = getHinges(N)
intersections = getIntersection(hinges)
print(len(intersections))
for i in range(len(intersections)):
    for j in range(2):
        intersections[i][j] = round(intersections[i][j], 6)
        print(intersections[i][j], end=" ")
    print()
