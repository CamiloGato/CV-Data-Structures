#include <iostream>
#include "vector"
#include "cstring"

using namespace std;

vector<int> get_vector(string texto, const char *delim){
    int n = texto.length();
    char char_array[n + 1];
    strcpy(char_array, texto.c_str());

    vector<int> numeros;

    char *ptr;
    ptr = strtok(char_array, delim);

    while (ptr != NULL)
    {
        numeros.insert( numeros.end() ,stoi(ptr));
        ptr = strtok (NULL, " , ");
    }
    return numeros;
}

void acumulador(vector<int> &numeros){

    int n = numeros.size();

    if (n == 1){
        return;
    }

    numeros[n-2] = numeros[n-1] + numeros[n-2];
    numeros.pop_back();
    cout << numeros[n-2] << endl;
    acumulador( numeros );

}

int main(){

    string n;
    getline(cin, n);
    string numeros;
    getline(cin, numeros);

    vector<int> num_list = get_vector(numeros, " ");

    acumulador(num_list);

    return 0;
}