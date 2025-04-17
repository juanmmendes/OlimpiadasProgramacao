def determinar_grupo():
    # Lê os resultados dos seis jogos
    jogos = []
    for _ in range(6):
        resultado = input().strip()
        jogos.append(resultado)
    
    # Conta o número de vitórias
    vitorias = jogos.count('V')
    
    # Determina o grupo com base no número de vitórias
    if vitorias >= 5:
        return 1
    elif vitorias >= 3:
        return 2
    elif vitorias >= 1:
        return 3
    else:
        return -1

# Executa o programa e imprime o resultado
print(determinar_grupo())