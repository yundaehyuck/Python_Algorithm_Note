#n*n배열에서 B*B 크기의 부분행렬이 포함하는 원소의 최대 최소 차이
from collections import deque
from sys import stdin

n,b,k = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

#maxrow[y][x] = 행 y에 대하여 x,x+1,..,x+b-1열 구간의 최댓값
#minrow[y][x] = 행 y에 대하여 x,x+1,...,x+b-1열 구간의 최솟값
maxrow = [[0]*n for _ in range(n)]
minrow = [[0]*n for _ in range(n)]

#deque를 이용한 슬라이딩 윈도우 최대 최소 트릭으로 최대 최소를 O(N^2)에 찾는다
for y in range(n):
    
    max_queue = deque([])
    min_queue = deque([])
    j = 0

    for i in range(b):
        
        while max_queue and maps[y][i] >= maps[y][max_queue[-1]]:
            
            max_queue.pop()
        
        while min_queue and maps[y][i] < maps[y][min_queue[-1]]:
            
            min_queue.pop()
        
        max_queue.append(i)
        min_queue.append(i)
    
    maxrow[y][0] = maps[y][max_queue[0]]
    minrow[y][0] = maps[y][min_queue[0]]
    j += 1

    for x in range(b,n):
        
        while max_queue and x-b >= max_queue[0]:

            max_queue.popleft()
        
        while min_queue and x-b >= min_queue[0]:
            
            min_queue.popleft()

        while max_queue and maps[y][x] >= maps[y][max_queue[-1]]:

            max_queue.pop()
        
        while min_queue and maps[y][x] < maps[y][min_queue[-1]]:
            
            min_queue.pop()

        max_queue.append(x)
        min_queue.append(x)

        maxrow[y][j] = maps[y][max_queue[0]] 
        minrow[y][j] = maps[y][min_queue[0]]
        j += 1 

#maxdp[y][x] = (x,y)가 왼쪽 위일때 b*b 크기의 부분행렬의 최댓값
#maxrow[y][x], maxrow[y+1][x],...,maxrow[y+b-1][x]중 최댓값

#mindp[y][x] = (x,y)가 왼쪽 위일때 b*b 크기의 부분행렬의 최솟값
#minrow[y][x], minrow[y+1][x],... minrow[y+b-1][x]중 최솟값
maxdp = [[0]*n for _ in range(n)]
mindp = [[0]*n for _ in range(n)]

for x in range(n):
    
    max_queue = deque([])
    min_queue = deque([])
    j = 0

    for i in range(b):
        
        while max_queue and maxrow[i][x] >= maxrow[max_queue[-1]][x]:
            
            max_queue.pop()
        
        while min_queue and minrow[i][x] < minrow[min_queue[-1]][x]:
            
            min_queue.pop()
        
        max_queue.append(i)
        min_queue.append(i)
    
    maxdp[0][x] = maxrow[max_queue[0]][x]
    mindp[0][x] = minrow[min_queue[0]][x]
    j += 1

    for y in range(b,n):
        
        while max_queue and y-b >= max_queue[0]:

            max_queue.popleft()
        
        while min_queue and y-b >= min_queue[0]:
            
            min_queue.popleft()

        while max_queue and maxrow[y][x] >= maxrow[max_queue[-1]][x]:

            max_queue.pop()
        
        while min_queue and minrow[y][x] < minrow[min_queue[-1]][x]:
            
            min_queue.pop()

        max_queue.append(y)
        min_queue.append(y)

        maxdp[j][x] = maxrow[max_queue[0]][x] 
        mindp[j][x] = minrow[min_queue[0]][x]
        j += 1 


for _ in range(k):
    
    y,x = map(int,stdin.readline().split())
    y -= 1
    x -= 1

    print(maxdp[y][x] - mindp[y][x])