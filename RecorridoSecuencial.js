const VACIO = -1;

let matriz = [
    [1, 2, VACIO, 4],
    [5, VACIO, 7, 8],
    [VACIO, 10, 11, VACIO]
];

let filas = matriz.length;
let columnas = matriz[0].length;

console.log("Matriz original");

for (let i = 0; i < filas; i++) {
    let linea = "";
    for (let j = 0; j < columnas; j++) {
        if (matriz[i][j] !== VACIO)
            linea += matriz[i][j] + " ";
        else
            linea += "-1 ";
    }
    console.log(linea);
}
for (let i = 0; i < filas; i++) {
    for (let j = 0; j < columnas; j++) {
        if (matriz[i][j] === VACIO) {
            for (let k = i + 1; k < filas; k++) {
                if (matriz[k][j] !== VACIO) {
                    matriz[i][j] = matriz[k][j];
                    matriz[k][j] = VACIO;
                    break;
                }
            }
        }
    }
}
console.log("\nMatriz recorrida");
for (let i = 0; i < filas; i++) {
    let linea = "";
    for (let j = 0; j < columnas; j++) {
        if (matriz[i][j] !== VACIO)
            linea += matriz[i][j] + " ";
        else
            linea += "-1 ";
    }
    console.log(linea);
}