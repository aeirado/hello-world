// este é um teste
var rl = require('readline-sync');
console.log("Digite um numero inteiro por favor:");
var a = rl.prompt();
console.log("O número é: " + a + "\n");
if (a < 20) {
    console.log('tá funcionando!');
} else {
    console.log('merda!!!');
}
