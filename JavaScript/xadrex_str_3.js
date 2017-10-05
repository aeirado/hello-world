//tacbuleiro de Damas
//construir um tab de Damas com "#" e " " em
// um arr

var cadeia = "", num_linhas = 8;
var cp = "|#", cb = "| ";

for (var i = 0; i < num_linhas; i++) {
    
    for (var j = 0; j < 8; j++) {
        if ((i + j) % 2 === 0) {
            cadeia += cp;
        } else {
            cadeia += cb;
        }
    }

    if (i < num_linhas) {
        cadeia += "|\n";
    }
}

console.log(cadeia);