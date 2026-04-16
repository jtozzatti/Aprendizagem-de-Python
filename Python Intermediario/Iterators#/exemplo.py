# Nossa coleção de dados
letras = ['A', 'B']

# Criamos o "ponteiro" (Iterator)
ponteiro = iter(letras)

# Pedimos o primeiro item
print(next(ponteiro))  # Saída: A

# Pedimos o próximo
print(next(ponteiro))  # Saída: B