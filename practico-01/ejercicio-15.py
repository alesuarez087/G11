def max(array):
    for i in array:
        n=0
        for j in array:
            if i>=j:
                n+=1
        if n==len(array):
            print("El mayor es ", i)
            break

def min(array):
    for i in array:
        n=0
        for j in array:
            if i<=j:
                n+=1
        if n==len(array):
            print("El menor es ", i)
            break

rta = ""
array = []
while rta != "fin":
    rta  = input("Ingrese un nro: ")
    if rta != "fin":
        array.append(int(rta))
    else:
        break

max(array)
min(array)
