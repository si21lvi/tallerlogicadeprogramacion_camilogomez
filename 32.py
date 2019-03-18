print("promedio de notas")

a=float(input("ingrese la primer nota"))

b=float(input("ingrese la segunda nota"))

c=float(input("ingrese la tercer nota"))

d=float(input("ingrese la cuarta nota"))

e=float(input("ingrese la quinta nota"))

nota1=((a*15)/100)

nota2=((b*20)/100)

nota3=((c*15)/100)

nota4=((d*30)/100)

nota5=((e*20)/100)

suma=nota1+nota2+nota3+nota4+nota5

if suma<2:
  
 print("no habilitas wey ")

if suma<3:
  
 print("reprobaste wey ")

if suma>=3:
  
 print("aprobaste")

if suma>4.5:
  
 print("felicidades por tu dedicacion")
  