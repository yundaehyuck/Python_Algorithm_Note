def solution(ability):
    
    n = len(ability)
    m = len(ability[0])
    
    p = max(n,m) #사람 수와 직업 수중 더 큰 값으로
    
    dp = [0]*(1 << p)
    
    for perm in range(1 << p):
        
        x = 0
        
        for j in bin(perm)[2:]:
            
            if j == '1':
                
                x += 1
                
        for i in range(p):
            
            if perm & (1 << i) == 0:
                
                #행렬 범위를 벗어나면(인덱스 에러 나는 경우) 0으로 하면 된다
                if x >= n or i >= m:
                    
                    cost = 0
                
                else:
                    
                    cost = ability[x][i]
                    
                dp[perm|(1 << i)] = max(dp[perm|(1<<i)], dp[perm] + cost)
        
    return dp[2**p-1]