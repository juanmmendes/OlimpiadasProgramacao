def verificar_baralho(cartas):
    # Inicializa dicionários para contar as cartas de cada naipe
    naipes = {'C': {}, 'E': {}, 'U': {}, 'P': {}}
    
    # Processa a entrada para contar as cartas
    i = 0
    while i < len(cartas):
        valor = cartas[i:i+2]
        naipe = cartas[i+2]
        
        # Verifica se este valor já existe no naipe (carta duplicada)
        if valor in naipes[naipe]:
            naipes[naipe][valor] += 1
        else:
            naipes[naipe][valor] = 1
        
        i += 3
    
    # Verifica e prepara a saída para cada naipe
    resultados = []
    for naipe_chave in ['C', 'E', 'U', 'P']:
        cartas_naipe = naipes[naipe_chave]
        
        # Verifica se há duplicatas
        if any(contagem > 1 for contagem in cartas_naipe.values()):
            resultados.append("erro")
        else:
            # Conta quantas cartas estão faltando
            faltando = 13 - len(cartas_naipe)
            resultados.append(str(faltando))
    
    return resultados

# Lê a entrada
cartas = input().strip()

# Processa e imprime a saída
resultado = verificar_baralho(cartas)
for res in resultado:
    print(res)