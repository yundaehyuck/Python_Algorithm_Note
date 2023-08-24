#정육면체를 쌓은 도형의 겉넓이 구하기
from sys import stdin

n,m = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

answer = 0

#위,아래
answer += 2*(1*n*m)

#해당방향으로 순회하는데, 인접한 원소끼리 차이가 양수면 그 차이만큼을 더해나가면 된다
#왼쪽, 오른쪽

for y in range(n):
    
    answer += maps[y][0]
    
    #고정된 행 y에 대하여 각 열을 왼쪽에서 오른쪽으로 순회
    for x in range(1,m):
        
        if maps[y][x] - maps[y][x-1] > 0:
            
            answer += (maps[y][x] - maps[y][x-1])
    
    answer += maps[y][m-1]
    
    #고정된 행 y에 대하여 각 열을 오른쪽에서 왼쪽으로 순회

    for x in range(m-2,-1,-1):
        
        if maps[y][x] - maps[y][x+1] > 0:
            
            answer += (maps[y][x] - maps[y][x+1])
        
#앞,뒤

for x in range(m):
    
    answer += maps[0][x]
    
    #고정된 열 x에 대하여 각 열을 위에서 아래로 순회
    for y in range(1,n):
        
        if maps[y][x] - maps[y-1][x] > 0:
            
            answer += (maps[y][x] - maps[y-1][x])
    
    answer += maps[n-1][x]
    
    #고정된 열 x에 대하여 각 열을 아래에서 위로 순회

    for y in range(n-2,-1,-1):
        
        if maps[y][x] - maps[y+1][x] > 0:
            
            answer += (maps[y][x] - maps[y+1][x])
            
print(answer)