// Fatorial recursivo
function fatorial(num){
    if (num == 1){
        return num;
    }
    else{
        return num * fatorial(num - 1);
    }
}

print(fatorial(5));
print(fatorial(10));