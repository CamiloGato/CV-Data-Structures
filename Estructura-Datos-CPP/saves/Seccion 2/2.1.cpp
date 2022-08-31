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

int main() {
    string cantidad;
    getline(cin, cantidad);
    string texto;
    getline(cin, texto);

    vector<int> numeros = get_vector(texto, ", ");

    string n_intervalos;
    getline(cin, n_intervalos);

    for (int i = 0; i < stoi(n_intervalos); ++i) {
        int cantidad = 0;
        string intervalo;
        getline(cin, intervalo);
        vector<int> intervalo_num = get_vector(intervalo, " ");

        for (auto &num: numeros){
            if (intervalo_num[0] <= num && num <= intervalo_num[1]){
                cantidad++;
            }
        }

        cout << cantidad << endl;
    }

}