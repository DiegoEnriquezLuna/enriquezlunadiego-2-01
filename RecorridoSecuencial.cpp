#include <iostream>

using namespace std;

int main() {
    const int filas = 3;
    const int columnas = 4;

    const int VACIO = -1;

    int matriz[filas][columnas] = {
        {1, 2, VACIO, 4},
        {5, VACIO, 7, 8},
        {VACIO, 10, 11, VACIO}
    };

    cout << "Matriz original\n";

    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            if (matriz[i][j] != VACIO)
                cout << matriz[i][j] << " ";
            else
                cout << "-1 ";
        }
        cout << endl;
    }

    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            if (matriz[i][j] == VACIO) {
                for (int k = i + 1; k < filas; k++) {
                    if (matriz[k][j] != VACIO) {
                        matriz[i][j] = matriz[k][j];
                        matriz[k][j] = VACIO;
                        break;
                    }
                }
            }
        }
    }

    cout << "\nMatriz recorrida\n";

    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            if (matriz[i][j] != VACIO)
                cout << matriz[i][j] << " ";
            else
                cout << "-1 ";
        }
        cout << endl;
    }

    return 0;
}