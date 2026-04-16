import re

# 1. O texto onde vamos procurar
texto = "O endereço da entrega é Rua ABC, CEP 01234-567."

# 2. O nosso padrão (5 números, traço, 3 números)
padrao_cep = r"\d{5}-\d{3}" 

# 3. Usamos o 'search' para encontrar o padrão no texto
busca = re.search(padrao_cep, texto)

if busca:
    print(f"CEP encontrado: {busca.group()}")
else:
    print("Nenhum CEP válido foi encontrado.")