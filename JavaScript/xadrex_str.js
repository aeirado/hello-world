//tabuleiro de xadrez
//construir um tab de xadrez com "#" e " " em
// uma string e separar cada linha com "\n"

var cadeia = "";
var num_linhas = 8;
var chave = 1;
var pb = "# "; // casa preta e casa branca
var bp = " #"; // inverso

for (var i = 1; i <= num_linhas; i++) {
    for (var j = 1; j <= 4; j++) {
        if (chave) {
            cadeia += pb;
        } else {
            cadeia += bp;
        }
    }
    if (chave) {
        chave = 0;
    } else {
        chave = 1;
    }
    if (i < num_linhas) {
        cadeia += "\n";
    }
}

print(cadeia);