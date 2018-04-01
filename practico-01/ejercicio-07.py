def es_palindromo(cadena):
   i=0
   l = len(cadena)//2
   while i<l:
       if cadena[i] == cadena[-(i+1)]:
           i+=1
       else:
           break

   if i == l:
       print(cadena, "es un palindromo")
   else:
       print(cadena, "no es un palindromo")

cadena = input("ingrese una palabra: ")
es_palindromo(cadena)
