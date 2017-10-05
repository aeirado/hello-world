/*
====================
REGRAS JOGO DE DAMAS
====================
1 - O jogo de damas é praticado em um tabuleiro de 64 casas, claras
    e escuras. A grande diagonal (escura), deve ficar sempre
    à esquerda de cada jogador. O objetivo do jogo é imobilizar ou
    capturar todas as peças do adversário.

2 - O jogo de damas é praticado entre dois parceiros, com 12 pedras
    brancas de um lado e com 12 pedras pretas de outro lado.

3 - O lance inicial cabe sempre a quem estiver com as peças brancas.

4 - A pedra anda só para frente, uma casa de cada vez. Quando a pedra
    atinge a oitava linha do tabuleiro ela é promovida à dama.

5 - A dama é uma peça de movimentos mais amplos. Ela anda para frente e
    para trás, quantas casas quiser. A dama não pode saltar uma peça da
    mesma cor.

6 - A captura é obrigatória. Não existe sopro.

7 - Duas ou mais peças juntas, na mesma diagonal, não podem ser captu-
    radas.

8 - A pedra captura a dama e a dama captura a pedra. Pedra e dama
    têm o mesmo valor para capturarem ou serem capturadas.

9 - A pedra e a dama podem capturar tanto para frente como para trás,
    uma ou mais peças

10 - Se no mesmo lance se apresentar mais de um modo de capturar, é
     obrigatório executar o lance que capture o maior número de peças
     (Lei da Maioria).

11 - A pedra que durante o lance de captura de várias peças, apenas
     passe por qualquer casa de coroação, sem aí parar, não será
     promovida à dama.

12 - Na execução do lance do lance de captura, é permitido passar mais de
     uma vez pela mesma casa vazia, não é permitido capturar duas vezes a
     mesma peça.

13 - Na execução do lance de captura, não é permitido capturar a mesma peça
     mais de uma vez e as peças capturadas não podem ser retiradas do tabu-
     leiro antes de completar o lance de captura.

14 - Empate:
     Após 20 lances sucessivos de damas, sem captura ou deslocamento de
     pedra, a partida é declarada empatada.
     Ou em finais de:
     2 damas contra 2 damas;
     2 damas contra uma;
     2 damas contra uma dama e uma pedra;
     1 dama contra 1 dama, e, 1 dama contra 1 dama e 1 pedra, são decla-
     rados empatados após 5 lances.

OBS: Também joga-se damas em um tabuleiro de 100 casas, com 20 pedras
     para cada lado (Damas Internacional).

*/
 
'use strict'
const pp = '☻';
const pb = '☺';
const dp = '■';
const db = '□';
var tabuleiro = [
                 [' ', '#', ' ', '#', ' ', '#', ' ', '#'],
                 ['#', ' ', '#', ' ', '#', ' ', '#', ' '],
                 [' ', '#', ' ', '#', ' ', '#', ' ', '#'],
                 ['#', ' ', '#', ' ', '#', ' ', '#', ' '],
                 [' ', '#', ' ', '#', ' ', '#', ' ', '#'],
                 ['#', ' ', '#', ' ', '#', ' ', '#', ' '],
                 [' ', '#', ' ', '#', ' ', '#', ' ', '#'],
                 ['#', ' ', '#', ' ', '#', ' ', '#', ' ']
                ];

function str_tab() {
    var linha_str = '';
    var tab_str = '';
    for (var i = 0; i < tabuleiro.length; i++) {
        for (var j = 0; j < tabuleiro.length; j++) {
            linha_str += '|' + tabuleiro[i][j];
        }
        tab_str += linha_str + '|\n';
        linha_str = '';
    }
    return tab_str;
}

function print_tab(rotulo, tab) {
    //console.log(tab);
    document.getElementById('tabuleiro').innerHTML = rotulo + tab;
}

function coloca_pecas(p, indice) {
    for (var i = indice; i < (indice + 3); i++) {
        for (var j = 0; j < tabuleiro.length; j++) {
            if (tabuleiro[i][j] === '#') {
                tabuleiro[i][j] = p;
            }
        }
    }
}

function move_peca () {
    var qual_peca, linha, coluna;
    qual_peca = prompt('Qual peça? Digite as coordenadas com inteiros <linha, coluna>  >> ');
    linha = prompt('Digite a linha [0-7] >> ');
    coluna = prompt('Digite a coluna [0-7] >> ');    
}


print_tab('TABULEIRO VAZIO\n', str_tab());

coloca_pecas(pp, 0);
coloca_pecas(pb, 5);

print_tab('TABULEIRO CHEIO\n', str_tab());