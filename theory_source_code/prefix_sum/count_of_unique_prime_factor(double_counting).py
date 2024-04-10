#정수 n의 유일한 소인수의 개수
#에라토스테네스의 체의 변형
def get_prime(n):
    
    result = [0]*(n+1)

    #2부터 n까지 정수 i에 대하여...
    for i in range(2,n+1):
        
        if result[i] == 0: #현재 i에 표시되어 있지 않다면 i는 소수이고
            
            #i이상 i의 배수는 i를 소인수로 가진다.
            for j in range(i,n+1,i):
                
                result[j] += 1
    
    return result