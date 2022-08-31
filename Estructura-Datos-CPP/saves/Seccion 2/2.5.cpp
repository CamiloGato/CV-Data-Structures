#include <iostream>
#include "vector"
#include "cstring"
#include "tuple"

using namespace std;

vector<int> get_vector(string texto, const char *delim){
    int suma = 0;
    int n = texto.length();
    char char_array[n + 1];
    strcpy(char_array, texto.c_str());

    vector<int> numeros;

    char *ptr;
    ptr = strtok(char_array, delim);

    while (ptr != NULL)
    {
        suma += stoi(ptr);
        numeros.insert( numeros.end() ,stoi(ptr));
        ptr = strtok (NULL, " , ");
    }

    return numeros;
}

string quien(int n){
    switch (n){
        case 0: return "SO";
        case 1: return "LAR";
        case 2: return "IS";
        default: return "ERROR";
    }
}

vector<int> cual(int n, vector<int> maso1 = {}, vector<int> maso2 = {}, vector<int> maso3 = {}){
    switch (n%3){
        case 0: return maso1;
        case 1: return maso2;
        case 2: return maso3;
        default: return {};
    }
}

int puntuacion(int j, vector<int> so, vector<int> lar, vector<int> is){
    int puntos = 0;
    for (int i = 0; i < so.size(); ++i) {
        if ( cual(j, so, lar, is)[i]%2 == ( cual(j, so, lar, is)[i] + cual(j+1, so, lar, is)[i] + cual(j+2, so, lar, is)[i])%2 ){
            puntos++;
        }

    }
    return puntos;
}

int main(){
    string n;
    getline(cin, n);

    string maso1;
    getline(cin, maso1);

    vector<int> so = get_vector(maso1, ", ");

    string maso2;
    getline(cin, maso2);

    vector<int> lar = get_vector(maso2, ", ");

    string maso3;
    getline(cin, maso3);

    vector<int> is = get_vector(maso3, ", ");

    for (int j = 0; j < 3; ++j) {
        cout << quien(j) << ":" << puntuacion(j, so, lar, is);
        if (j != 2){
            cout << ", ";
        }
    }

    return 0;
}