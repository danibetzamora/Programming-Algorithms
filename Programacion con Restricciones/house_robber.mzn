int: n;
array[1..n] of int: value;
array[1..n] of var 0..1 : taken;

constraint forall(i,j in 1..n where j = i + 1)(taken[i] * taken[j] = 0);

var int : total_value = sum(i in 1..n)(taken[i] * value[i]);

solve maximize total_value;

output["taken= \(taken)\ntotal_value= \(total_value)"];
