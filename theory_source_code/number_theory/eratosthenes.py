 #n까지 숫자 중에서 소수를 구하는 방법

def get_prime(n):

    #0~n까지가 모두 소수라고 표시한 초기화된 형태
    
    steve = [True] * (n+1)
    
    for i in range(2,int((n+1)**(1/2))+1): #제곱근깞까지 검사를 해야함 그래서 +1해줘야

        #i번째 수가 소수라면,
        
        if steve[i]:
            
            #step size가 i라면 i의 배수씩 검사하게 되는거
            #i를 제외한 i의 배수를 모두 제거

            for j in range(i+1,n+1,i):
                
                steve[j] = False
    
    #2부터 n까지 True인 수를 모두 리스트에 담아 return
    return [i for i in range(2,n+1) if steve[i] == True]