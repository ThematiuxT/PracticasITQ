st = str(input("cadena: "))
listaRevez = []
for i,letra in enumerate(st):
    listaRevez.insert(-i-1,letra)

es_palindromo = True
for i in range(len(st)):
    es_palindromo = es_palindromo and (st[i] == listaRevez[i])

if es_palindromo:
    print("Es palindromo")
else:
    print("No es palindromo")