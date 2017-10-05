var A = [72, 1, 34, 5.6, 41, 12, "55", 0, -87, 32, 6, 17];
print("\nArray inicial: ", A);

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