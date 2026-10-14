string = str(input("Introduce cadena: "))
vocales = ["A","E","I","O","U"]
cuenta_vocales = 0
for letra in string:
    if letra.capitalize() in vocales:
        cuenta_vocales = cuenta_vocales + 1

print(f"Hay {cuenta_vocales} vocales.")