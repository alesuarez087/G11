from random import randint

fila = randint(4, 10)
col = 2

laberinto = [range(fila) for i in range(col)] #defino al laberinto como una matrix de 2 columnas y X filas (entre 4 y 10)

i=0
while i<fila: #lleno los valores del laberinto con pares True False con una funcion random y de ese resulta, obtengo el valor contrario para l aotra columna
    if 5>randint(1, 10):
        laberinto[i][0] = True
    else:
        laberinto[i][0] = False
    if laberinto[i][0]:
        laberinto[i][1] = False
    else:
        laberinto[i][1] = False

i = 0
while i<fila:
    if laberinto[i][0] == False:
        print("Camino: ", i, 0)
        i+=1
    else:
        print("Camino: ", i, 1)
        i+=1








