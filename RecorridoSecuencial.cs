using System;

class Program
{
    static void Main()
    {
        int VACIO = -1;
        int[,] matriz =
        {
            {1, 2, VACIO, 4},
            {5, VACIO, 7, 8},
            {VACIO, 10, 11, VACIO}
        };
        int filas = matriz.GetLength(0);
        int columnas = matriz.GetLength(1);
        Console.WriteLine("Matriz original");
        for (int i = 0; i < filas; i++)
        {
            for (int j = 0; j < columnas; j++)
            {
                if (matriz[i, j] != VACIO)
                    Console.Write(matriz[i, j] + " ");
                else
                    Console.Write("-1");
            }
            Console.WriteLine();
        }
        for (int i = 0; i < filas; i++)
        {
            for (int j = 0; j < columnas; j++)
            {
                if (matriz[i, j] == VACIO)
                {
                    for (int k = i + 1; k < filas; k++)
                    {
                        if (matriz[k, j] != VACIO)
                        {
                            matriz[i, j] = matriz[k, j];
                            matriz[k, j] = VACIO;
                            break;
                        }
                    }
                }
            }
        }
        Console.WriteLine("\nMatriz recorrida");
        for (int i = 0; i < filas; i++)
        {
            for (int j = 0; j < columnas; j++)
            {
                if (matriz[i, j] != VACIO)
                    Console.Write(matriz[i, j] + " ");
                else
                    Console.Write("-1");
            }
            Console.WriteLine();
        }
    }
}