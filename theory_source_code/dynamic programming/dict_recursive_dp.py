#boj 1351
from sys import stdin

def dfs(i,dp):
    
    #만약 A[i]를 이미 구했다면, 그대로 접근해서 return
    if dp.get(i,0) != 0:
        
        return dp[i]
    
    #A[i]를 구하지 않았다면,
    else:
        
        #i//p와 i//q를 재귀호출해서 A[i]를 구한다
        dp[i] = dfs(i//p,dp)+dfs(i//q,dp)

        return dp[i]

n,p,q = map(int,stdin.readline().split())

#A[n]을 저장할 dict
dp = {}

#A[0] = 1
dp[0] = 1

print(dfs(n,dp))