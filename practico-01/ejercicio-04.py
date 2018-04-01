def isVocal(letra):
   vocales = ['a', 'e', 'i' , 'o', 'u']
   i=0
   while i < 5:
       if vocales[i] == letra:
           print(letra, " es una vocal")
           break
       else:
           i=i+1
   if i == 5:
       print(letra, " es una consonante")

letra = input("Ingrese una letra: ")
isVocal(letra)
