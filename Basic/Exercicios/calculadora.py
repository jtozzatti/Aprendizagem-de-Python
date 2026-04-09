# Objetivo é criar um calculadora baisca, usando apenas dois numeros escolhidos pelo usario

#Loop para calculadora continuar mesmo apos o resultado
while True:
    #variaveis que irao guardar o valor, float é para decimais e o input vai imprimir o valor no terminal
    numero1 = float(input("numero: "))
    numero2 = float(input("numero: "))
    
    #Aqui damos o valor a operaçap
    operaçao = input("operaçao (+, -, *, /): ")

#Se a operaçao começar com cada um desse ele aparece o numero1 mais a operaçao com o numero 2, caso o contrario da como opçao invaladia
    if operaçao == "+":
        print(numero1 + numero2)
    elif operaçao == "-":
        print(numero1 - numero2)
    elif operaçao == "*":
        print(numero1 * numero2)
    elif operaçao == "/":
        print(numero1 / numero2)
    else:
        print("Operação inválida")

#Aqui fazemos uma opçao de sair
    sair = input("Quer sair? (s/n): ")
    if sair == "s":
        break