visited = [0] * n

def dfs(v,visited):
    
    visited[v] = 1
    
    stack = []
    
    while 1:
        
        for w in adjlist[v]:
            
            if visited[w] == 0:
                
                stack.append(v)
                
                v = w
                visited[v] = 1
                
                break
        
        else:
            
            if stack == []:
                
                break
            
            else:
                
                v = stack.pop()