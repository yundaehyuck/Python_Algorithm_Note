#두 문자열 s1,s2에 대하여 s1을 s2로 바꾸는데 필요한 최소 연산 횟수
#가능한 연산은 다음 3가지
#1. 임의의 위치에 아무 문자나 하나 삽입
#2. 임의의 위치에 있는 문자를 하나 삭제
#3. 임의의 위치에 있는 문자를 하나 아무거나 교체
def edit_distance(s1,s2):
    
    m,n = len(s1),len(s2)

    INF = 10**9

    #dp[i][j] = s1[:i+1], s2[:j+1]의 최소 편집거리
    dp = [[INF]*(n+1) for _ in range(m+1)] 

    #dp[i][0] = s1[:i+1]을 ''으로 만드는데 드는 최소 편집거리는 s1[:i+1]의 길이인 i번 삭제하면 됨
    for i in range(m+1):
        
        dp[i][0] = i
    
    #dp[0][j] = ''을 s2[:j+1]로 만드는데 드는 최소 편집거리는 s2[:j+1]의 길이인 j번 추가하면 됨
    for j in range(n+1):
        
        dp[0][j] = j
    
    for i in range(1,m+1):
        
        for j in range(1,n+1):
            
            if s1[i-1] == s2[j-1]: #마지막 문자 i-1번, j-1번이 서로 같다면, 나머지 s1[:i], s2[:j]를 비교하면 된다
                
                dp[i][j] = dp[i-1][j-1]
            
            else: #일치하지 않는다면 3가지 연산중 하나를 수행
                #s1[i-1]을 삭제한다면, s1[:i]와 s2[:j+1]을 비교하면 되므로 dp[i-1][j]
                #s1[i-1]을 s2[j-1]로 바꾼다면, s1[:i]와 s2[:j]를 비교하면 되므로 dp[i-1][j-1]
                #s2[j-1]을 s1의 끝에 삽입한다면, s1[:i+1]과 s2[:j]를 비교하면 되므로, dp[i][j-1]
                
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
    
    return dp[m][n]

s1 = input()
s2 = input()

print(edit_distance(s1,s2))