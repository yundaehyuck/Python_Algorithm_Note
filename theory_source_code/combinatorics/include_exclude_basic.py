from sys import stdin

T = int(stdin.readline())

for t in range(T):
    
    a,b,n = map(int,stdin.readline().split())
        
    p = 2

    answer1 = 0 #1 ~ B 이하에서 N과 서로소가 아닌 수들의 개수
    answer2 = 0 #1 ~ A-1 이하에서 N과 서로소가 아닌 수들의 개수
    
    #N의 모든 소인수를 찾는다
    prime = []

    while p*p <= n:
        
        count = 0

        while n % p == 0:
            
            n//=p
            count += 1
        
        if count >= 1:
            
            prime.append(p)
        
        p += 1
    
    if n > 1:
        
        prime.append(n)
    
    #N의 소인수들의 집합에 대한 모든 부분집합을 찾는다
    p = len(prime)

    for i in range(1<<p):
        
        partial = []

        x = 0

        for j in range(p):
            
            if i & (1 << j):
                
                partial.append(prime[j])
                x += 1
        
        #포함과 배제의 원리
        
        #공집합은 제외하고,
        if x == 0:
            
            continue
        
        #부분집합의 크기가 짝수이면,
        if x % 2 == 0:
            
            #원소들의 곱을 빼준다
            y = 1

            for k in partial:
                
                y *= k

            answer1 -= b//y
            answer2 -= (a-1)//y
        
        #부분집합의 크기가 홀수이면
        else:
            
            #원소들의 곱을 더해준다
            y = 1

            for k in partial:
                
                y*= k
            
            answer1 += b//y
            answer2 += (a-1)//y
    
    #[A이상 B이하에서 N과 서로소인 수들의 개수]
    # = [A이상 B이하의 개수] - [B 이하에서 N과 서로소가 아닌 수들의 개수] - [A-1이하에서 N과 서로소가 아닌 수들의 개수]
    print(f'Case #{t+1}: {b - a + 1 - answer1 + answer2}')