#한번 담은 물건을 또 담을 수 있는 배낭문제
#무게 제한이 h이상인 경우

from sys import stdin

n,h = map(int,stdin.readline().split())

bag = []

for _ in range(n):
    
    p,c = map(int,stdin.readline().split())
    bag.append((p,c))

INF = 2500000000
dp = [INF]*(h+1)
dp[0] = 0

for w,c in bag:
    
    for i in range(h+1): #무게를 순방향 i = 0,1,2,..,h으로 순회하면 이미 담은 물건을 또 담을 수 있다

        if i + w <= h:
            
            dp[i+w] = min(dp[i+w],dp[i] + c)
        
        else:
            #최소 h 이상을 담을 수 있으므로
            #현재 무게 i + 담은 물건 무게 w > h이면, h로 하면 된다
            dp[h] = min(dp[h], dp[i] + c)

print(dp[h])