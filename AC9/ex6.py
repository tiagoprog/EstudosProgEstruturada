def calcular_distancia(tempo, velocidade):
    return tempo * velocidade

N = int(input())

distancia_total = 0

for _ in range(N):
    tempo, velocidade = map(int, input().split())
    distancia_total += calcular_distancia(tempo, velocidade)
print(distancia_total)
