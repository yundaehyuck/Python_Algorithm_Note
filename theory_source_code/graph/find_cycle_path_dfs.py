def dfs(u,path):
    
    global count

    if visited[u]:
        
        if visited[u] == -1:
            
            #u로 왔는데, 사이클이 탐지되었다
            
            #그동안 저장된 path는 도달한 노드를 순서대로 
            #u > u1 > u2 > .... > un이 저장되어 있다
            
            #path를 차례대로 순회해서 u의 위치를 알아낸다.
            
            #[u1,u2,u3,...,un]에서 j번이 u라면...
         
            #path[j:]가 사이클이다
            
            for j in range(len(path)):
                
                if path[j] == u:

                    break

            count += (len(path) - j)
            #print(path[j:]) #실제 사이클

            return True
        
        return False
    
    visited[u] = -1
    
    #도달한 노드 u를 path에 저장
    path.append(u)
    
    #다음 노드 A[u]로 이동
    dfs(A[u]-1,path)
    
    visited[u] = 1