from sys import stdin

n = int(stdin.readline())

cost_list = []

for _ in range(n):
    
    c = int(stdin.readline())

    cost_list.append(c)

cost_list.sort(reverse=True)

cost = 0

for i in range(1,n+1):
    
    if i % 3 == 0:
        
        continue
    
    else:
        
        cost += cost_list[i-1]

print(cost)