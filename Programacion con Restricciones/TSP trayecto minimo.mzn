%TSP trayecto parcial mínimo

include "globals.mzn";
int: numCities;          % número de ciudades
set of int: City = 1..numCities; 
int: maxAllowedEdge;     % máxima distancia permitida de un trayecto del recorrido

% distancia entre ciudades 
% -1 significa que no hay conexión directa
array[City,City] of int: distance; 
array[City] of var int : succ;
array[City] of var int : values;

constraint circuit(succ);

constraint forall(i in City)(distance[i,succ[i]] != 0 /\ distance[i,succ[i]] != -1 /\ distance[i,succ[i]] <= maxAllowedEdge);

constraint forall(i in City)(values[i] == distance[i,succ[i]]);

solve minimize max(values);

%output["\(succ)\n\(sum(i in City)(distance[i,succ[i]]))\n\(values)\n\(max(values))"];
output["\(values)\nsucc = array1d(\(City), \(succ));\nmaxEdge = \(max(values));"];