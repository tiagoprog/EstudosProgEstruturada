def contar_respostas_corretas(tipo_cha, respostas):
    corretas = respostas.count(tipo_cha)
    return corretas

tipo_cha = int(input())
respostas = list(map(int, input().split()))

print(contar_respostas_corretas(tipo_cha, respostas))