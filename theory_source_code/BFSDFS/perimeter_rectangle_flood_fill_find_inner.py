from collections import deque
from sys import stdin

#사각형들로 둘러쌓인 연결된 도형의 둘레의 길이 구하기
#도형의 내부 구멍의 둘레는 구하지 않는다

n = int(stdin.readline())

#핵심은 전체 영역의 주변에 패딩을 씌운다
maps = [[0]*(102) for _ in range(102)]
visited = [[0]*102 for _ in range(102)]

for _ in range(n):
    
    x,y = map(int,stdin.readline().split())
    maps[y][x] = 1
    visited[y][x] = 2 #건초는 2로 표시

#1~100에만 더미가 존재하고, 패딩은 확실하게 외부이므로, (0,0)부터 BFS시작
#외부영역을 1로 표시
queue = deque([(0,0)])

while queue:
    
    x,y = queue.popleft()

    for a,b in [[0,1],[1,0],[0,-1],[-1,0]]:
        
        dx = x + a
        dy = y + b

        if dx >= 0 and dx <= 101 and dy >= 0 and dy <= 101:
            
            if visited[dy][dx] == 0:
                
                visited[dy][dx] = 1
                queue.append((dx,dy))

#건초더미로 표시된 2의 상하좌우를 살펴봐서, 1의 개수를 세면 그것이 외부 둘레의 길이가 된다
p = 0

for y in range(1,101):
    
    for x in range(1,101):
        
        if visited[y][x] == 2:
            
            for a,b in [[0,1],[1,0],[0,-1],[-1,0]]:
                
                dx = x + a
                dy = y + b

                if visited[dy][dx] == 1:
                    
                    p += 1

print(p)