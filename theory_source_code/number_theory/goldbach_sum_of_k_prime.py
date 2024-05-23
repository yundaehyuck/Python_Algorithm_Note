#정수 n을 k개의 소수 합으로 표현하는 방법
def is_prime(n):
    
    for i in range(2,int(n**(1/2))+1):
        
        if n % i == 0:
            
            return False
    
    return True

def represent_two_prime(n):
    
    for i in range(2,n+1):
        
        if is_prime(i) and is_prime(n-i):
            
            return i

n,k = map(int,input().split())

#가장 작은 소수는 2이므로, k개의 소수로 만들 수 있는 가장 작은 정수는 2k
if n < 2*k:
    
    print(-1)

else:
    
    #n을 1개의 소수로 만들 수 있는가?
    #n 자체가 소수인지 아닌지 판단
    if k == 1:
        
        if is_prime(n):
            
            print(n)
        
        else:
            
            print(-1)
    
    #2개의 소수로 만들 수 있는가?
    elif k == 2:
        
        #n이 짝수이면 2보다 큰 모든 짝수는 2개의 소수 합으로 분해할 수 있다
        if n % 2 == 0:
            
            a = represent_two_prime(n)
            print(a,n-a) #아무거나 빠르게 하나를 찾는다
        
        else:
            
            #n이 홀수라면, 짝수 + 홀수 = 홀수이고 소수중 2만이 유일하게 짝수이므로
            #2를 반드시 사용해야하고, 나머지 n-2가 소수인지 아닌지 판단
            if is_prime(n-2):
                
                print(2,n-2)
            
            else:
                
                print(-1)
        
    else: #n을 3개 이상의 소수로 만들 수 있는가?
        
        if n % 2 == 0:
            
            #n이 짝수이면 n - 2(k-2)도 짝수이다.
            #따라서 2를 k-2번 사용하고, 나머지 2개는 n-2(k-2)를 2개의 소수 합으로 분해
            for _ in range(k-2):
                
                print(2,end=' ')
            
            a = represent_two_prime(n-2*(k-2))
            print(a,end=' ')
            print(n-2*(k-2)-a,end=' ')
        
        else:
            
            #n이 홀수이면 n-3-2(k-3)도 짝수이다.
            #따라서 2를 k-3번 사용, 3을 1번 사용, 나머지 2개는 n-3-2(k-3)을 2개의 소수 합으로 분해
            for _ in range(k-3):
                
                print(2,end=' ')
            
            print(3,end=' ')
            a = represent_two_prime(n-3-2*(k-3))
            print(a,end=' ')
            print(n-3-2*(k-3)-a,end=' ')