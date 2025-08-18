#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int main(){
  int n, intervalo;
  cin>>n>>intervalo;

  vector<int> temperaturas(n);
  for(int i=0; i<n; ++i){
    cin>>temperaturas[i];
  }
  double menor_media=INT_MAX;
  double maior_media=INT_MIN;
  for(int i=0; i<=n-intervalo; ++i){
    double soma = 0;
    for(int j=i; j<i+intervalo; ++j){
      soma+=temperaturas[j];
    }
    double media=soma/intervalo;
    menor_media=min(menor_media, media);
    maior_media=max(maior_media, media);
  }
  cout<<maior_media<<" "<<menor_media<<endl;

  return 0;
}
