visited = [0] * n

def dfs(v,visited):
    
    visited[v] = 1
    
    for w in adjlist[v]:
        
        if visited[w] == 0:
            
            dfs(w,visited)