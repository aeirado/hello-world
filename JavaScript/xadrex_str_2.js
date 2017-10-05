//tabuleiro de xadrez
//construir um tab de xadrez com "#" e " " em
// uma string e separar cada linha com "\n"

var cadeia = "", num_linhas = 8, chave = 1;
var p = "#", b = " ";

for (var i = 1; i <= num_linhas; i++) {
    
    for (var j = 1; j <= 8; j++) {
        if (chave) {
            cadeia += p;
            chave = 0;
        } else {
            cadeia += b;
            chave = 1;
        }
    }

    if (i%2 == 0) {
        p = "#", b = " ";
    } else {
        b = "#", p = " ";
    }
    if (i < num_linhas) {
        cadeia += "\n";
    }
}

print(cadeia);