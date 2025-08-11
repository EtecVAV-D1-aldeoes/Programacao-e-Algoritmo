#include <iostream>
#define PI 3.14
double area(double raio){
    return PI*raio*raio;
}

int main(int argc, char** argv){
	int n1, n2, n3, n4, n5;
	char n='s';
	while(n=='s'){
		std::cout << "Digite o raio do circulo 1: ";
		std::cin >>n1;
		
		std::cout << "Digite o raio do circulo 2: ";
		std::cin >>n2;
		
		std::cout << "Digite o raio do circulo 3: ";
		std::cin >>n3;
		
		std::cout << "Digite o raio do circulo 4: ";
		std::cin >>n4;
		
		std::cout << "Digite o raio do circulo 5: ";
		std::cin >>n5;
		
		std::cout << "A area do circulo 1: " << area(n1) << "\n";
		std::cout << "A area do circulo 2: " << area(n2) << "\n";
		std::cout << "A area do circulo 3: " << area(n3) << "\n";
		std::cout << "A area do circulo 4: " << area(n4) << "\n";
		std::cout << "A area do circulo 5: " << area(n5) << "\n";
		
		std::cout << "Deseja usar novamente? (s/n)";
		std::cin>>n;
	}
	return 0;
}
