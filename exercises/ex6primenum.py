mode = input("Selecione o modo de apresentação:\na. Descobrir se n é primo;\nb. Lista de números primos de 1-100.\nc. Lista de números primos gémeos.\n[a/b/c]: ")

if mode == "a":
    print("Modo: a. Descobrir se n é primo")
    n = int(input("Insira um número positivo inteiro: "))
    if n <= 1:
        print("O número deve ser positivo e inteiro.")
    else:
        is_prime = "é primo." # Flag variable
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = "não é primo."
                break
        print(f"{n} {is_prime}")

elif mode == "b":
    print("Modo: b. Lista de números primos de 1-100:")
    for num in range(2,101):
        if all(num%i!=0 for i in range(2,num)):
            print(num)

elif mode == "c":
    print("Modo: c. Lista de números primos gémeos")
    primos = []
    for num in range(2, 101):
        if all(num%i!=0 for i in range(2,num)):
            primos.append(num)
    
    for primo1, primo2 in zip(primos, primos[1:]):
        if primo2 - primo1 == 2:
            print(f"({primo1}, {primo2})")