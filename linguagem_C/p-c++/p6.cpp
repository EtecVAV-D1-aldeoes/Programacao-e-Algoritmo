#include <iostream>
#include <string>

int main(){
    std::string dias[7]={
        "Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"};

    int num;
    std::cout << "Digite um numero de 1 a 7: ";
    std::cin >> num;

    if(num >= 1 && num <= 7){
        std::cout << dias[num - 1] << std::endl;
    }else{
        std::cout << "Numero invalido. Digite apenas entre 1 e 7." << std::endl;
    }
    return 0;
    
}
