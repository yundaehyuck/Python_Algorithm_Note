#어떤 지점까지 함께 가고 나머지는 a,b로 나눠서 갈때 최소 거리를 구하는 방법
def solution(n, s, a, b, fares):
    
    INF = 1000000000000000000000000000000000000
    
    dp = [[INF]*(n+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        dp[i][i] = 0
    
    for p,q,f in fares:

        dp[p][q] = f
        dp[q][p] = f
    
    #플로이드 워셜로 어떤 지점 i에서 모든 지점 j = 1,2,..,n까지 최소 거리를 찾는다
    for k in range(1,n+1):
        
        for i in range(1,n+1):
            
            for j in range(1,n+1):
                
                dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
    
    #s에서 k까지 함께 간다고 하고, k에서 a, k에서 b로 나눠서 간다고 하자.
    #그러면 dp[s][k] + dp[k][a] + dp[k][b]의 최솟값을 구하는 문제가 된다.
    answer = INF
    
    for k in range(1,n+1):
        
        if answer > dp[s][k] + dp[k][a] + dp[k][b]:
            
            answer = dp[s][k] + dp[k][a] + dp[k][b]
            
    return answer