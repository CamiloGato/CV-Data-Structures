#include <iostream>
#include "vector"
#include "cstring"
#include "tuple"

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

int main(){

    string n;
    getline(cin, n);

    for (int i = 0; i < stoi(n); ++i) {
        string lista;
        getline(cin, lista);

        vector<int> numeros = get_vector(lista, " ");
        sort(numeros.begin(), numeros.end());

        int actual = numeros[0];
        int suma = 0;
        for (int j = 0; j < numeros.size() - 1; ++j) {
            if (j == numeros.size() - 1 ) {
                cout << suma << endl;
                break;
            }
            if ( actual != numeros[j] ) {
                cout << suma << " ";
                suma = 0;
            }
            actual = numeros[j];
            suma++;
        }

        cout << endl;

    }

    return 0;
}