from collections import namedtuple
from solve       import *

Item = namedtuple("Item", ['index', 'value', 'weight'])

first_line = input().split() 	# N, Capacity
N          = int(first_line[0])
capacity   = int(first_line[1])

items = []
for i in range(1, N+1):
    parts = input().split()
    items.append(Item(i, int(parts[0]), int(parts[1])))

value, taken = solve_tabulation(items, capacity)
print(value, taken)
