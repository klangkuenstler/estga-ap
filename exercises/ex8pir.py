# Programa principal - Pirâmide de Números

print("=== PIRÂMIDE DE NÚMEROS ===\n")

# Parte b) - Validação da entrada do utilizador
while True:
    try:
        int_lines = int(input("Introduza o número de linhas da pirâmide: "))
        
        if int_lines <= 0:
            print("Por favor, introduza um número positivo.")
        elif int_lines > 9:
            print("Por favor, introduza um número entre 1 e 9.")
        else:
            break
            
    except ValueError:
        print("Entrada inválida! Por favor, introduza um número inteiro.")

print(f"\nPirâmide com {int_lines} linha(s):\n")

# Parte a) - Impressão da pirâmide
for i in range(1, int_lines + 1):
    # Calcula os espaços necessários para centralizar
    espacos = '  ' * (int_lines - i)
    
    # Parte crescente: de 1 até i
    parte_crescente = ' '.join(str(num) for num in range(1, i + 1))
    

    # Parte decrescente: de i-1 até 1
    parte_decrescente = ' '.join(str(num) for num in range(i - 1, 0, -1))
    
    # Monta a linha completa
    if i == 1:
        linha = parte_crescente
    else:
        linha = parte_crescente + ' ' + parte_decrescente
    
    print(espacos + linha)