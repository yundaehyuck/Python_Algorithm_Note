from collections import deque
from sys import stdin

def zero_one_bfs(x,k):
    
    queue = deque([x])

    dist = [10000000000000000000000000000000000000]*(100001)

    dist[x] = 0

    while queue:
        
        x = queue.popleft()

        if x == k:
            
            return dist[k]

        for i in [1,-1,2]:
            
            if i == 1 or i == -1:

                if x+i >= 0 and x+i <= 100000:

                    if dist[x+i] > dist[x] + 1:

                        dist[x+i] = dist[x]+1
                        queue.append((x+i))

            else:
                
                if 2*x >= 0 and 2*x <= 100000:

                    if dist[2*x] > dist[x]:

                        dist[2*x] = dist[x]
                        queue.appendleft((2*x))

                
n,k = map(int,stdin.readline().split())

print(zero_one_bfs(n,k))