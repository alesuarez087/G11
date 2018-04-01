def palabras(lista):
  r = ''
  for i in lista:
     if len(i)>len(r):
        r = i
  return r

lista = ['maxi','joaquin','gimenita','santiago']
print ("La palabra màs larga es:", palabras(lista))
