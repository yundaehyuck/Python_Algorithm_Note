from collections import deque

def bfs(a,k):
    
    queue = deque([(a,0)])

    visited = [0] * (1000001)

    visited[a] = 1

    while queue:
        
        a,c = queue.popleft()

        for o in [1,2]:
            
            if o == 1:
                
                if a + 1 <= 1000000 and visited[a+1] == 0:

                    if a+1 == k:

                        return c+1

                    else:
                        
                        visited[a+1] = 1

                        queue.append((a+1,c+1))
            
            elif o == 2:
                
                if a*2 <= 1000000 and visited[2*a] == 0:
                    
                    if 2*a == k:
                        
                        return c+1
                    
                    else:
                        
                        visited[2*a] = 1
                        queue.append((2*a,c+1))



a,k = map(int,input().split())

print(bfs(a,k))