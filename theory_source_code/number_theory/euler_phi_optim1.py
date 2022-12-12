#소인수분해를 이용한 오일러 phi

def phi(n):
    
    #소인수 p1,p2,...,pr에 대하여,
    #n에 1-(1/p1), (1-(1/p2),..를 곱해나갈것이다.
    
    result = n 
    
    p = 2
    
    #소인수분해 시작
    while p*p <= n:
        
        #n이 p로 나누어 떨어진다면.. p는 n의 소인수
        
        if n % p == 0:
            
            #n을 p로 나눈 몫으로 갱신하는데,
            #어차피 다음에도 n이 p로 나누어지는지 검사할거니까,
            #n이 p로 나누어 떨어지지 않을때까지 계속 반복해준다.
            
            while n % p == 0:
                
                n = n//p #n이 p로 나누어 떨어지면, n을 p로 나눈 몫으로 갱신
            
            #p는 n의 소인수이므로
            result = result * (1.0 - (1.0/float(p)))
        
        p = p + 1
    
    
    #여기서 n이 1보다 크면 n은 소수이다.
    
    if n > 1:
        
        result = n - 1 #오일러 phi의 정의에 따라..
    
    return int(result)