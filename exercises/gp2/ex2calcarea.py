print("*** Cálculo de áreas ***\nSelecione o polígono:\n1 - Retângulo\n2 - Triângulo\n3 - Círculo")

operacao = input("> ")

match operacao:
    # retangulo
    case '1':
        lado_maior = int(input("Introduza o lado maior: "))
        lado_menor = int(input("Introduza o lado menor: "))
        resultado = lado_maior * lado_menor
        resultado_string = f"{resultado}"
        operacao_string = "retângulo"
    # triangulo
    case '2':
        lado_maior = int(input("Introduza o lado maior: "))
        lado_menor = int(input("Introduza o lado menor: "))
        resultado = (lado_maior * lado_menor) / 2
        resultado_string = f"{resultado}"
        operacao_string = "triângulo"
    # circulo
    case '3':
        raio = int(input("Introduza o raio do círculo: "))
        resultado = 3.14 * raio ** 2
        resultado_string = f"{resultado}"
        operacao_string = "círculo"
    # input nao 'int'
    case _:
        resultado = "Operacao invalida."


print(f"O valor da área do " + operacao_string + " é: " + resultado_string)