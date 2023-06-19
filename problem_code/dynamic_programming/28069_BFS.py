from collections import deque

n,k = map(int,input().split())

queue = deque([0])

visited = [0]*(n+1)

visited[0] = 1

for _ in range(k):
    
    x = len(queue)

    for _ in range(x):
        
        i = queue.popleft()

        if i+1 <= n and visited[i+1] == 0:
            
            queue.append(i+1)
            visited[i+1] = 1
        
        if i+i//2 <= n and visited[i+i//2] == 0:
            
            queue.append(i+i//2)
            visited[i+i//2] = 1

if visited[n] == 1:
    
    print("minigimbob")

else:
    
    print("water")