m = int(input("Valor de m: "))
M = int(input("Valor de M: "))

if m > M:
    print("'m' deve ser menor que 'M'.")


m_string = f"{m}"
M_string = f"{M}"

print(f"m = " + m_string + "\nM = " + M_string)