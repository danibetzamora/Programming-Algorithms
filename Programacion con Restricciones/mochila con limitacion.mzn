int : n;
int : capacity;
set of int : ITEMS = 1 .. n;
array[ITEMS] of int : value;
array[ITEMS] of int : weight;

set of ITEMS: limitation;
int : m;

array[ITEMS] of var 0..1 : taken;

constraint sum(i in ITEMS) (taken[i] * weight[i]) <= capacity;
constraint sum(i in limitation) (taken[i]) <= m;

var int : total = sum(i in ITEMS) (taken[i] * value[i]);

solve maximize total;

output ["{"] ++ [show(i) ++ if i == n then "" else "," endif | 
       i in ITEMS where fix(taken[i]) == 1] ++ 
       ["}\n\(total)"];
