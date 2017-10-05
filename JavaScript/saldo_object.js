// Objeto Saldo. Treinando OOP em JavaScript.
function Saldo(valor){
    this.saldo = valor; // propriedade
    this.saque = saque; // função
    this.deposito = deposito; // função
    this.mostra_saldo = mostra_saldo; // função
}

function deposito(valor){
    this.saldo += valor;
}

function saque(valor){
    if (valor <= this.saldo){
        this.saldo -= valor;
    }
    if (valor > this.saldo){
        print("\nVocê não tem fundos suficientes\npara fazer esse saque!\n")
    }
}

function mostra_saldo(){
    return "Saldo: " + this.saldo;
}

var conta = new Saldo(500);
conta.deposito(1000);
print(conta.mostra_saldo());
conta.saque(600);
print(conta.mostra_saldo());
conta.saque(1000);
print(conta.mostra_saldo());
