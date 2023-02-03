% Perfect Match minimum cost

include "globals.mzn";

int: n;
set of int: VERTEX = 1..n;

array[VERTEX, VERTEX] of int: weights;

array[VERTEX] of var VERTEX: edge;

constraint forall(i in VERTEX)(edge[edge[i]] == i /\ edge[i] != i);

var int : total = sum(i in VERTEX)(weights[i,edge[i]]) div 2;

solve minimize total;

output["\(total)->\(edge)"];