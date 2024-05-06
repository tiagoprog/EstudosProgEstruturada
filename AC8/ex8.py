def calcular_pontuacao_rafael(x, y):
    """Calcular pontuação de Rafael"""
    return 6 * x + 2 * y

def calcular_pontuacao_beto(x, y):
    """Calcular pontuação de Beto"""
    return 4 * x + 10 * y

def calcular_pontuacao_carlos(x, y):
    """Calcular pontuação de Carlos"""
    return -100 * x + y ** 3

def competicao(x, y):
    """Determinar o vencedor"""
    pontuacoes = {
        "Rafael": calcular_pontuacao_rafael(x, y),
        "Beto": calcular_pontuacao_beto(x, y),
        "Carlos": calcular_pontuacao_carlos(x, y)
    }
    vencedor = max(pontuacoes, key=pontuacoes.get)
    print(f"{vencedor} ganhou")

# Entrada de dados e execução
num_casos = int(input())
for _ in range(num_casos):
    x, y = map(int, input().split())
    competicao(x, y)