from sys import stdin

n = int(stdin.readline())

grid = list(map(int,stdin.readline().split()))

sorted_grid = sorted(set(grid))

compression = {}

i = 0

for g in sorted_grid:
    
    compression[g] = i
    i += 1

for g in grid:
    
    print(compression[g], end = " ")