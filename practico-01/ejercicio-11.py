def contador(num):
   return len(str(num))

num = int(input("Ingresa un numero: "))
print("El numero tiene %s digitos" % (contador(num)))
