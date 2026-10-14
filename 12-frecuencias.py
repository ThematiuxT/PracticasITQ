lista = [0,0,3,0,2,2,1,0,0,0,3]
freq = []
encontrados = []
lista.sort()
for num in lista:
    try:
        freq[num] = freq[num] + 1
    except IndexError:
        freq.insert(num,1)

for x, frequence in enumerate(freq):
    print(f"Hay {frequence} del numero {x}")