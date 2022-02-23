from math import acos, atan2, pi, degrees

try: file = open("input.txt")
except FileNotFoundError: from sys import stdin as file

x, y, z = map(int, file.readline().split())
L1, L2, L3 = 225, 275, 200
H = (x * x + y * y) ** 0.5

try: a = acos((L1 ** 2 + H ** 2 - L2 ** 2) / (2 * L1 * H))
except ValueError: a = 0
a = round(degrees(atan2(y, x) - a))

try: b = acos((L1 ** 2 + L2 ** 2 - H ** 2) / (2 * L1 * L2))
except ValueError: b = pi
b = round(degrees(pi - b))

c = z - L3

print(a, b, c, 0)
