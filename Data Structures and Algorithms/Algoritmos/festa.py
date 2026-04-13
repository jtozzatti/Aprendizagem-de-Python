convidados = {
    "Ana": 20,
    "Bruno": 17,
    "Carlos": 22
}

# Puxando a idade de Ana
convidados["Ana"] = 19

# Verificando se Ana pode entrar na festa
if convidados["Ana"] >= 18:
    print("Ana pode entrar!")
else:
    print("Ana não pode entrar!")