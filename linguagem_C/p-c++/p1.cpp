#include <iostream>

int main(){
    int num, soma;
    char n='s';

    while(n=='s' || n=='S'){
        soma=0;

        std::cout << "Digite um numero: ";
        std::cin >> num;

        for (int i=1; i <=num; i++){
            if(i % 2 != 0){
                soma += i;
            }
        }

        std::cout << "A soma dos impares ate " << num << " = " << soma << std::endl;

        std::cout << "Deseja usar novamente? (s/n): ";
        std::cin >> n;
    }
    return 0;
    
}
