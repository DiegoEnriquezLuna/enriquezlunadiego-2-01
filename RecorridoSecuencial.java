public class Main {
    public static void main(String[] args) {
        final int VACIO = -1;
        int[][] matriz = {
            {1, 2, VACIO, 4},
            {5, VACIO, 7, 8},
            {VACIO, 10, 11, VACIO}
        };
        int filas = matriz.length;
        int columnas = matriz[0].length;
        System.out.println("Matriz original");
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                if (matriz[i][j] != VACIO)
                    System.out.print(matriz[i][j] + " ");
                else
                    System.out.print("-1 ");
            }
            System.out.println();
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
        System.out.println("\nMatriz recorrida");
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                if (matriz[i][j] != VACIO)
                    System.out.print(matriz[i][j] + " ");
                else
                    System.out.print("-1 ");
            }
            System.out.println();
        }
    }
}