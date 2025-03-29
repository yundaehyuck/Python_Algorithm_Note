#가장 많은 점을 포함하는 사각형을 찾는 방법
from sys import stdin

n,m,l,k = map(int,stdin.readline().split())

A = []

for _ in range(k):
    
    a,b = map(int,stdin.readline().split())
    A.append((a,b))

#가장 많은 점을 포함하는 정사각형 배치는 항상 존재하고,
#여전히 그 점들을 포함하게 정사각형을 이동시킬 수 있다
#이때 임의의 두 점(A,B)를 아래쪽 변, 왼쪽 변에 오도록 배치할 수 있다
# A의 x좌표, B의 y좌표를 기준으로 하여 (x,x+l), (y,y+l)안의 점의 개수를 세면 된다
answer = 0

for i in range(k):
    
    for j in range(k):
            
        x,y = A[i][0],A[j][1]

        count = 0

        for a,b in A:
      
            if a >= x and a <= x+l and b >= y and b <= y+l:
            
                count += 1

        answer = max(answer,count)

print(k-answer)