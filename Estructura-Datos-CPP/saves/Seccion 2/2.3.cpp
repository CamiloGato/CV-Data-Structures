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

void cantidad_num(vector<int> numeros, int num){
    int mayor = 0, menor = 0, igual = 0;
    for (int n: numeros){
        if (num > n){
            menor++;
        } else if (num < n) {
            mayor++;
        } else if (num == n){
            igual++;
        } else {
            cout << "ERROR RARO EN IF";
        }
    }
    cout << "mayores: " << mayor << ", menores: " << menor << ", iguales: " << igual << endl;
}

int main(){

    string n;
    getline(cin, n);
    string numeros;
    getline(cin, numeros);
    vector<int> lista_num = get_vector(numeros, ", ");

    string cantidad;
    getline(cin, cantidad);

    for (int i = 0; i < stoi(cantidad); ++i) {
        string numero;
        getline(cin, numero);
        cantidad_num(lista_num, stoi(numero));
    }

    return 0;
}