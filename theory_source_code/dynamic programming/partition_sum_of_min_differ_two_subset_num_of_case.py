#원소 합의 차이가 최소가 되도록 두 집합으로 분할하는 방법의 수를 구하는 문제
from sys import stdin

n = int(stdin.readline())

v = []

total = 0

for _ in range(n):
    
    w = int(stdin.readline())
    v.append(w)
    total += w

#절반에 가깝게 분할하는 것이 최적
target = total//2

#dp[i] = 집합에서 일부 원소를 골라 합이 i가 될 수 있는가?
dp = [0]*(target+1)
dp[0] = 1

#count[i] = 집합에서 일부 원소를 골라 합이 i가 되는 경우의 수
count = [0]*(target+1)
count[0] = 1
mod = 1000000

for w in v:
    
    for i in range(target,w-1,-1):
        
        if dp[i-w] == 1:
            
            dp[i] = 1
            count[i] += count[i-w]
            count[i] %= mod

team1 = 0

#절반에 가까울수록 최적
for i in range(target,-1,-1):
    
    if dp[i] == 1:

        team1 = i
        break

team2 = total - team1

print(abs(team1-team2))
print(count[team1])