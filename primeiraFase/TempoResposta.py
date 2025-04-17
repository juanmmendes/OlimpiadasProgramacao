def calcular_tempo_resposta():
    # Lê o número de registros
    n = int(input())
    
    # Variáveis para rastreamento
    amigos = {}  # Dicionário para armazenar o estado de cada amigo
    tempo_atual = 0  # Contador de tempo desde o início
    
    # Estrutura para cada amigo: {amigo_id: {'pendente': bool, 'tempo_recebido': int, 'tempo_total': int}}
    
    for _ in range(n):
        registro = input().split()
        tipo = registro[0]
        valor = int(registro[1])
        
        if tipo == 'T':
            # Atualiza o contador de tempo
            tempo_atual += valor - 1  # -1 porque cada evento já conta 1 segundo por padrão
        elif tipo == 'R':
            # Recebeu mensagem do amigo
            if valor not in amigos:
                amigos[valor] = {'pendente': True, 'tempo_recebido': tempo_atual, 'tempo_total': 0}
            else:
                amigos[valor]['pendente'] = True
                amigos[valor]['tempo_recebido'] = tempo_atual
        elif tipo == 'E':
            # Enviou resposta para o amigo
            if amigos[valor]['pendente']:
                tempo_resposta = tempo_atual - amigos[valor]['tempo_recebido']
                amigos[valor]['tempo_total'] += tempo_resposta
                amigos[valor]['pendente'] = False
        
        # Incrementa o tempo (cada evento conta como 1 segundo, exceto quando há um registro T)
        tempo_atual += 1
    
    # Prepara a saída
    resultado = []
    for amigo_id in sorted(amigos.keys()):
        if amigos[amigo_id]['pendente']:
            resultado.append(f"{amigo_id} -1")
        else:
            resultado.append(f"{amigo_id} {amigos[amigo_id]['tempo_total']}")
    
    return resultado

# Executa o programa
resultados = calcular_tempo_resposta()
for linha in resultados:
    print(linha)