#유클리드 호제법
def gcd(a,b):
    
    while b != 0:
        
        a,b = b, a%b
    
    return a

#오일러의 phi

def phi(n):
    
    #1과는 어차피 서로소이므로 최솟값은 1
    result = 1
    
    for i in range(2,n):
        
        if gcd(i,n) == 1: #2부터 n-1까지 n과의 최대공약수가 1이면
            
            result += 1
    
    return result