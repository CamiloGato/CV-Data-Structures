#include <iostream>
#include "vector"
#include "cstring"

using namespace std;

vector<string> get_vector(string texto, const char *delim){
    int n = texto.length();
    char char_array[n + 1];
    strcpy(char_array, texto.c_str());

    vector<string> numeros;

    char *ptr;
    ptr = strtok(char_array, delim);

    while (ptr != NULL)
    {
        numeros.insert( numeros.end() ,ptr);
        ptr = strtok (NULL, " , ");
    }
    return numeros;
}

int main(){
    string n;
    getline(cin, n);
    string texto;
    getline(cin, texto);
    vector<string> arreglo = get_vector(texto, ", ");
    for (int i = 0, id1 = 0, id2 = 0, act1 = 0; i < arreglo.size(); i++) {
        act1 = (act1+1)%2;
        int act2 = (act1+1)%2;
        cout << arreglo[(id1)*(act1) + (stoi(n)-(id2))*(act2)];
        if (!act1){
            id1++;
        } else {
            id2++;
        }
    }

    return 0;
}