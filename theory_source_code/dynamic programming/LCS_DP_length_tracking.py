#실제 LCS를 역추적하여 구하는 함수
def get_lcs(dp,n,m,X):
    
    i = n
    j = m

    lcs = [0]*(dp[i][j]) #LCS의 길이는 dp[n][m]이므로.. 배열을 초기화

    k = 1
    
    #i = 0, j = 0에 도달할때까지 (n,m)부터 역으로 이동
    while i != 0 or j != 0:
        
        #j가 1이상이고, dp[i][j] == dp[i][j-1]이면, j > j-1로 이동
        #j가 1이상이어야 j > j-1로 이동할 수 있기 때문...
        if j >= 1 and dp[i][j] == dp[i][j-1]:
            
            j -= 1
        
        #dp[i][j] != dp[i][j-1]일때, dp[i][j] == dp[i-1][j]이면, i > i-1로 이동
        elif dp[i][j] == dp[i-1][j]:
            
            i -= 1
        
        #dp[i][j] != dp[i][j-1]이고 dp[i][j] != dp[i-1][j]이면...
        #해당 위치 i는 lcs의 문자에 포함된다.
        else:
            
            #어차피 역으로 문자열을 읽어야하므로, 배열에 미리 뒤에서부터 집어넣는다.
            #인덱스가 one - based이므로... X[i]가 아니라 X[i-1]을 집어넣어야...
            lcs[-k] = X[i-1]
            i -= 1
            j -= 1
            k += 1
    
    return ''.join(lcs)
    
X = input()
Y = input()

n = len(X)
m = len(Y)

#LCS의 길이를 구하는 과정
#DP[i][j]는 X[1,2,...,i]와 Y[1,2,..,j]의 가장 긴 공통 부분문자열의 길이
dp = [[0]*(m+1) for _ in range(n+1)]


#X[i] == Y[j]이면, X[1,2,..,i-1]과 Y[1,2,..,j-1]의 가장 긴 공통 부분문자열의 길이에 X[i] 하나를 더해준다
#X[i] != Y[j]이면, X[1,2,..,i]와 Y[1,2,..,j-1]의 가장 긴 공통 부분문자열의 길이와
#X[1,2,..,i-1]과 Y[1,2,..,j]의 가장 긴 공통 부분문자열의 길이 중 더 큰 값이 된다
for i in range(1,n+1):
    
    for j in range(1,m+1):
        
        if X[i-1] == Y[j-1]:
            
            dp[i][j] = dp[i-1][j-1] + 1

        else:
            
            dp[i][j] = max(dp[i][j-1],dp[i-1][j]) #조건문으로 풀어쓰면 조금 더 빠르긴함..

answer = dp[n][m] #LCS의 길이

if answer == 0:
    
    print(answer)

else:
    print(answer)
    print(get_lcs(dp,n,m,X))