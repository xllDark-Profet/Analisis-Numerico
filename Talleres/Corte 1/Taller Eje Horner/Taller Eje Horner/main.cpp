#include<stdio.h>

int main(int argc, char** argv) {

	//Valor de x
	float valorX = 8;
	//Coeficientes del polinomio
	float coeficientes[] = { 4,7,3,6,2 };
	float resultado = 0;
	int i;

	//Recorrer los coeficientes
	for (i = 0; i < (sizeof(coeficientes) / sizeof(float)); i++) {
		//Multiplicar al valor parcial el valor de x más el coeficiente
		resultado = resultado * valorX + coeficientes[i];
	}

	printf("Resultado %f\n", resultado);
	return 0;
}