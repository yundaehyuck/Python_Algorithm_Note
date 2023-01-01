#smallest prime factor
def get_spf(n):
    
    #각 수의 SPF는 i가 되도록 초기화
    spf = [i for i in range(n+1)]
    
    #모든 짝수는 2를 소인수로 가진다.
    
    for i in range(4,n+1,2):
        
        spf[i] = 2
    
    #3부터 n**(1/2)까지 SPF를 계산
    
    for i in range(3,int((n+1)**(1/2))+1):
        
        #i의 가장 작은 소인수가 i라는 것은
        #i가 소수이고..
        if spf[i] == i:
            
            #i를 제외한 i의 배수는 i로 나누어 떨어지고
            for j in range(i*i,n+1,i):
                
                #아직 j의 spf가 계산되지 않았다면..
             
                if spf[j] == j:
                    
                    #i의 배수인 j는 spf가 i이다.
                    spf[j] = i
    
    return spf
    
#spf를 이용한 소인수분해

def get_factorization(x,spf):
    
    factor = []
    
    while x != 1:
        
        #x의 가장 작은 소인수가 spf[x]에 들어가 있음
        factor.append(spf[x])
        
        #x를 x의 가장 작은 소인수로 나눠서, 다음 x에 저장
        x = x//spf[x]
    
    return factor