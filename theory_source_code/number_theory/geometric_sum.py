#기하급수의 합

#r은 공비, n은 마지막 항의 지수(항 수-1), mod는 나머지 연산
def geometric(r,n,mod):
    
    if n == 0:
        
        return 1
    
    else:
        
        #n이 홀수
        #g(r,n) = (1+r)g(r**2,(n-1)/2)
        
        if n % 2 == 1:
            
            return ((1+r)%mod*geometric(r*r%mod, (n-1)//2, mod))%mod
        
        #n이 짝수
        #g(r,n) = 1+(r+r**2)g(r**2,(n-2)/2)
        
        else:
            
            return 1 + ((r+r*r)%mod*geometric(r*r%mod, (n-2)//2, mod))%mod