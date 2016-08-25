#include <stdio.h>
#include <math.h>

void NewtonRaphson(double x0, double (*F)(double), double (*Df)(double));

double Fa (double x);
double Fb (double x);
double Fc (double x);
double Fd (double x);
double Fexe (double x); // primeiro exemplo da worksheet

double Dfa (double x);
double Dfb (double x);
double Dfc (double x);
double Dfd (double x);
double Dfexe (double x);


int main(int argc, char const *argv[])
{
	NewtonRaphson(-3,  &Fa, & Dfa);
	NewtonRaphson(0,   &Fb, &Dfb);
	NewtonRaphson(1.5, &Fb, &Dfb);
	NewtonRaphson(2,   &Fb, &Dfb);
	NewtonRaphson(3,   &Fc, &Dfc);
	NewtonRaphson(-3,  &Fd, &Dfd);
	NewtonRaphson(1.5,   &Fd, &Dfd);

	return 0;
}

/******************************************************/
/*             Metodo de Newton - Raphson             */                          
/******************************************************/

void NewtonRaphson(double x0, double (*F)(double), double (*Df)(double)){
	int i = 0;
	double x = x0, erro = 1e-8;

	while ( fabs(F(x)) > erro ){
		i++;
		x -= F(x)/Df(x);
		printf("x%d = %.17lf\n", i, x);
	}
	printf("%d iterações\n x = %.18lf\n\n", i, x);

}


/******************************************************/
/*                     Equações                       */                           
/******************************************************/

double Fa (double x){
	return atan(x) - sin(x) + 1; 
}

double Fb (double x){
	return sin(pow(x,2) + 1) + x - 1; 
}

double Fc (double x){
	return pow(x,5) - 4 * pow(x,4) + 3 * pow(x,3) - pow(x,2) + x - 1;
}

double Fd (double x){
	return pow(x,10) - 20 * pow(x,8) + 160 * pow(x,6) - 640 * pow(x,4) + 1280 * pow(x,2) - 1024; 

}

double Fexe(double x){
	return 4 * pow(x,5) - 3 * pow(x,3) - 3 * pow(x,2) - 5 * x + 3; 
}

/******************************************************/
/*                     Derivadas                      */                           
/******************************************************/

double Dfa (double x){
	return 1/(pow(x,2) + 1) - cos(x);
}

double Dfb (double x){
	return 2 * x * cos(pow(x,2) + 1) + 1;
}

double Dfc (double x){
	return 5 * pow(x,4) - 16 * pow(x,3) + 9 * pow(x,2) - 2*x + 1;
}

double Dfd (double x){
	return 10 * pow(x,9) - 160 * pow(x,7) + 960 * pow(x,5) - 2560 * pow(x,3) +  2560 * x ;
}


double Dfexe(double x){
	return 20 * pow(x,4) - 9 * pow(x,2) - 6 * x - 5;
}


