int_jogador1 = int(input("Introduza um número positivo inteiro\nJogador 1: "))
tries_limit = int(input("Introduza o número do limite de tentativas para o Jogador 2: "))
int_jogador2 = -65165161651651651
tries = 0

while int_jogador1 != int_jogador2:
    if tries == tries_limit:
        print(f"O Jogador 2 chegou ao limite de {tries} tentativas.")
        exit()

    else:
        int_jogador2 = int(input("Jogador 2: "))
    
        if int_jogador2 == int_jogador1:
            print(f"Você adivinhou o número do adversário após {tries} tentativas!")
    
        elif int_jogador2 < int_jogador1:
            tries = tries + 1
            print(f"O número do Jogador 1 é maior que {int_jogador2}.")
    
        elif int_jogador2 > int_jogador1:
            tries = tries + 1
            print(f"O número do Jogador 1 é menor que {int_jogador2}.")