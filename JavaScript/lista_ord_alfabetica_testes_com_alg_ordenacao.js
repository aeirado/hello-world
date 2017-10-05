/*
Dados e Fatos:
1 - um array de caracteres desordenado
2 - Para saber se 2 caracteres são um maior que o outro, o JS usa a tabela UTF8
3 - Na tabela UTF8 as letras maiúsculas são menores que as minúsculas e as letras
    acentuadas funcionam da mesma forma, mas são maiores que aquelas não acentuadas
4 - No português o fato de: a. as letras serem acentuadas ou não acentuadas não
    altera a ordem alfabética; b. as maiúsculas e as minúsculas têm precedência
    diferente. EX: AaBbCcEe....

Processamento:
1 - o array de caracteres desordenados será composto na mão
2 - não usar a tabela UTF8, construir função que gera uma tabela
    própria para ordem alfabética no português => usar type {} ou Object
3 - com a tabela posso comparar os caracteres em termos de maior ou menor
4 - para ordenar tenho que percorrer o array de caracteres e
    comparar os valores encontrados trocá-los qdo i > i+1
5 - o array estará ordenado qdo i > i+1 valer para todos os caracteres 
*/
 
function ordenacao_alfabetica() {
    var tabela_ordenacao = {};
    var letras_ordenadas = "AÁÂÃÀaáâãàBbCcÇçDdEÉÊeéêFfGgHhIÍÎiíîJj" +
                           "KkLlMmNnOÓÔÕoóôõPpQqRrSsTtUÚÛuúûWwVvXxYyZz";
    
    for (var i = 0; i < letras_ordenadas.length; i++) {
        tabela_ordenacao[letras_ordenadas[i]] = i;
    }
    return tabela_ordenacao
}

var tabela = ordenacao_alfabetica();


//Abaixo código para mostrar e testar a tabela:
/*var j = 0;
var lista_comp = [];

for (var i in tabela) {
    lista_comp += i;
    if (i != 'A') {
        print('{' + lista_comp[j-1] + ' : ' + tabela[lista_comp[j-1]] + '}' +
              ' é menor que {' + i + ' : ' + tabela[i] +
              '} ?', (tabela[lista_comp[j-1]] < tabela[i]));
    }
    j++;
}*/


var lista_letras = ['n','h','B','o','e','j','k','f','A','z','w','ç',
'ã','G','û','O','p','W','q','Ê','i','ó','H','s','a','r','Â','y','C',
'b','Í','l','i','d','Û','x','D','À'];

//Primeiro algoritmo de ordenação alfabética
document.writeln("\nLista de letras inicial: ", lista_letras);
var tam_list = lista_letras.length;

while (tam_list != 0) {
    var novo_tam_lista = 0;
    for (var i = 0; i < tam_list; i++) {
        if (tabela[lista_letras[i]] > tabela[lista_letras[i+1]]) {
            var temp = lista_letras[i+1];
            lista_letras[i+1] = lista_letras[i];
            lista_letras[i] = temp;
            novo_tam_lista = i;
        }
    }
    tam_list = novo_tam_lista;
}

document.writeln("\nLista de letras ordenada: ", lista_letras);


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