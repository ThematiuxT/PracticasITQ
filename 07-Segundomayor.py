lista = [1,2,3,4,6,7,8,9,5]
mayor = lista[0]
smayor = float("-inf")

for num in lista:
    if num > mayor:
        smayor = mayor
        mayor = num
    elif num > smayor and num < mayor:
        smayor = num

if smayor == float("-inf"):
    print("No hay segundo mayor.")
else:
    print(f"El segundo mayor es {smayor}")