#무게가 실수인 무한 배낭 문제
#무게는 소수점 둘째자리까지만 주어짐
from sys import stdin

while 1:

    n,m = stdin.readline().rstrip().split()

    n = int(n)
    
    #무게에 100을 곱해서 모두 정수로 바꾼다
    #그냥 100을 곱하면 부동소수점 오차가 나기 때문에
    #.을 기준으로 split해서 두 원소를 합치고 int로 바꾼다
    temp = m.split('.')
    m = temp[0] + temp[1]
    m = int(m)

    if n == 0 and m == 0:
        
        break

    candy = []

    for _ in range(n):
        
        c,p = stdin.readline().rstrip().split()
        c = int(c)
        temp = p.split('.')
        p = temp[0] + temp[1]
        p = int(p)

        candy.append((c,p))
    
    dp = [0]*(m+1)

    for c,p in candy:
        
        for i in range(p,m+1): #중복해서 담을 수 있는 무한 배낭 문제라서 정방향 순회
            
            dp[i] = max(dp[i],dp[i-p] + c)
    
    print(dp[m])