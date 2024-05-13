def calcular_gasto(produtos_disponiveis, produtos_desejados):
    total = 0
    for produto, quantidade in produtos_desejados:
        for p, preco in produtos_disponiveis:
            if p == produto:
                total += preco * quantidade
                break
    return total

def main():
    casos_teste = int(input())

    for _ in range(casos_teste):
        m = int(input())
        produtos_disponiveis = []
        for _ in range(m):
            produto, preco = input().split()
            produtos_disponiveis.append((produto, float(preco)))

        p = int(input())
        produtos_desejados = []
        for _ in range(p):
            produto, quantidade = input().split()
            produtos_desejados.append((produto, int(quantidade)))

        gasto_total = calcular_gasto(produtos_disponiveis, produtos_desejados)
        print("R$ {:.2f}".format(gasto_total))

if __name__ == "_main_":
    main()