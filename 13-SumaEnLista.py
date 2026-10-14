"""
Arreglo de N entreros y objetivo k, 2 elementos diferentes que sumen k
"""

lista = [1,2,3,4,5,6,7,8]
k = 12
encontrado = False
for i in range(len(lista)):
    for j in range(i+1,len(lista)):
        if lista[i] + lista[j] == k:
            print(f"{lista[i]} y {lista[j]} suman {k}")
            encontrado = True
            break
    if encontrado:
        break
if not encontrado:
    print(f"No hay par que sume {k}")