#include <iostream>
#include <string>

int main(int argc, char** argv){
	double altura, pesoid;
	std::string sx;
	char n='s';
	while(n=='s'){
		std::cout <<"Digite qual seu sexo (homem/mulher): ";
		std::cin >> sx;
		
		std::cout <<"Digite a sua altura: ";
		std::cin >> altura;
		
		if(sx=="homem"){
			pesoid=(72.7*altura-58);
			std::cout <<"O seu peso ideal e " <<pesoid;
		}else if(sx=="mulher"){
			pesoid=(62.1*altura-44.7);
			std::cout <<"O seu peso ideal e " <<pesoid;
		}
		std::cout <<"\nDeseja usar novamente? (s/n)";
		std::cin >>n;
	}
	return 0;
}

