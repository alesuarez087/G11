def definir_n_caracteres (n, c):
   i=0
   p=""
   while i<n:
      p=p+c
      i+=1
   print("cadena: ", p)

n = int(input("ingrese un nro: "))
c = input("ingrese un caracter: ")
definir_n_caracteres(n, c)
