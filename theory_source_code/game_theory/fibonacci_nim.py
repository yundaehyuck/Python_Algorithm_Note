from sys import stdin

#완전제곱수인지 판단
def is_perfect(n):
    
    if int((n**(1/2)))**2 == n:
        
        return True
    
    return False

#피보나치 수인지 판단
def is_fib(n):
    
    x = 5*n*n+4
    y = 5*n*n-4

    if is_perfect(x) or is_perfect(y):
        
        return True
    
    return False

#제켄도르프 분해해서 가장 작은 피보나치 수를 구함
def z(n):
    
    fib = [1,1]

    i = 2

    while 1:
        
        x = fib[i-1] + fib[i-2]

        if x <= n:

            fib.append(x)
            i += 1
        
        else:
            
            break
    
    len_f = len(fib)

    while n > 0:
        
        for i in range(len_f-1,-1,-1):
            
            if n >= fib[i]:
                
                n -= fib[i]
                break
    
    return fib[i]


n = int(stdin.readline())

#피보나치 수이면, 이길 수 없고
if is_fib(n):
    
    print(-1)

#피보나치 수가 아니라면, 제켄도르프 분해해서 나타나는 가장 작은 피보나치 수를 집는다
else:

    print(z(n))