from sys import stdin

n,k = map(int,stdin.readline().split())

money = []

for _ in range(n):
    
    m = int(stdin.readline())

    money.append(m)

dp = [0]*(k+1)

dp[0] = 1

#N가지 도구를 사용해 합이 K가 되는 방법의 수 
#구성이 같은데 순서가 다르면 같은 경우로 세는 방법의 수
#도구를 먼저 순회하고, 목표로 만들고자 하는 0~K를 순회한다
for m in money:
    
    for i in range(1,k+1):
      
      if i >= m:
          
          dp[i] += dp[i-m]

print(dp[k])