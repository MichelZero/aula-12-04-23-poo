

# exemplos de objetos iteráveis utilizando o método pop().

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# pop() é um método de objetos iteráveis, como listas, tuplas, dicionários e conjuntos.
# correto
lista.pop() # Remove o último elemento da lista e retorna o valor removido.
lista.pop(0) # Remove o elemento da lista que está na posição 0 e retorna o valor removido.
dicionario.pop('chave1') # Remove o elemento do dicionário que tem a chave 'chave1' e retorna o valor removido.
conjunto.pop() # Remove um elemento do conjunto e retorna o valor removido. o elemento removido é arbitrário.

print(lista) # 
print(dicionario)
print(conjunto)

# erro
# tupla.pop() # Erro de execução pois a tupla é um objeto imutável e não pode ser alterado.

# dicionario.pop() # Erro de execução pois o método pop() não recebe 
#                  parâmetros e o dicionário é um objeto iterável 
#                  e não um objeto indexável como uma lista ou tupla por exemplo. 
conjunto.pop() # Erro de execução pois o conjunto é .
