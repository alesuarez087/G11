from random import randint
def multi():
   lista = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]
   a = 1
   for nro in lista:
       a = a * nro
   print("los numeros son: ", lista[0], lista[1], lista[2], lista[3])
   print("el producto es ", a)

multi()
