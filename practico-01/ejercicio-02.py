from random import randint
def max_de_tres(a, b, c):
   if a>b & a>c:
       print("el mayor es ", a)
   elif b>a & b>c:
       print("el mayor es ", b)
   else:
       print("el mayor es ", c)

a=randint(0, 30)
b=randint(0,30)
c=randint(0,30)
print("a = ", a)
print("b = ", b)
print("c = ", c)
max_de_tres(a, b, c)
