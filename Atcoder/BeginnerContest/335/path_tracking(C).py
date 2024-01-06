from sys import stdin

n,q = map(int,stdin.readline().split())

h_x = 1
h_y = 0

path = [(i,0) for i in range(n,0,-1)]

delta = {'R':[1,0], 'L':[-1,0], 'U':[0,1], 'D':[0,-1]}

for _ in range(q):
    
    a,b = stdin.readline().rstrip().split()

    if a == '1':
        
        h_x += delta[b][0]
        h_y += delta[b][1]

        path.append((h_x,h_y))

    else:
        
        b = int(b)
        
        print(*path[-b])