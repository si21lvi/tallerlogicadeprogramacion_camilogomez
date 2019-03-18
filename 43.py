print("ejercicio 43")

a=int(input("ingrese el numero"))

b=int(input("ingrese el segundo numero"))

c=int(input("ingrese el tercer numero"))

if a<b and b<c and c>b:
 
  print("aumenta",a,b,c)

if a>b and b<a and c<b:

  print("disminuye",a,b,c)

if a>b and b<a and c>b :
  
  print("no avnza ni se sotiene",a,b,c)

if a<b and b>a and c<b:

  print("no avanza wey",a,b,c)