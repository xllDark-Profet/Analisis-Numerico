#include <iostream>
#include <math.h>
using namespace std;


void EcuacionCuadratica(double x, double y, double z);

int main() {

	double a, b, c;

	cout << "Ingrese el valor de a: ";
	cin >> a;

	cout << "Ingrese el valor de b: ";
	cin >> b;

	cout << "Ingrese el valor de c: ";
	cin >> c;

	cout << endl;

	EcuacionCuadratica(a, b, c);

	return 0;
}

void EcuacionCuadratica(double x, double y, double z) {

	double expNeg ;
	double expPos ;
	double raiz;

	raiz = sqrt((pow(y, 2) - 4*((x)*(z))));

	expNeg = (-(y) - (raiz)) / (2 * x);
	expPos= (-(y)+(raiz)) / (2 * x);

	cout << "El resultado en x1_+: " << expPos << endl;

	cout << "El resultado en x2_-: " << expNeg << endl;

	cout << endl;

}
