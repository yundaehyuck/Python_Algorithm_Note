from collections import deque
from sys import stdin

def bfs(n,m,T):
    
    #그람 획득 여부
    sword = 0
    
    #좌표,그람 획득 여부
    queue = deque([(0,0,0)])
    
    #3차원 방문 배열, x,y,그람여부
    visited = [[[0,0] for _ in range(m)] for _ in range(n)]

    visited[0][0][0] = 1

    t = 0 #시간

    while queue:
        
        t += 1

        if t > T: #제한시간을 넘어가면 반복문 종료
            
            break
        
        for _ in range(len(queue)): #매 초마다 큐의 길이만큼 탐색 수행
        
            x,y,sword = queue.popleft()

            for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
                
                dx = x + ni
                dy = y + nj

                if sword == 0: #검이 없는 경우
                    
                    #벽은 이동 불가능
                    if dx >= 0 and dx <= m-1 and dy >= 0 and dy <= n-1 and visited[dy][dx][sword] == 0 and maps[dy][dx] != 1:
                        
                        #탐색하다가 그람을 만나면...
                        if maps[dy][dx] == 2:
                            
                            sword = 1 #검을 획득
                        
                        #탐색하다가 목표지점에 도달한다면 그것이 최단시간
                        if dx == m-1 and dy == n-1:
                            
                            return t
                        
                        queue.append((dx,dy,sword))
                        visited[dy][dx][sword] = 1
                
                else: #검이 있는 경우
                    
                    #maps와는 상관없이 이동가능
                    if dx >= 0 and dx <= m-1 and dy >= 0 and dy <= n-1 and visited[dy][dx][sword] == 0: #어디든 갈 수 있음
                        
                        #탐색하다가 목표지점 m-1,n-1에 도달하면 그것이 최단시간
                        if dx == m-1 and dy == n-1:
                            
                            return t

                        queue.append((dx,dy,sword))
                        visited[dy][dx][sword] = 1
    
    #반복문이 끝나더라도 return하지 못하면 목표지점에 도달하지 못했다
    return -1
        

n,m,T = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

result = bfs(n,m,T)

#목표지점에 도달하지 못하면..
if result == -1:
    
    print('Fail')

#목표지점에 도달했으면..
else:
    
    print(result)