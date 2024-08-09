#x를 2^30으로 나눈 나머지가 a라면
#x를 2^1,2,3,...,29로 나눈 나머지는 a를 2^1,2,3,...,29로 나눈 나머지와 같다
from sys import stdin

dp = [0]*(10**6+1)
dp[0] = 1

mod = 2**30

for i in range(1,10**6+1):
    
    for j in range(1,3):
        
        if i >= j:

            dp[i] += (dp[i-j])
            dp[i] %= mod

z = int(stdin.readline())

for _ in range(z):
    
    s,p = map(int,stdin.readline().split())
    
    print(dp[s] % (2**p))