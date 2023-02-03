int : n;

array[1..n] of var 1..9 : x;

constraint sum(x) == product(x);

constraint forall(i,j in 1..n where i < j)(x[i] <= x[j]);

solve maximize sum(x);

output["x = array1d(1..\(n), \(x));"];