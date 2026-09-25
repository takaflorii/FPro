#include <stdio.h>
#include <math.h>
int main() {

int a = 3, b = 11, c = 4, d = 2;
int resultado;
double potencia, raiz1, raiz2;

potencia = pow(a+b, c*d);
raiz1 = (-b + sqrt(b*b - 4*a*c)) / (2*a);
raiz2 = (-b - sqrt(b*b - 4*a*c)) / (2*a);

printf("As raizes da equacao do segundo grau sao: %.2lf e %.2lf\n", raiz1, raiz2);
printf("O resultado da potencia e: %.2lf\n", potencia);

}