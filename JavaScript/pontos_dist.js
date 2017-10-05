var pontos = [
    {x : 0, y : 0},
    {x : 1, y : 1}
];

pontos.dist = function () {
    var p1 = this[0];
    var p2 = this[1];
    var a = p2.x - p1.x;
    var b = p2.y - p1.y;
    var distancia = Math.sqrt(a * a + b * b);
};
var resultado = pontos.dist();
print(String(resultado));