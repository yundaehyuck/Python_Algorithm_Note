#https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    
    answer = 0
    
    for n in range(left,right+1):
        
        #변수에 원본 n을 복사
       
        number = n
        
        #n에 대한 소인수분해
        p = 2
        
        divisor = 1
        
        while p*p <= n:
            
            count = 0
            
            if n % p == 0:
                
                while n % p == 0:
                    
                    n = n // p
                    
                    count += 1
                
                #p의 지수+1을 divisor에 누적 곱
                divisor *= (count+1)
            
            p = p + 1
        
        if n > 1:
            
            #n>1이면 n도 소인수이므로, 2를 곱해준다
            divisor *= 2
        
        #약수의 개수가 짝수이면 더해주고, 아니면 빼주고
        if divisor % 2 == 0:
            
            answer += number
        
        else:
            
            answer -= number
    
    return answer


#제곱수의 약수의 개수는 홀수개이고, 
#제곱수가 아닌 수의 약수의 개수는 짝수개
def solution(left, right):
    
    answer = 0
    
    for n in range(left,right+1):
        
        #n이 제곱수라면, (1/2)제곱을 하더라도, 정수이므로
        if int(n**(1/2)) == n**(1/2):
            
            answer -= n
        
        else:

            answer += n
    
    return answer