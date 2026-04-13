convidados = {
    "Ana": 20,
    "Bruno": 17,
    "Carlos": 22,
    "Diana": 15,
    "Eduardo": 19,
    "Fernanda": 21,
    "Gustavo": 16,  # Apenas uma vírgula aqui!
    "Helena": 18,
    "Igor": 17
}

# Verificando quem pode entrar na festa
pode_entrar = []

# Iterando sobre o dicionário para verificar a idade de cada convidado e se poode entrar na festa
for nome, idade in convidados.items():
    if idade >= 18:
        pode_entrar.append(nome)

print(pode_entrar)