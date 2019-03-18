print("costos de viaje")

a=float(input("ingrese la distancia"))

b=float(input("ingrese el tiempo"))

precio=5.000

precio_definitivo=a*precio

vd=(precio_definitivo*b)*15/100

if vd>1000:

  print("se hara un descuento bro",vd)

if precio_definitivo<100000:

  print("precio total es ",precio_definitivo)