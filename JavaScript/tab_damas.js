//tabuleiro de Damas
//construir um tab de Damas com "#" e " " em
//um arr de arrs

"use strict";
const num_linhas = 8;
var tabuleiro = [], linha = [];
var cp = "|#", cb = "| ";

for (var l = 0; l <= num_linhas; l++) {
    tabuleiro[l] = linha;
}

for (var i = 0; i < num_linhas; i++) {    
    for (var j = 0; j < num_linhas; j++) {
        if ((i + j) % 2 === 0) {
            tabuleiro[i][j] = cp;
        } else {
            tabuleiro[i][j] = cb;
        }
    }
}

console.log(tabuleiro);