import math

while True:
    try:
        N = int(input())
        H, C, L = map(int, input().split())

        area_rampa = N * math.sqrt(H**2 + C**2) * L / 10000

        print('{:.4f}'.format(area_rampa))
    except EOFError:
        break