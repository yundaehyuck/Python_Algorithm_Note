#dp[i] = 배열 v의 원소를 일부 골라 합해서 i를 만들 수 있는가?
target = total//2

dp = [0]*(target+1)
dp[0] = 1

for w in v:
    
    for i in range(target,w-1,-1):
        
        if dp[i-w] == 1: #i-w가 될 수 있다면,
            
            dp[i] = 1 #i-w에 w를 더하면 i가 될 수 있다.