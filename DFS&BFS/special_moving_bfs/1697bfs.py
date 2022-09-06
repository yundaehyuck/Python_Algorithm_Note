#https://www.acmicpc.net/problem/1697
from collections import deque
from sys import stdin

def bfs(n,k):
    
    visited = [0] * 100001

    queue = deque([n])
    
    visited[n] = 1

    while queue:
        
        n = queue.popleft()

        for j in [-1,1,n]:
            
            dn = n + j

            if dn >= 0 and dn <= 100000 and visited[dn] == 0:
                
                queue.append(dn)
                visited[dn] = visited[n] + 1

                if dn == k:
                    
                    return visited[dn] - 1
                
n,k = map(int,stdin.readline().split())

if n == k:
    
    print(0)

else:

    print(bfs(n,k))