#Objetivo criar um jogo de papel e tesoura

#Importa o random
import random

#Criando variavel para guardar as opçoes
opcoes = ["pedra", "papel", "tesoura"]

#loop
while True:
    #eu e minhas opçoes, o adversario por ser maquina usamos a opçao random
    eu = input("Escolha (pedra, papel, tesoura): ")
    adversario = random.choice(opcoes)

#aqui o sistema com todas as possibilidades
    if eu == adversario:
        print("empatemos")

    elif (eu == "pedra" and adversario == "tesoura") or \
         (eu == "papel" and adversario == "pedra") or \
         (eu == "tesoura" and adversario == "papel"):
        print("ganhemos")

    elif (eu == "pedra" and adversario == "papel") or \
         (eu == "papel" and adversario == "tesoura") or \
         (eu == "tesoura" and adversario == "pedra"):
        print("noob")

    else:
        print("ta errado painhu")

#aqui caso eu queira sair
    sair = input("Quer sair? (s/n): ")
    if sair == "s":
        break