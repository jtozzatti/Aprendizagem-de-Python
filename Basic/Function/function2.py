import random  # importa a biblioteca que gera números aleatórios

# cria uma função que recebe um número e retorna uma resposta
def getAnswer(answerNumber):

    # se o número for 1
    if answerNumber == 1:
        return 'It is certain'

    # se o número for 2
    elif answerNumber == 2:
        return 'It is decidedly so'

    # se o número for 3
    elif answerNumber == 3:
        return 'Yes'

    # se o número for 4
    elif answerNumber == 4:
        return 'Reply hazy try again'

    # se o número for 5
    elif answerNumber == 5:
        return 'Ask again later'

    # se o número for 6
    elif answerNumber == 6:
        return 'Concentrate and ask again'

    # se o número for 7
    elif answerNumber == 7:
        return 'My reply is no'

    # se o número for 8
    elif answerNumber == 8:
        return 'Outlook not so good'

    # se o número for 9
    elif answerNumber == 9:
        return 'Very doubtful'


# gera um número aleatório entre 1 e 9
r = random.randint(1, 9)

# chama a função e guarda a resposta
fortune = getAnswer(r)

# mostra a resposta na tela
print(fortune)