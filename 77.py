b=input("ingrese el nombre de usuario: ")
a=input("contraseña a ingresar: ")
c="correoproxd@gmailcom"
d="camilo02"
f=0
if b!=c or a!=d :
    while f<1:
        a = input("Vuelva a poner la contraseña: :")
        b= input("vuelva ingrese el nombre de usuario")
        f+=1
        if f>3:
            break
else:
    if b==c and a==d:
        print("hola bro")

if f>3:
    print("usuario incorecto")
    