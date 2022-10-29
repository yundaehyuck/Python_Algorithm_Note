n = 4 ##물건의 개수

weight = [0,5,4,6,3]
value = [0,10,40,30,50]

w = 10 ##가방 무게

dp = [[-1]*(w+1) for _ in range(n+1)]

##0행과 0열을 채운다

##물건이 존재하지 않으면.. 담을 수 없으므로 가치는 0
for W in range(w+1):
    
    dp[0][W] = 0

##남은 용량이 없으면.. 담을수 없으므로 가치는 0
for i in range(n+1):
    
    dp[i][0] = 0

#1행 1열부터 채워넣는다
for i in range(1,n+1):
    
    for W in range(1,w+1):
        
        if W >= weight[i]: ##담을 물건 i의 무게가.. 남아있는 물건의 무게 이하라면..
            
            ##해당 물건은 담을 수 있으므로..
            dp[i][W] = max(dp[i-1][W-weight[i]]+value[i], dp[i-1][W])
        
        else: ##무게가 i번이 남은 용량보다 더 커서 담을 수 없다면..
            
            dp[i][W] = dp[i-1][W]

print(dp[n][w])
"""
90
"""