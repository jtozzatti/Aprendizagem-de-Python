#Imagine que você tem uma lista de palavras: ["maçã", "oi", "computador", "sol"].
#Se você quisesse filtrar apenas as palavras que têm mais de 3 letras, 
#como ficaria a parte da expressão da sua lambda? (Dica: em Python, usamos len(x) para contar o tamanho de algo).

listas_palavras = ["maçã", "oi", "computador", "sol"]

resultado = list(filter(lambda x: len(x) > 3, listas_palavras))
print(resultado)