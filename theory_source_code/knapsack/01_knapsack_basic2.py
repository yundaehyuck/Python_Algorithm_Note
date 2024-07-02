#1차원 배열을 이용한 0-1 knapsack
n,k = map(int,input().split())

bag = []

for _ in range(n):
    
    w,v = map(int,input().split())
    bag.append((w,v))

#dp[i] = 가방에 담긴 물건 무게가 i일때, 물건 가치 합의 최댓값
dp = [0]*(k+1)

#가방 물건을 먼저 순회하고,
for w,v in bag:
    
    #무게를 역순으로 순회해야 한번 담긴 물건이 중복해서 안담김
    for i in range(k,-1,-1):
        
        if i-w >= 0:
            
            dp[i] = max(dp[i],dp[i-w] + v)

print(dp[k])