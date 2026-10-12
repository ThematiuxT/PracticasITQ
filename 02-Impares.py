numeros = [1,2,3,3,4,6,6,2000,2001]
impares = []

for num in numeros:
    if num % 2 != 0:
        impares.append(num)

print(f"Hay {len(impares)} impares, son {impares}")