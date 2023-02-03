var 0..10 : x;

constraint x mod 4 == 0;

var int : pow = pow(x - 7, 2);

solve minimize pow;

output["x=\(x)\nobj=\(pow)"]