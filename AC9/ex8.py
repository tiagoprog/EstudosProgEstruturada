N = int(input())

sequencia = []
for _ in range(N):
    sequencia.append(int(input()))

numeros_marcados = 1   

for i in range(1, N):
    if sequencia[i] != sequencia[i - 1]:
        numeros_marcados += 1
print(numeros_marcados)