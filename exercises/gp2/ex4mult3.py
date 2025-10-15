m = int(input("Valor de m: "))
M = int(input("Valor de M: "))

# Validação
if m >= M:
    print("'m' deve ser menor que 'M'.")
else:
    print(f"m = {m}")
    print(f"M = {M}")
    
    # Imprimir múltiplos de 3 entre m e M
    for num in range(m, M + 1):
        if num % 3 == 0:
            print(num)