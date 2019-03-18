import math

radio=float(input("ingrese el radio", ))

medida=float(input("ingresar medida", ))

apotema=(math.sqrt((radio**2)-(medida/2)**2))

area_de_un_hexagono=(3*medida*apotema)

print("el area de un hexagono es",area_de_un_hexagono)