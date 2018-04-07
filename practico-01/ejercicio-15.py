
rta = ""
array = []
while rta != "fin":
    rta  = input("Ingrese un nro: ")
    if rta != "fin":
        array.append(int(rta))
    else:
        break

print("El mayor numero es:", max(array))
print("El menor es:", min(array))
