// tentando construir um quicksort algoritmo

var A = [34,98,6,56,3,12,41,90,4,0,34,52,6,13,1,17];

function valor_medio(list) {
    var soma = 0;
    for (var i = 0; i < list.length; i++) {
        soma += list[i];
    }
    console.log(i);
    return Math.floor(soma/(i));
}
var med = valor_medio(A);
console.log(med);