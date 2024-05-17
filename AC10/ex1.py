class Camiseta:
    def _init_(self, nome, cor, tamanho):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

def comparar_camisetas(camiseta_a, camiseta_b):
    if camiseta_a.cor == camiseta_b.cor:
        if camiseta_a.tamanho == camiseta_b.tamanho:
            if camiseta_a.nome < camiseta_b.nome:
                return -1
            if camiseta_a.nome > camiseta_b.nome:
                return 1
            return 0
        if camiseta_a.tamanho > camiseta_b.tamanho:
            return -1
        return 1
    if camiseta_a.cor < camiseta_b.cor:
        return -1
    return 1

def particionar(lista_camisetas, inicio, fim):
    pivo = lista_camisetas[fim - 1]
    i = inicio
    for j in range(inicio, fim):
        if comparar_camisetas(lista_camisetas[j], pivo) < 0:
            lista_camisetas[j], lista_camisetas[i] = lista_camisetas[i], lista_camisetas[j]
            i += 1

    if comparar_camisetas(pivo, lista_camisetas[i]) < 0:
        lista_camisetas[fim - 1], lista_camisetas[i] = lista_camisetas[i], lista_camisetas[fim - 1]

    return i

def quicksort(lista_camisetas, inicio, fim):
    if fim > inicio:
        posicao_pivo = particionar(lista_camisetas, inicio, fim)
        quicksort(lista_camisetas, inicio, posicao_pivo)
        quicksort(lista_camisetas, posicao_pivo + 1, fim)

primeira_execucao = True
while True:
    try:
        numero_camisetas = int(input())

        if numero_camisetas == 0:
            break

        if primeira_execucao:
            primeira_execucao = False
        else:
            print('')

        lista_camisetas = []
        for _ in range(numero_camisetas):
            nome = input()
            cor, tamanho = input().strip().split(' ')

            lista_camisetas.append(Camiseta(nome, cor, tamanho))

        quicksort(lista_camisetas, 0, len(lista_camisetas))

        for camiseta in lista_camisetas:
            print(f'{camiseta.cor} {camiseta.tamanho} {camiseta.nome}')
    except EOFError:
        break