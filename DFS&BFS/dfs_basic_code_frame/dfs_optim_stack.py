visited = [0] * n

def dfs(v,visited):
    
    stack = [v]
    
    while stack:
        
        v = stack.pop()
        
        if visited[v] == 1:
            
            continue
        
        visited[v] = 1
        
        for w in adjlist[v]:
            
            if visited[w] == 0:
                
                stack.append(w)