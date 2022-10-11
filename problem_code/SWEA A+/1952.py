#다이나믹 프로그래밍
T = int(input())

for tc in range(1,T+1):
    
    d,m,q,y = map(int,input().split())  #1일,1달,3달,1년

    year_list = [0] + list(map(int,input().split())) ##1년 이용계획 0~11에 인덱스를 위해 [0]을 추가

    dp = [0]*13 ##dp[i]: i달까지 사용된 최소 요금 비용

    for i in range(1,13):
        
        ##2월까지 최소비용
        ##이전 월의 최소비용+1일요금*이용일과 이전 월의 최소비용+1달비용중 최솟값
        if i <= 2:
            
            dp[i] = min(dp[i-1]+d*year_list[i],dp[i-1]+m)
        
        ##3월부터는 3개월 이용권을 구입 가능
        ##이전 월까지의 최소 비용+1일요금*이용일과 이전 월의 최소비용+1달비용과 3개월전의 최소비용+3달비용중 최솟값
        elif i <= 11:
            
            dp[i] = min(dp[i-1]+d*year_list[i],dp[i-1]+m,dp[i-3]+q)
        
        
        ##마지막해에는 1년 이용권을 구입 가능
        
        ##이전 월까지의 최소 비용+1일요금*이용일과 이전 월의 최소비용+1달비용과 3개월전의 최소비용+3달비용과 1년전 최소비용+1년비용중 최솟값
        else:
            
            dp[i] = min(dp[i-1]+d*year_list[i], dp[i-1]+m, dp[i-3]+q, dp[i-12]+y)

    
    print('#'+str(tc),dp[12])