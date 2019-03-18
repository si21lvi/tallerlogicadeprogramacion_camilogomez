print("ejercicio 42")

x=int(input("ingrese el primer numero"))

if x>100000:
  
 print("no se puede imprimir")

if x>=10000 and x<=100000:

  print("el numero tiene 5 cifras")

if x>=1000 and x<10000:

  print("el numero tiene 4 cifras")

else:

  if x>=1000 and x<10000:

    print("el numero tiene 3 cifras")

  if x>=10 and x<1000:
    
    print("el numero tiene 2 cifras")

  if x<10 and x<1000:

    print("el numero tiene 1 cifra")