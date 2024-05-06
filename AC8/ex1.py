def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def max_figurinhas(f1, f2):
    return mdc(f1, f2)

n = int(input())

for _ in range(n):
    f1, f2 = map(int, input().split())
    print(max_figurinhas(f1, f2))