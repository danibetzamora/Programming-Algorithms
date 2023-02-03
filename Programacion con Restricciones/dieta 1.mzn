include "table.mzn";
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
    
array[FEATURE] of var int: main;
array[FEATURE] of var int: side;
array[FEATURE] of var int: dessert;
var int: budget;

constraint main[name] in mains;
constraint side[name] in sides;
constraint dessert[name] in desserts;
constraint table(main, dd);
constraint table(side, dd);
constraint table(dessert, dd);
constraint main[energy] + side[energy] + dessert[energy] >=min_energy;
constraint main[protein]+side[protein]+dessert[protein] >=min_protein;
constraint main[salt] + side[salt] + dessert[salt] <= max_salt;
constraint main[fat] + side[fat] + dessert[fat] <= max_fat;
constraint budget = main[cost] + side[cost] + dessert[cost];

var int : max_main = sum([ 1 | food in special_foods where main[name] == food]);
var int : max_side = sum([ 1 | food in special_foods where side[name] == food]);
var int : max_dessert = sum([ 1 | food in special_foods where dessert[name] == food]);

%var int : max_main = sum(food in special_foods where main[name] == food)(1);
%var int : max_side = sum(food in special_foods where side[name] == food)(1);
%var int : max_dessert = sum(food in special_foods where dessert[name] == food)(1);

constraint (max_main + max_side + max_dessert) <= max_special_foods;

solve minimize budget;

output ["main = ", show(to_enum(FOOD,main[name])),
        ", side = ", show(to_enum(FOOD,side[name])),
        ", dessert = ", show(to_enum(FOOD,dessert[name])),
        ", cost = ", show(budget), "\n"];