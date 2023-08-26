#naive polynomial multiplication
def multiply(a,b,mod):

    result = [0]*(len(a)+len(b)-1)

    for i in range(len(a)):
        
        for j in range(len(b)):
            
            result[i+j] += (a[i]*b[j]) % mod
    
    return result

#negative mod

def negative_mod(x,mod):
    
    if x < 0:
        
        return (x+mod)%mod
    
    else:
        
        return x%mod
    
#naive polynomial division
#a/b
def divide(a,b,mod):
    
    q = [0]*(len(a)-len(b)+1) #몫

    #최고차항부터 순회해서..
    for i in range(len(q)-1,-1,-1):
        
        q[i] = a[i+len(b)-1]//b[-1]

        for j in range(len(b)-1,-1,-1):

            a[i+j] -= (q[i]*b[j])
            a[i+j] = negative_mod(a[i+j],mod)
    
    while a:
        
        x = a.pop()

        if x != 0:

            a.append(x)
            break

    return a

def kitamasa(w,a,n,mod):
    
    c = [1] #a_n = sum(w[i]a_n-i) = sum(c[i]a[i])
    x = [0,1] #x^1, x^2, x^4, ...
    
    #w를 이용해 f(x) = x^k - w1x^k-1 - w2x^k-2 - ...을 구한다.
    f = [negative_mod(-i,mod) for i in w]
    f.append(1)
    
    #분할정복을 이용한 거듭제곱으로 x^n mod f를 구한다.
    #합동식의 성질 a*b mod p = (a mod p * b mod p) mod p를 이용
    while n:
        
        if n & 1:
            
            c = divide(multiply(c,x,mod),f,mod)
            
        n >>= 1

        x = divide(multiply(x,x,mod),f,mod)
    
    #c배열을 찾았다면, an의 값을 구한다.
    #find a_n = sum(c[i]a[i])
    answer = 0

    for i in range(len(a)):

        answer += (a[i]*c[i])
        answer = negative_mod(answer,mod)

    return answer