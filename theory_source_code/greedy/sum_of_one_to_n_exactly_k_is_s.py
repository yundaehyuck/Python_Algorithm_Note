#1부터 n중에서 정확히 k개를 사용해 더해서 s를 만드는 방법

from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    
    n,s,k = map(int,stdin.readline().split())
    
    #1부터 k까지 합 = (k*(k+1)//2)
    #n-k+1,n-k+2,...,n까지 합 = (1부터 n까지 합) - (1부터 n-k까지 합)
    #만약 s가 (k*(k+1)//2)보다 작거나, (n*(n+1)//2) - ((n-k)*(n-k+1)//2)보다 크면 불가능하다.
    if s < (k*(k+1)//2) or s > (n*(n+1)//2) - ((n-k)*(n-k+1)//2):
        
        print('NO')
    
    else: #범위 내라면 확실하게 만들 수 있다.

        answer = ['0']*n

        while k > 0:
            
            #가장 작은 가격 1~k-1까지 선택했다고 한다면, 나머지 하나는
            a = s - ((k-1)*k//2)
            
            #a가 n보다 큰 경우가 있을 수 있다.
            if n < a:

                #그런 경우에는 n을 사용하고
                answer[n-1] = '1'

                s -= n #n을 썼으니까
                k -= 1 #1개 썼으니까
                n -= 1 #n을 썼으니까 n은 사용 불가하고 1 감소시켜서 제한을 갱신
            
            else:
                
                #a가 n보다 작다면 a를 선택하고
                answer[a-1] = '1'
                
                #그 다음은 1부터 k-1까지로 채우면 된다.
                for i in range(1,k):
                    
                    answer[i-1] = '1'
                
                break

        print('YES')
        print(''.join(answer))