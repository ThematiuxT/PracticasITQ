def CaminoSearchADestino(laberinto, searchX, searchY, searched:list[list[bool]], path ):
    # Checar que no se salga
    if (searchX < 0) or (searchX >= len(laberinto[0])) or (searchY < 0) or (searchY >= len(laberinto)):
        return -1
    pointToSearch = laberinto[searchY][searchX]
    # Checar que no choque o que se se halla buscado previamente
    if (searched[searchY][searchX]) or (pointToSearch == "#"):
        return -1
    if pointToSearch == "E":
        return path
    newSearched = searched.copy()
    newSearched[searchY][searchX] = True
    # Busca Norte este norte oeste
    paths = [
        CaminoSearchADestino(laberinto, searchX, searchY-1, newSearched, path + 1),
        CaminoSearchADestino(laberinto, searchX+1, searchY, newSearched, path + 1),
        CaminoSearchADestino(laberinto, searchX, searchY+1, newSearched, path + 1),
        CaminoSearchADestino(laberinto, searchX-1, searchY, newSearched, path + 1)
    ]
    while ((-1 in paths) and len(paths) > 1):
        paths.remove(-1)
    return min(paths)

    
        

def MasCorto(laberinto):
    # Encontrar Inicio y generar ya buscado
    searched = []
    for y,row in enumerate(laberinto):
        searched.append([])
        for x,cell in enumerate(row):
            searched[y].append(False)
            if cell == "S":
                startX = x
                startY = y

    return CaminoSearchADestino(laberinto,startX,startY,searched,0)

    
    

print(MasCorto([
    ["S",".",".","#",".","."],
    ["#","#",".","#",".","."],
    [".",".",".","#",".","."],
    [".","#",".","#",".","."],
    [".",".",".","#",".","E"]
]))