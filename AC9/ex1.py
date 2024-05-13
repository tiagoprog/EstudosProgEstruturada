def calcular_tempo(distancia):
    tempo = distancia / (90 - 60)
    tempo_minutos = tempo * 60
    return tempo_minutos

distancia = int(input())

tempo_necessario = calcular_tempo(distancia)

print(f"{int(tempo_necessario)} minutos")