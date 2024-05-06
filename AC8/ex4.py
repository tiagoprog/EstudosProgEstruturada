def calcular_dias_comida(C):
    dias = 0
    while C > 1:
        C = C / 2
        dias += 1
    return dias

N = int(input())

for _ in range(N):
    C = float(input())
    
    dias = calcular_dias_comida(C)
    print(f"{dias} dias")