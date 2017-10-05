function factorial(number){
	var product = 1;
	for (var i = number; i >= 1; i--){
		product *= i;
	}
	return product
}

print("factorial de 4:", factorial(4));
print("factorial de 5:", factorial(5));
print("factorial de 10:", factorial(10));
