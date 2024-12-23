#원형 배열에서 i번 원소를 선택하면 인접한 i-1,i+1번 원소를 선택할 수 없을때,
#적절히 선택하여 원소 합을 최대로 만드는 방법

def solution(sticker):
    answer = 0
    
    n = len(sticker)
    
    #n = 1인 경우 해당 원소를 선택하는게 무조건 최대
    if n == 1:
        
        return sticker[0]
    
    #dp[i] = i번까지 봤을떄, 원소 합의 최댓값
    #i번을 선택하지 않은 경우 dp[i-1]
    #i번을 선택한다면 i-1번은 선택할 수 없으므로 dp[i-2] + A[i]
    
    #0번 원소를 선택하는 경우
    dp1 = [0]*n
    
    dp1[0] = sticker[0]

    for i in range(1,n-1):
        
        if i >= 2:
            
            dp1[i] = max(dp1[i-1],dp1[i-2] + sticker[i])
        
        else:
            
            dp1[i] = dp1[i-1]
    
    dp1[n-1] = dp1[n-2]
    
    v1 = dp1[n-1]
    
    #0번 원소를 선택하지 않는 경우
    dp2 = [0]*n
    
    dp2[1] = sticker[1]
    
    for i in range(2,n):
            
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
        
    v2 = dp2[n-1]
    
    return max(v1,v2)