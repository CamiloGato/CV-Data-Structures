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

        string longitud;
        getline(cin, longitud);

        string lista;
        getline(cin, lista);
        vector<int> vector = get_vector(lista, " ");

        int contador = 0;
        int aux = 0;
        do{
            int valor = vector[aux];
            if ( vector[aux] + vector[aux+valor] == 0 ){
                contador++;
                break;
            }
            aux += valor;
            contador++;

        } while ( 0 < aux && aux < stoi(longitud) );

        cout << contador << endl;

    }

    return 0;
}