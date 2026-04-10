# Programa de verificação de senha

# Início do loop (vai rodar até o usuário decidir sair)
while True:
    
    # Entrada da senha digitada pelo usuário
    senha = input("Digite a sua senha: ")

    # Variáveis de controle (verificam se a senha tem número e letra maiúscula)
    tem_numero = False
    tem_maiuscula = False
    
    # Percorre cada caractere da senha
    for c in senha:
        # Verifica se existe pelo menos um número
        if c.isdigit():
            tem_numero = True
        
        # Verifica se existe pelo menos uma letra maiúscula
        if c.isupper():
            tem_maiuscula = True
    
    # Verifica se a senha atende todos os requisitos:
    # - mínimo de 8 caracteres
    # - pelo menos um número
    # - pelo menos uma letra maiúscula
    if len(senha) >= 8 and tem_numero and tem_maiuscula:
        print("ta certo painhu")
    else:
        print("ta errado painhu")

    # Pergunta se o usuário deseja sair do programa
    sair = input("voce deseja sair? (s/n)")

    # Encerra o loop se o usuário digitar "s"
    if sair == "s":
        break