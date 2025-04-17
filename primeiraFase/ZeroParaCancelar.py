def calcular_soma():
    # Lê o número de entradas
    n = int(input())
    
    # Lista para armazenar os números válidos
    numeros_validos = []
    
    # Processa cada número
    for _ in range(n):
        num = int(input())
        
        if num == 0:
            # Se o número for zero, remove o último número da lista (se houver)
            if numeros_validos:
                numeros_validos.pop()
        else:
            # Caso contrário, adiciona o número à lista
            numeros_validos.append(num)
    
    # Calcula a soma dos números válidos
    soma = sum(numeros_validos)
    
    return soma

# Executa o programa e imprime o resultado
print(calcular_soma())