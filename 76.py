contador=0
a=int(input("numero bro ))
b=1
while b<a+1:
    if a%b==0:
        print("Con este numero la division es exacta: ",b)
        contador=contador+1
    b+=1
print("total ",contador)