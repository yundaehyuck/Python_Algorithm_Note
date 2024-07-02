#가방이 여러개인 배낭 문제

from sys import stdin

P = int(stdin.readline())

for p in range(1,P+1):
    
    #첫번째 가방 무게 제한이 w1, 두번째 가방 무게 제한이 w2
    n,w1,w2 = map(int,stdin.readline().split())

    W = list(map(int,stdin.readline().split()))
    V = list(map(int,stdin.readline().split()))
    
    #dp[i][j] = 첫번째 가방에 담긴 물건 무게 합이 i, 두번째 가방에 담긴 물건 무게 합이 j
    #일때 물건 무게 가치 합의 최댓값
    dp = [[0]*(w2+1) for _ in range(w1+1)]

    for i in range(n):
        
        w = W[i]
        v = V[i]
        
        #역순으로 순회해야 물건이 중복해서 안담김
        for j in range(w1,-1,-1):
            
            for k in range(w2,-1,-1):
                
                if j-w >= 0:
                    
                    dp[j][k] = max(dp[j-w][k] + v, dp[j][k])
                
                if k-w >= 0:
                    
                    dp[j][k] = max(dp[j][k-w] + v, dp[j][k])
    
    print(f'Problem {p}: {dp[w1][w2]}')