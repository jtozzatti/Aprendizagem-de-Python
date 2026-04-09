# Objetivo é fazer um gerador de senhas usando o random

#importando o sistema random
import random

#aqui a variavel ira guardar as caracteres
caracteres = ["a", "b", "c", "1", "2", "3"]

#senha = variavel vazia onde vamos montar a senha aos poucos
senha = ""

#Aqui o range pega e faz uma senha de somente 5 caracteres aletorios
for i in range(5):  
    #aqui usamos o random.choice para escolher um caractere aleatorio da lista
    letra = random.choice(caracteres)
    #aqui juntamos a letra escolhida na variavel senha
    senha += letra

#aqui imprime a senha
print(senha)