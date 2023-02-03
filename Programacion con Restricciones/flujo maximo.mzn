int: num_nodes;                          % número de nodos del grafo
int: num_edges;                          % número de aristas del grafo

1..num_nodes:source;                     % nodo fuente
1..num_nodes:sink;                       % nodo sumidero

array[1..num_edges, 1..2] of int: edges; % aristas del grafo (origen->destino)
array[1..num_edges] of int: capacity;    % capacidad de cada arista

var int: max_flow;                       % variable de decision para el valor
                                         % del flujo máximo
array[1..num_edges] of var int: flow;    % variable de decisión para el flujo
                                         % final de cada arista

constraint max_flow >= 0;
constraint forall(i in 1..num_edges) (flow[i] >= 0 /\ flow[i] <= capacity[i]);
constraint forall(n in 1..num_nodes where n != source /\ n != sink)(sum(i in 1..num_edges where edges[i,1] == n)(flow[i]) == sum(j in 1..num_edges where edges[j,2] == n)(flow[j])); 
constraint sum(i in 1..num_edges where edges[i,2] == sink)(flow[i]) == max_flow;

solve maximize max_flow;

output
[ 
  "max flow =" ++ show(max_flow) ++ "\n\(flow)"
];