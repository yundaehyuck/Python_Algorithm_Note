from sys import stdin

#dp[s][k][n]을 최댓값이 n이고 k개의 서로 다른 정수를 사용하여 합이 s가 되는 방법의 수
dp = [[[0]*21 for _ in range(11)] for _ in range(156)]

#0개의 서로 다른 정수로 0을 만드는 방법은 아무것도 안하면 되니까 1로 초기화
for i in range(21):

    dp[0][0][i] = 1

#최댓값이 n = 1,2,...,20까지 모든 경우 각각에 대하여...
#k-1개의 서로 다른 정수를 사용해서 합이 s-i가 되는 경우의 수 dp[s-i][k-1][n] 각각에 i만 더해주면 된다
for n in range(1,21):
    
    for i in range(1,n+1):
        
        #k를 역으로 순회해서 동일한 정수를 사용하는 경우를 피한다
        for k in range(10,0,-1):

            for s in range(1,156):
                
                if s >= i:

                    dp[s][k][n] += dp[s-i][k-1][n]

while 1:
    
    n,k,s = map(int,stdin.readline().split())

    if n == 0 and k == 0 and s == 0:
        
        break
    
    else:
        
        print(dp[s][k][n])