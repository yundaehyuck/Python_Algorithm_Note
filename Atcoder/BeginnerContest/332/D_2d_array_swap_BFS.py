from collections import deque
from copy import deepcopy

h,w = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(h)]
B = [list(map(int,input().split())) for _ in range(h)]

#2차원 배열의 모든 행을 튜플로 바꾼다
#딕셔너리에 저장할려면 리스트는 안되고 튜플로 바꿔줘야함
def to_tuple(A):
    
    return tuple(tuple(r) for r in A)

def bfs(A,B,h,w):

    p = deepcopy(A)
    
    #배열 자체를 상태로 두고
    visited = {to_tuple(A):1,to_tuple(B):-1}
    
    #키를 넣어봤을때, 값이 -1이라면 B가 되었다는 뜻이다
    if visited[to_tuple(p)] == -1:
        
        return 0

    queue = deque([(p,0)]) #(배열, 바꾼 횟수)

    while queue:
        
        p,c = queue.popleft()
        
        #행부터 바꿔보고
        for i in range(h-1):
                
            q = deepcopy(p)

            q[i],q[i+1] = q[i+1],q[i]
            
            #방문 상태 체크
            #키가 없다면 아직 방문하지 않은 배열 상태
            if visited.get(to_tuple(q),0) == 0:
                
                visited[to_tuple(q)] = 1
                queue.append((q,c+1))
            
            #value가 -1이라면 목적 배열 B가 되었다는 뜻이니 바로 바꾼 횟수 c+1을 return
            elif visited.get(to_tuple(q),0) == -1:
                
                return c+1
        
        #행을 바꿔봤으면 열도 바꿔본다
        for i in range(w-1):
            
            q = deepcopy(p)

            for y in range(h):
            
                q[y][i],q[y][i+1] = q[y][i+1],q[y][i]

            if visited.get(to_tuple(q),0) == 0:
                
                visited[to_tuple(q)] = 1
                queue.append((q,c+1))
            
            elif visited.get(to_tuple(q),0) == -1:
                
                return c+1
        
        #각 큐에 행끼리 바꾼 배열, 열끼리 바꾼 배열들이 들어가있는데..
        #매번 큐에서 꺼내면서 행끼리만 바꾼 배열은 또 열도 바꿔보고
        #열끼리만 바꾼 배열은 또 행도 바꿔보면서...
        #모든 행과 열을 서로 바꿔보는 완전탐색이 된다
    
    return -1

print(bfs(A,B,h,w))