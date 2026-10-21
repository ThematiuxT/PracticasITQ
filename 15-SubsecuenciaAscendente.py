def subSec(lista) -> int:
    tamannoActual = 1
    tamannoMax = 1
    last = float("inf")
    for item in lista:
        if item < last:
            tamannoActual = 1
        else:
            tamannoActual = tamannoActual + 1
            tamannoMax = max(tamannoActual,tamannoMax)
        last = item
    return tamannoMax


print(subSec([10,9,2,3,5,7,1,18]))