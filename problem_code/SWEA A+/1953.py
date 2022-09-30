from collections import deque

def bfs(c,r,l,m,n,maps,d):
    
    visited = [[0]*m for _ in range(n)]

    queue = deque([(c,r,maps[r][c]-1)])

    visited[r][c] = 1

    if l == 1:
        
        return 1
    
    else:
        
        ans = 0
        
        ##l시간 동안 이동
        for _ in range(l-1):
            
            ##각 시간마다 큐의 길이만큼 BFS 탐색을 반복함
            
            for _ in range(len(queue)):
            
                x,y,dir = queue.popleft()

                for ni,nj in d[dir]:
                    
                    dx = x + ni
                    dy = y + nj

                    if dx >= 0 and dx <= m-1 and dy >= 0 and dy <= n-1 and visited[dy][dx] == 0 and maps[dy][dx] != 0:
                            
                            ##이동 불가능한 경우를 모두 고려한다
                            
                        if maps[y][x] == 1:
                            
                            if ni == 1 and nj == 0:
                                
                                if maps[dy][dx] in [2,4,5]:
                                    
                                    continue
                            
                            elif ni == -1 and nj == 0:
                                
                                if maps[dy][dx] in [2,6,7]:
                                    
                                    continue
                            
                            elif ni == 0 and nj == 1:
                                
                                if maps[dy][dx] in [3,5,6]:
                                    
                                    continue
                            
                            elif ni == 0 and nj == -1:
                                
                                if maps[dy][dx] in [3,4,7]:
                                    
                                    continue
                            
                        if maps[y][x] == 2:
                            
                            if nj == -1 and ni == 0: ##올라갈때
                                
                                if maps[dy][dx] in [3,4,7]:

                                    continue

                            elif nj == 1 and ni == 0:

                                if maps[dy][dx] in [3,5,6]:

                                    continue

                        elif maps[y][x] == 3:

                            if ni == -1:

                                if maps[dy][dx] in [2,6,7]:

                                    continue


                            elif ni == 1:

                                if maps[dy][dx] in [2,4,5]:
                                    
                                    continue
                        
                        elif maps[y][x] == 4:
                            
                            if ni == 0 and nj == -1:

                                if maps[dy][dx] in [3,4,7]:

                                    continue

                            elif ni == 1 and nj == 0:

                                if maps[dy][dx] in [2,4,5]:

                                    continue

                        elif maps[y][x] == 5:

                            if ni == 1 and nj == 0:

                                if maps[dy][dx] in [2,4,5]:

                                    continue

                            elif ni == 0 and nj == 1:

                                if maps[dy][dx] in [3,5,6]:

                                    continue

                        elif maps[y][x] == 6:

                            if ni == -1 and nj == 0:

                                if maps[dy][dx] in [2,6,7]:

                                    continue

                            elif ni == 0 and nj == 1:

                                if maps[dy][dx] in [3,5,6]:

                                    continue

                        elif maps[y][x] == 7:

                            if ni == -1 and nj == 0:

                                if maps[dy][dx] in [2,6,7]:

                                    continue

                            elif ni == 0 and nj == -1:

                                if maps[dy][dx] in [3,4,7]:

                                    continue 
                        
                        queue.append((dx,dy,maps[dy][dx]-1))

                        visited[dy][dx] = visited[y][x] + 1

##이동 후에 0보다 큰 곳은 이동했다는 의미이므로, 이동한 곳을 모두 센다.
        for y in range(n):
            
            for x in range(m):
                
                if visited[y][x] > 0:
                    
                    ans += 1

        return ans




T = int(input())

for t in range(1,T+1):
    
    n,m,r,c,l = map(int,input().split())

    maps = [list(map(int,input().split())) for _ in range(n)]

##터널 타입별로 이동가능한 델타배열
    d = [[[0,1],[1,0],[0,-1],[-1,0]], [[0,1],[0,-1]], [[1,0],[-1,0]], [[0,-1],[1,0]], [[0,1],[1,0]], [[0,1],[-1,0]], [[0,-1],[-1,0]]]

    print('#'+str(t),bfs(c,r,l,m,n,maps,d))