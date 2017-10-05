/*
Dados e Fatos:
1 - 

Processamento:
1 - 
*/
 
function ordenacao_alfabetica () {
    var tabela_ordenacao = {};
    var letras_ordenadas = "AÁÂÃÀaáâãàBbCcÇçDdEÉÊeéêFfGgHhIÍÎiíîJjKk"+
                           "LlMmNnOÓÔÕoóôõPpQqRrSsTtUÚÛuúûWwVvXxYyZz";

    for (var i = 0; i < letras_ordenadas.length; i++) {
        tabela_ordenacao[letras_ordenadas[i]] = i;
    }
    return tabela_ordenacao
}

var tabela = ordenacao_alfabetica();


//Primeiro algoritmo de ordenação alfabética
function ordena_nomes () {
    var chave = true;

    while (chave) {
        chave = false;
        for (var i = 0; i < lista_letras.length; i++) {
            if (tabela[lista_letras[i]] > tabela[lista_letras[i+1]]) {
                var temp = lista_letras[i+1];
                lista_letras[i+1] = lista_letras[i];
                lista_letras[i] = temp;
                chave = true;
            } 
        }
    }
}


//Segundo algoritmo de ordenação alfabética
/*document.writeln("\nLista de letras inicial: ", lista_letras);

for (var i = 1; i < lista_letras.length; i++){
    var a_comparar = lista_letras[i];
    var anterior = i - 1;

    while (anterior >= 0 && tabela[a_comparar] < tabela[
           lista_letras[anterior]]){
        lista_letras[anterior + 1] = lista_letras[anterior];
        i--;
        anterior--;
    }
    lista_letras[i] = a_comparar;
}
document.writeln("\nLista de letras ordenada: ", lista_letras);
*/