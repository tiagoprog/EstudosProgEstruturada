from collections import Counter
import sys

def calcular_fracao_populacao(arvores):

    total_arvores = len(arvores)
    contagem_arvores = Counter(arvores)
    especies_unicas = sorted(contagem_arvores.keys())

    for especie in especies_unicas:
        fracao = contagem_arvores[especie] / total_arvores * 100

        print(f"{especie} {fracao:.4f}")

def processar_casos_teste():
    num_casos = int(input())
    input()

    for i in range(num_casos):
        arvores = []
        while True:
            try:
                arvore = input().strip()
                if not arvore:
                    break
                arvores.append(arvore)
            except EOFError:
                break

        calcular_fracao_populacao(arvores)
        if i != num_casos - 1:
            print()

try:
    processar_casos_teste()
except EOFError:
    sys.exit(0)