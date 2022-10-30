from sys import stdin

#보라색 블록을 제외한 나머지 블록을 그려서 합을 구해보는 함수
def dfs(x,y,n,m,maps,visited,s,sum_value,max_maps):
    
    global max_value
    
    #만약 현재 전체 최댓값이, block이 읽을 수 있는 가능한 최댓값 
    #sum_value + max_maps*(4-s)보다 크다면
    #더 이상 탐색할 필요가 없다
    if max_value > sum_value + max_maps*(4-s):
        
        return
        
    #길이가 4가 된다면, 탐색을 중지하고 최댓값 갱신
    if s == 4:
        
        if max_value < sum_value:
            
            max_value = sum_value
    
    else:

        for ni,nj in [[0,1],[1,0],[0,-1],[-1,0]]:
            
            dx = x + ni
            dy = y + nj

            if dx >= 0 and dx <= m-1 and dy >= 0 and dy <= n-1 and visited[dy][dx] == 0:
                
                #탐색을 하다가 길이가 2가 된다면
                #보라색 블록을 그리기 위해 
                if s == 2:
                    
                    visited[dy][dx] = 1
                    #현재 지점 (x,y)에서 다시 dfs를 수행한다
                    #이때 길이 1을 더해주고, 다음 값을 읽은 상태로 들어가면
                    #읽은 지점으로 가지 않고 다른 지점으로 이동할 수 있잖아
                    dfs(x,y,n,m,maps,visited,s+1,sum_value+maps[dy][dx],max_maps)
                    visited[dy][dx] = 0
                
                #여기는 보라색 블록 말고 다른 블록을 그리도록 if문이랑 상관없이 계속 수행
                visited[dy][dx] = 1
                dfs(dx,dy,n,m,maps,visited,s+1,sum_value+maps[dy][dx],max_maps)
                visited[dy][dx] = 0

n,m = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

#2차원 배열에서 가장 큰 값을 찾는다
#maps는 각 원소가 리스트인 2차원 리스트인데
#map(max,maps)를 한다면, 각 원소별로 최댓값을 찾아서 하나의 리스트가 나올거고
#거기서 또 max를 하면 전체 max가 나오겠지
max_maps = max(map(max,maps))

visited = [[0]*m for _ in range(n)]

max_value = 0

for y in range(n):
    
    for x in range(m):
        
        #시작 지점을 방문 처리하고,
        visited[y][x] = 1
        
        #시작 지점의 합을 읽어서 DFS를 들어가야지
        #길이는 1이고
        dfs(x,y,n,m,maps,visited,1,maps[y][x])
        
        #탐색이 끝나면, 시작 지점 복구하고 visited를 원래 초기 상태로
        #이러면 visited를 다시 만들 필요가 없다
        visited[y][x] = 0

print(max_value)