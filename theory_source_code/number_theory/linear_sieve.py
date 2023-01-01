#linear sieve & spf

def linear_sieve(n):
    
    sieve = [1]*(n+1)
    prime = []
    spf = [0]*(n+1)
    
    #2부터 n까지 소수인지 검사
    for i in range(2,n+1):
        
        #i가 소수이면
        if sieve[i] == 1:
            
            #소수 리스트에 넣고
            prime.append(i)
            
            #당연히 소수 i의 최소소인수는 i이다.
            spf[i] = i
        
        #소수 리스트에 있는 j에 대하여..
        #ij는 합성수이고, 이것을 지운다.
        #지우면서 ij가 n보다 커지거나 
        #i가 j의 배수이면 그 다음의 소수는 ij의 최소소인수가 아니므로 멈춘다.
        for j in prime:
            
            if i * j > n:
                
                break
                
            sieve[i*j] = 0
            
            #i*j의 최소소인수는 j이다.
            spf[i*j] = j
            
            if i % j == 0:
                
                break
    
    return prime,spf