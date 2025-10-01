# 2025-10-01
# '03_introducao_python.pdf' slide n27 (Segunda parte - desenvolver o programa em linguagen python)
'''
EXERCÍCIO
▪ Desenvolva, usando pseudo-código, um programa que:
    ▪ indique qual o dia da semana se for introduzido um número de 1 a 7 (primeiro dia da semana é domingo)
    ▪ caso seja introduzido um número fora do intervalo, deve ser enviada a mensagem “Dia da semana (<número_introduzido>) inválido!”
    ▪ Implemente o algoritmo usando a linguagem de programação Python e teste o seu correcto funcionamento
'''

def dia_da_semana(numero):
    if numero == 1:
        return "Domingo"
    elif numero == 2:
        return "Segunda-feira"
    elif numero == 3:
        return "Terça-feira"
    elif numero == 4:
        return "Quarta-feira"
    elif numero == 5:
        return "Quinta-feira"
    elif numero == 6:
        return "Sexta-feira"
    elif numero == 7:
        return "Sábado"
    else:
        return f"Dia da semana ({numero}) inválido!"

# Pedir input e comparar com as variaveis atribuidas acima
dia_da_semana_int = (input("Introduza um numero de 1 a 7: "))
print(dia_da_semana(dia_da_semana_int))



