#include <iostream>

int somar(int a, int b){
	return a+b;
}
int subtrair(int a, int b){
	return a-b;
}
int multiplicar(int a, int b){
	return a*b;
}
int divisao(int a, int b){
	return a/b;
}
int main(int argc, char** argv){
	int n1, n2, adi, sub, mul;
	double div;
	char n='s';
	while(n=='s'){
		std::cout <<"Digite um numero: ";
		std::cin >> n1;
		
		std::cout << "Digite um numero: ";
		std::cin >> n2;
		
		adi=somar(n1, n2);
		sub=subtrair(n1, n2);
		mul=multiplicar(n1, n2);
		div=divisao(n1, n2);
		
		std::cout << "Adicao = " << adi << "\nSubtracao = " <<sub<< "\nMultiplicacao = " <<mul<< "\nDivisao = " <<div;
		
		std::cout <<"\nDeseja usar novamente? (s/n)";
		std::cin >>n;
	}
	return 0;
}
