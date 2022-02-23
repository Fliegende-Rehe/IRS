from math import pi, acos, atan2
from numpy import sign

try: file = open("input.txt")
except FileNotFoundError: from sys import stdin as file

def get_line(): return list(map(float, file.readline().split()))
def spin(n): return n - pi * 2 * sign(n) if pi < abs(n) else n
def spinner(n): return list(map(lambda j: spin(j), n))
def cosine_rule(m, n, p): return acos((n ** 2 + p ** 2 - m ** 2) / (2 * n * p))

L1, L2, L3 = get_line()
ac, bc, cc = [get_line() for x in range(3)]
x, y = get_line()
x -= L3

H = (x ** 2 + y ** 2) ** 0.5
P = atan2(y, x)

a1 = cosine_rule(L2, L1, H)
a = spinner([P - a1, P + a1])

b1 = cosine_rule(H, L1, L2)
b = spinner([pi - b1, b1 - pi])

c1 = pi - a1 - b1
c = spinner([-c1 - P, c1 - P])

res = ["None"]
MIN, MAX = 0, 1
for i in range(2):
    a[i], b[i], c[i] = map(lambda j: round(j, 5), [a[i], b[i], c[i]])
    if ac[MIN] <= a[i] <= ac[MAX]:
        if bc[MIN] <= b[i] <= bc[MAX]:
            if cc[MIN] <= c[i] <= cc[MAX]:
                res = a[i], b[i], c[i]
                break
print(*res)
