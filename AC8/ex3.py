def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

while True:
    try:
        M, N = map(int, input().split())
        soma = fatorial(M) + fatorial(N)
        print(soma)
    except EOFError:
        break