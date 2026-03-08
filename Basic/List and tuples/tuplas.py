# 1. Criando uma tupla com dados fixos
coordenadas = (10, 20, 30)

# 2. Acessando elementos pelo índice
primeiro_valor = coordenadas[1]

# 3. Desempacotando a tupla em variáveis
x, y, z = coordenadas

# 4. Tentativa de modificação (isso gerará erro)
# coordenadas[0] = 50

# 5. Usando tupla como chave de dicionário
mapa = {
    (1, 2): "Local A",
    (3, 4): "Local B"
}

# 6. Contando ocorrências
tupla_numeros = (1, 2, 2, 3, 2)
quantidade_dois = tupla_numeros.count(2)

# 7. Imprimindo resultados
print(f"Primeiro valor: {primeiro_valor}")
print(f"Desempacotado: {x}, {y}, {z}")
print(f"Quantidade de 2s: {quantidade_dois}")
