#job assignment problem
#비트마스킹을 이용한 다이나믹 프로그래밍
from sys import stdin

n = int(stdin.readline())

cost = [list(map(int,stdin.readline().split())) for _ in range(n)]

INF = 1000000000000000000
dp = [INF]*(1 << n)
dp[0] = 0

#0~n-1 비트열에서 i번째 비트는 i번째 사람이 일을 배정받았냐 아니냐
#길이 n인 비트열은 0~에서 2^n-1까지
for p in range(1 << n):
    
    #0에서 x-1번까지 사람이 직업을 배정받았다
    x = p.bit_count() #비트열 p에서 1인 개수
    
    #이제 x번 사람의 직업을 배정할 차례
    #0~n-1번 비트중 안켜진 비트를 찾는다
    for i in range(n):
        
        #1 << i는 i번째 비트만 키고 나머지는 끄고
        #p와 1 << i의 &연산이 0이면 p의 i번째 비트는 꺼져있다
        if p & (1 << i) == 0:
            
            #p의 i번째 비트가 꺼져있으면 x번 사람을 i번째 직업에 배정해본다
            dp[p | (1 << i)] = min(dp[p | (1 << i)], dp[p] + cost[x][i])

#모든 경우를 검사하고 모든 직업을 배정한 1111...111에 구하고자 하는 최솟값이 저장되어있다 
print(dp[2**n-1])