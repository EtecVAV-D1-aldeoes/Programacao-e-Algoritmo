#include <iostream>
#include <limits>
#include <cctype>

bool ehVogal(char c){
    c=std::tolower(static_cast<unsigned char>(c));
    return (c=='a' || c=='e' || c=='i' || c=='o' || c=='u');
}

bool ehConsoante(char c){
    c=std::tolower(static_cast<unsigned char>(c));
    return (std::isalpha(static_cast<unsigned char>(c)) && !ehVogal(c));
}

int contarVogais(const char texto[]){
    int count = 0;
    for (int i=0; texto[i] != '\0'; i++){
        if (ehVogal(texto[i])){
            count++;
        }
    }
    return count;
}

int contarConsoantes(const char texto[]){
    int count=0;
    for (int i=0; texto[i] != '\0'; i++){
        if (ehConsoante(texto[i])){
            count++;
        }
    }
    return count;
}

int main(){
    char nome[100];
    char n='s';

    while (n=='s' || n=='S'){
        std::cout << "Digite seu nome completo: ";
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cin.getline(nome, 100);

        int vogais=contarVogais(nome);
        int consoantes=contarConsoantes(nome);

        std::cout << "Quantidade de vogais: " << vogais << std::endl;
        std::cout << "Quantidade de consoantes: " << consoantes << std::endl;

        std::cout << "Deseja usar novamente? (s/n): ";
        std::cin >> n;
    }
    return 0;
}


