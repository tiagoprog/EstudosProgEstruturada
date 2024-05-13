C, P, F = map(int, input().split())

total_folhas_necessarias = C * F

if total_folhas_necessarias <= P:
    print('S')
else:
    print('N')