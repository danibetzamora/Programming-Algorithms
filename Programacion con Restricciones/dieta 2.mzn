include "table.mzn";
include "alldifferent.mzn";

int: min_energy;
int: min_protein;
int: max_salt;
int: max_fat;

set of FOOD: desserts;
set of FOOD: mains;
set of FOOD: sides;
enum FEATURE = { name, energy, protein, salt, fat, cost};
enum FOOD;
array[FOOD, FEATURE] of int: dd;

set of FOOD: special_foods;   % Conjunto de comidas especiales
int: max_special_foods;       % Máximo de comidas especiales que podemos utilizar
int: num_main; 
    
array[FEATURE, 1..num_main] of var int: main;
array[FEATURE] of var int: side;
array[FEATURE] of var int: dessert;
var int: budget;

constraint forall(n in 1..num_main)(main[name, n] in mains);
constraint alldifferent([main[name, n] | n in 1..num_main]);
constraint side[name] in sides;
constraint dessert[name] in desserts;
constraint forall(n in 1..num_main)(table(main[..,n], dd));
constraint table(side, dd);
constraint table(dessert, dd);
constraint sum(n in 1..num_main)(main[energy, n]) + side[energy] + dessert[energy] >= min_energy;
constraint sum(n in 1..num_main)(main[protein, n]) + side[protein] + dessert[protein] >= min_protein;
constraint sum(n in 1..num_main)(main[salt, n]) + side[salt] + dessert[salt] <= max_salt;
constraint sum(n in 1..num_main)(main[fat, n]) + side[fat] + dessert[fat] <= max_fat;
constraint budget = sum(n in 1..num_main)(main[cost, n]) + side[cost] + dessert[cost];

var int : max_main = sum([ 1 | food in special_foods, n in 1..num_main where main[name, n] == food]);
var int : max_side = sum([ 1 | food in special_foods where side[name] == food]);
var int : max_dessert = sum([ 1 | food in special_foods where dessert[name] == food]);

constraint (max_main + max_side + max_dessert) <= max_special_foods;

solve minimize budget;

output [
  if i = 1 then "main= " else ", " endif ++
    show(to_enum(FOOD, main[name,i]))
  | i in 1..num_main
];

output [" side = ", show(to_enum(FOOD,side[name])),
        ", dessert = ", show(to_enum(FOOD,dessert[name])),
        ", cost = ", show(budget), "\n"];