#서로 겹치는 구간 쌍의 개수
from sys import stdin

n = int(stdin.readline())

L = []
R = []

for _ in range(n):
    
    l,r = map(int,stdin.readline().split())

    L.append(l)
    R.append(r)

L.sort()
R.sort()

#n개의 구간 중 2개를 선택하면 전체 구간 쌍의 개수
answer = n*(n-1)//2

#서로 겹치지 않는 구간 쌍의 개수를 구해 빼준다

#어떤 구간 [Li,Ri]가 [Lj,Rj]와 겹치지 않는다면 Rj < Li
#i = 0,1,2,...에 대하여 Rj < Li인 j의 개수

#L,R을 서로 정렬해두면 Rj < Li < Li+1
#j는 계속 증가
j = 0

for i in range(n):

    while R[j] < L[i]:
        
        j += 1
    
    answer -= j

print(answer)