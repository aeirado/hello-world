// Gerar lista de NOMES: "nome sobrenome"
function gerar_NOMES (tamanho_NOMES){
    var nomes = [], sobrenomes = [], NOMES = [];
    var nome;
    nomes = read("prog/nomes.txt").split(',');
    sobrenomes = read("prog/sobrenomes.txt").split(',');
    for (var i = 0; i < tamanho_NOMES; i++) {
        var nome_rand = nomes[Math.floor(Math.random() * nomes.length)];
        var sobrenome_rand = sobrenomes[Math.floor(Math.random() * sobrenomes.length)];
        nome = nome_rand + " " + sobrenome_rand;
        NOMES[i] = nome;
    }
    return NOMES;
}

// Gera lista de nomes na forma "sobrenome, nome"
function sobrenome_nome (NOMES) {
    var list_sobrenome_nome = [];
    var nome_mesmo, sobrenome, nome, temp;
    var nome_temp = [];
    for (var i = 0; i < NOMES.length; i++) {
        nome_mesmo = "";
        sobrenome = "";
        nome = "";
        temp = "";
        nome_temp = NOMES[i];
        for (var j = nome_temp.length - 1; j >= 0 ; j--) {
            if (nome_temp[j] == " ") {break;};
            temp += nome_temp[j];
        }
        for (var k = temp.length - 1; k >= 0; k--) {
            sobrenome += temp[k];
        }
        for (var l = 0; l < nome_temp.length - sobrenome.length - 1; l++) {
            nome += nome_temp[l];
        }
        nome_mesmo = sobrenome + ", " + nome;
        list_sobrenome_nome[i] = nome_mesmo;
    }
    return list_sobrenome_nome; 
}

// Examina letras acentuadas e ç -> troca pelas não acentuadas e c
// Essa função só serve para o português
function troca_letras(l) {
    switch (l) {
        case "Á": l = "A"; break;
        case "Â": l = "A"; break;
        case "Ã": l = "A"; break;
        case "á": l = "a"; break;
        case "â": l = "a"; break;
        case "ã": l = "a"; break;
        case "É": l = "E"; break;
        case "Ê": l = "E"; break;
        case "é": l = "e"; break;
        case "ê": l = "e"; break;
        case "Í": l = "I"; break;
        case "Î": l = "I"; break;           
        case "í": l = "i"; break;
        case "î": l = "i"; break;
        case "Ô": l = "O"; break;
        case "Ó": l = "O"; break;
        case "Õ": l = "O"; break;
        case "ó": l = "o"; break;
        case "ô": l = "o"; break;
        case "õ": l = "o"; break;
        case "Ú": l = "U"; break;
        case "Û": l = "U"; break;
        case "ú": l = "u"; break;
        case "û": l = "u"; break;
        case "Ç": l = "C"; break;
        case "ç": l = "c"; break;
        default: break;
    }
    return l
} 

// compara 2 nomes até uma certa letra
function comp_nome(nome1, nome2, num_l) {
    if (nome1.length < num_l && nome1.length < nome2.length) {
        num_l = nome1.length;            
    }
    else if (nome2.length < num_l && nome2.length < nome1.length) {
        num_l = nome2.length;
    }
    for (var i = 0; i < num_l; i++) {
        if (troca_letras(nome1[i]) == "," || troca_letras(nome1[i]) == " ") {
            continue;
        }
        if (troca_letras(nome2[i]) == "," || troca_letras(nome2[i]) == " ") {
            continue;
        }
        if (troca_letras(nome1[i]) == troca_letras(nome2[i])) {
            if (i + 1 == num_l) {
                return [nome1, nome2];
            }
            continue;
        }
        else if (troca_letras(nome1[i]) < troca_letras(nome2[i])) {
            return [nome1, nome2];
        }
        else {
            return 0;
        }
    }
}

// Ordena alfabeticamente a lista de nomes
function ordena_alfabeticamente(lista, num_l) {
    var nomes;
    for (var i = 0; i < lista.length; i++) {
        for (var j = 0; j < lista.length; j++) {
            nomes = comp_nome(lista[i], lista[j], num_l);
            if (nomes == 0) {
                continue;
            }
            lista[i] = nomes[1];
            lista[j] = nomes[0];
            // print(lista);
        }
    }
    return lista;
}

var lista_nomes = gerar_NOMES(100);
var lista_a_ordenar = sobrenome_nome(lista_nomes);
// var teste = ["Zuleica", "Ana", "Deobaldo", "Ivanildo", "Carla", "André", "Eduardo", "Ricardo", "Fabio"];
var resultado = ordena_alfabeticamente(lista_a_ordenar, 20);
for (var i = 0; i < resultado.length; i++) {
    if (i >= 100) {
        print(i + ") " + resultado[i]);
    } else if (i >= 10) {
        print(" " + i + ") " + resultado[i]);
    } else {
        print("  " + i + ") " + resultado[i]);
    }
    
}