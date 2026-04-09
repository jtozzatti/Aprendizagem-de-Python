# Objetivo é criar um jogo de adivinhaçao

#Aqui importamos o random
import random

#Nessa parte o "numero =" é uma variavel, o "random.randint (1,10)" gera de forma aletoria um numero de um a dez, poderia ser qualquer valor
numero = random.randint(1, 10)

#While true é o inicio do loop para que o codigo nao acabe no terminal
while True:
    #aqui o chute é a variavel, o int é usado para numero inteiros, o input vai fazer com que a mensagem "digite o numero" apareça ao rodar o codigo.
    chute = int(input("Digite um número: "))

#if (se) o chute(variavel) for igual o numero(variavel) da como certo
    if chute == numero:
        print("Acertou!")
        break
#porem se o chute for maior que o numero da como alto
    elif chute > numero:
        print("Muito alto")
#Mas se o numero for errado da como muito baixo
    else:
        print("Muito baixo")