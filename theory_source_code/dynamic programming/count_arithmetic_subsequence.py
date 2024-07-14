#배열의 일부를 골라 길이가 i = 1,2,3,..,n인 등차수열을 만드는 방법의 수를 구하기

n = int(input())
A = list(map(int,input().split()))

dp = [[{} for _ in range(n+1)] for _ in range(n+1)]

for i in range(n): #끝 항
    
    for j in range(i): #0~i-1항
        
        d = A[i] - A[j] #공차
        
        #끝항이 A[i], 길이가 2, 공차가 d
        dp[i][2][d] = dp[i][2].get(d,0) + 1

mod = 998244353

for i in range(3,n+1): #길이
    
    for j in range(n): #끝항
        
        for k in range(j): #0~j-1항
            
            d = A[j] - A[k] #공차
            
            #끝항이 A[j]이고 길이가 i이며 공차가 d인 등차수열은..
            #끝항이 A[k]이고 길이가 i-1이며 공차가 d인 등차수열이 존재한다면..
            dp[j][i][d] = dp[j][i].get(d,0) + dp[k][i-1].get(d,0)
            dp[j][i][d] %= mod

result = [n] #길이가 1인 경우는 n개

for i in range(2,n+1): #길이가 2부터

    v = 0

    for j in range(n):
        
        for d in dp[j][i]: #끝항이 A[j]이고 길이가 i인 dp[j][i]의 모든 공차 d에 대하여
            
            v += dp[j][i][d]
            v %= mod
    
    result.append(v)