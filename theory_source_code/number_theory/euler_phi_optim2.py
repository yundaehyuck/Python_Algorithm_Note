#소인수분해를 이용한 개선된 오일러 phi함수

def phi(n):
    
    #result = n으로 초기화
    
    result = n 
    
    #n에 대한 소인수분해 시작
    #p=2부터 시작
    
    p = 2
    
    #p*p <= n일때, 소인수분해 반복문을 수행
    
    while p*p <= n:
        
        #만약 n이 p로 나누어 떨어진다면?
        #p는 n의 소인수이다.
        
        if n % p == 0:
            
            #n이 p로 나누어 떨어진다면
            #n을 p로 나눈 몫으로 n을 갱신하는 과정을 반복
            
            while n % p == 0:
                
                n = n//p
            
            #반복문을 탈출하면, p는 n의 소인수이고
            #다음 소인수를 찾을 차례인데, 그 전에 result값을 갱신
            
            #result에서 result를 p로 나눈 몫을 빼준다.
            
            #아래 둘은 동일한 식
            
            result -= result//p
            #result = result // p * (p - 1)
        
        #n이 p로 나누어 떨어지지 않으면
        #p에 1 증가
        p = p + 1
    
    #반복문 밖에서 n이 1보다 크다면, n은 그 자체로 소수이다.
    if n > 1:
        
        #소수의 오일러 phi값
        result = n - 1
    
    return result