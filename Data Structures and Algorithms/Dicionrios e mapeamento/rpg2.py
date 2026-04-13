precos = {"pocao": 10, "espada": 50, "escudo": 30}

# Adicionando um novo item ao dicionário
precos["sopa de ovos de draga"] = 30

print (precos)

# Acessando o preço da espada e diminuindo (MANEIRA DE USAR O DICIONÁRIO)
precos["espada"] = precos["espada"] - 5
print (precos["espada"])

# Iterando sobre os itens do dicionário e imprimindo o preço com desconto (UMA DAS MANEIRAS DE USAR O DICIONÁRIO)
#for item in precos:
   # print (f'{precos["espada"] - 5}')



