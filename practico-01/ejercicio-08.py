def superposicion():
  lista1 = ['a', 'ante', 'bajo', 'con', 'contra']
  lista2 = ['g', 'gg', 'g', 'g', 'gol']
  bool = False
  for pal1 in lista1:
      for pal2 in lista2:
          if pal1==pal2:
              bool = True
              break
  return bool

if superposicion():
  print("Existe una similitud en las listas")
else:
  print("No existe una similitud en las listas")
