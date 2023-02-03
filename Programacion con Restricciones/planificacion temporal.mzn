%Planificacion temporal

include "cumulative.mzn";

int : n; % total programas

int : k; % numero total de programadores

int : max_tiempo; % limite superior de tiempo

array [1..n] of int : tiempo;
array [1..n] of int : prog;

array [1..n] of var 0..max_tiempo : comienzo;
var 0..max_tiempo : total;

constraint cumulative(comienzo, tiempo, prog, k);
constraint forall(i in 1..n)(comienzo[i] + tiempo[i] <= total);

solve minimize total;

output["Total: "++show(total)++"\n"]++[show(comienzo[i])++" " | i in 1..n];