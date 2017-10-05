//programa para gerar um array de numeros inteiros
//aleatórios e verificar se são inteiros mesmo

function num_aleatorio(semente, multiplica, c) {
    var num = (multiplica * semente + c) % 1000;
    return num;
}

var tam = 100;
var c = 1;
var semente = 54563;
var multiplica = 12;
var lista_inteiros = [];

for (var i = 0; i < tam; i++) {
    var item = num_aleatorio(semente, multiplica, c);
    lista_inteiros[i] = item;
    semente = item;
    multiplica += i;
    c--;
}

print("Array aleatório: ", lista_inteiros);

var A = lista_inteiros;

for (var i = 1; i < A.length; i++){
    var a_comparar;
    a_comparar = A[i];
    var anterior;
    anterior = i - 1;

    while (anterior >= 0 && a_comparar < A[anterior]){
        A[anterior + 1] = A[anterior];
        i--;
        anterior--;
    }
    A[i] = a_comparar;
}

print("\nArray ordenado: ", A);