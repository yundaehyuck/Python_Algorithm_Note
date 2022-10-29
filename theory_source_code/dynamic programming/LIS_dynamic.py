#다이나믹 프로그래밍으로 최장증가 부분수열 찾기

s = [3,2,6,4,5,1]

n = len(s)

dp = [0]*(n+1)

for i in range(1,n): ##1번부터 n-1번까지
    
    dp[i] = 1 ##최초 1로 시작

    for j in range(1,i): ##인덱스 i이전의 j에 대하여
    
    ##a_i보다 작은 a_j를 찾는다

        if s[j] < s[i]:
            
            ##그러면, dp[i]는 1+dp[j]중 최댓값

            if dp[i] < 1+dp[j]:
                
                dp[i] = 1+dp[j]
    
print(max(dp)) ##dp테이블에서 최댓값이 전체 수열에서 가장 긴 증가 부분수열의 길이

"""
3
"""