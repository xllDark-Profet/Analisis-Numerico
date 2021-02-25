#Desarrollado por Alejo, Cris y Andy  <3

valorX=int(input("Ingrese el valor de X: "))
coeficientes=[4,3,3,0,2];
resultado=0;

CLC=len(coeficientes)

for i in range(0,CLC):
	resultado= resultado * valorX + coeficientes[i]

print("Resultado:"+str(resultado))
