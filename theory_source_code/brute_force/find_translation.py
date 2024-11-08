#A의 모든 점이 얼마나 평행이동 해야 B의 부분집합이 될 수 있는가?
from sys import stdin

m = int(stdin.readline())

A = []

for _ in range(m):
    
    x,y = map(int,stdin.readline().split())
    A.append((x,y))

n = int(stdin.readline())

B = {}

for i in range(n):
    
    x,y = map(int,stdin.readline().split())

    B[(x,y)] = i

delta = []

#A의 모든 점은 동일한 양 (dx,dy)만큼 이동해야하므로
#A의 한 점이 B의 각각 점에 대하여 이동해야하는 양 (dx,dy)를 모두 구해놓은 다음
X = A[0][0]
Y = A[0][1]

for x,y in B:
    
    delta.append((x - X,y - Y))

#이동해야하는 양 (dx,dy)에 대하여
for dx,dy in delta:
    
    #서로 다른 두 점 (x1,y1), (x2,y2)에 대하여 (dx,dy)만큼 이동시킬 때 (x1+dx,y1+dy), (x2+dx,y2+dy)는 반드시 서로 다른 두 점임
    #visited로 체크할 필요 없음
    no = False

    for i in range(m):
        
        x,y = A[i] #A의 각 점을 모두 이동시켜본 다음

        if B.get((x + dx, y + dy),-1) == -1: #B에 속하는지 체크
            
            no = True
            break
    
    if no == False: #(dx,dy)만큼 이동시킬때 B에 속하게 된다면
        
        break

print(dx,dy)