import math
lista = [1,3,4,5,6]
#       [0,1,2,3]
n = 5
lo = 0
hi = n-1
while True:
    i = math.floor((hi-lo)/2) + lo
    if lista[i] - 1 == i:
        #Muy chico, mas alto
        lo = i
    else:
        #Muy alto, mas chico
        hi = i
    if hi == lo + 1:
        faltante = hi + 1
        break

print(f"Falta {faltante}")