#어떤 집합을 합의 차이가 최소가 되도록 두 집합으로 분할하는데
#두 집합 각각 원소의 개수 차이가 1 이하가 되도록
from sys import stdin

n = int(stdin.readline())

w = []

total = 0

for _ in range(n):
    
    k = int(stdin.readline())
    w.append(k)
    total += k

t1 = total//2

#dp[i][j] = 1번팀의 원소 개수가 j개이며, 원소 합이 i가 될 수 있는가?
dp = [[0]*(n//2+2) for _ in range(t1+1)]
dp[0][0] = 1

for k in w:
    
    for i in range(t1,k-1,-1):
        
        for j in range(1,n//2+2):
            
            if dp[i-k][j-1] == 1:

                dp[i][j] = 1

#집합 원소의 개수가 짝수냐, 홀수냐에 따라 가능한 경우가 다르다
if n % 2 == 0:
    
    m = [n//2]

else:
    
    m = [n//2,n//2+1]

#절반에 최대한 가깝게 분할하는 것이 최적
team1 = 0

for i in range(t1,-1,-1):
    
    find = False
    
    for j in m:
        
        if dp[i][j] == 1:
            
            team1 = i
            find = True
            break
            
    if find:
        
        break
                
team2 = total - team1

if team1 > team2:
    
    print(team2,team1)

else:
    
    print(team1,team2)