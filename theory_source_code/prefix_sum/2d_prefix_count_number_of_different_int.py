#(X1,Y1), (X2,Y2) 직사각형 내부에 서로다른 정수의 개수
from sys import stdin

n = int(stdin.readline())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

#dp[y][x][i] = (0,0),(x,y)에서 정수 i의 개수
dp = [[[0]*11 for _ in range(n)] for _ in range(n)]

dp[0][0][maps[0][0]] = 1

for x in range(1,n):      
    
    dp[0][x][maps[0][x]] += 1
    
    for i in range(1,11):

        dp[0][x][i] += dp[0][x-1][i]
        
for y in range(1,n):
    
    dp[y][0][maps[y][0]] += 1
    
    for i in range(1,11):
        
        dp[y][0][i] += dp[y-1][0][i]
            
for y in range(1,n):

    for x in range(1,n):
        
        dp[y][x][maps[y][x]] += 1
        
        for i in range(1,11):
            
            dp[y][x][i] += (dp[y-1][x][i] + dp[y][x-1][i] - dp[y-1][x-1][i])
            
q = int(stdin.readline())

#(x1,y1),(x2,y2)가 주어질때, 모든 정수 i = 1,2,..,10에 대하여 
#(x1,y1),(x2,y2) 내부의 정수 i의 개수를 찾는다
#i의 개수가 1 이상이면 해당 정수가 존재하므로 1을 더해주고
#없으면 0을 더해주고
for _ in range(q):
    
    y1,x1,y2,x2 = map(int,stdin.readline().split())

    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    count = 0

    for i in range(1,11):
        
        A = dp[y2][x2][i]

        if y1 == 0:
            
            B = 0
        
        else:

            B = dp[y1-1][x2][i]

        if x1 == 0:
            
            C = 0
        
        else:

            C = dp[y2][x1-1][i]
        
        if x1 == 0 or y1 == 0:

            D = 0

        else:

            D = dp[y1-1][x1-1][i]
        
        count += min((A - B - C + D),1)
    
    print(count)