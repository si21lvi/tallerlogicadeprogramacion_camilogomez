s=float(input("ingrese el numero"))

horas=int(s/3600)

minutos=int((s-(horas*3600))/60)

segundos=s-((horas*3600)+(minutos*60))

print(str(horas)+ ":" +str(minutos)+":" +str(segundos))