def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

n = int(input())

if 0 < n < 13:
    resultado = calcular_fatorial(n)
    print(resultado)
else:
    print("O valor de N deve estar entre 1 e 12.")
    