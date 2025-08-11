#include <iostream>
#include <string>

int main(){
    std::string palavra;
    std::cout << "Digite uma palavra: ";
    std::cin >> palavra;

    int inicio=0;
    int fim=palavra.length()-1;
    bool ehPalindromo=true;

    while (inicio<fim) {
        if (palavra[inicio]!=palavra[fim]){
            ehPalindromo=false;
            break;
        }
        inicio++;
        fim--;
    }

    if(ehPalindromo){
        std::cout << palavra << " e um palindromo.\n";
    } else {
        std::cout << palavra << " nao e um palindromo.\n";
    }
    return 0;

}
