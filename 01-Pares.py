numeros = [1,2,3,3,4,6,6,2000,2001]
pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print(f"Hay {len(pares)} pares, son {pares}")