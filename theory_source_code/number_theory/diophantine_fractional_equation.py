#1/x + 1/y = 1/n의 정수해 (x,y)의 개수 (x<=y)
#n^2 = pq, x = p + n, y = q + n이 일반해

from sys import stdin

T = int(stdin.readline())

for i in range(1,T+1):
    
    n = int(stdin.readline())

    p = 2

    answer = 1
    
    #n에 대한 소인수분해로 n^2의 약수의 개수를 구해준다
    while p*p <= n:
        
        count = 0

        while n % p == 0:
            
            count += 1
            n//= p
        
        #n에서 소수 p에 대한 지수가 count
        #n^2에서 소수 p에 대한 지수는 2count
        #2count+1을 누적곱해준다
        count *= 2
        answer *= (count+1)
        p += 1
    
    if n > 1:
        
        answer *= 3
    
    #제곱수 n^2의 약수의 개수는 홀수개 = 2k+1
    #x <= y인 (x,y)를 구해야하므로, 2k개끼리는 서로 짝지어주어서 k개
    #나머지 1개인 p = n, q = n을 더해주면 k+1개가 정답
    answer //= 2
    answer += 1
        
    print(f'Scenario #{i}:')
    print(answer)
    print()