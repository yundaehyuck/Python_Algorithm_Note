#주어진 대문자 알파벳들 개수로 만들 수 있는 길이 1 이상 k이하 모든 문자열의 개수
#각 알파벳들을 일렬로 배열하는 복수순열의 수 
def factorial(n):
    
    f = [0]*(n+1)

    f[0] = 1

    for i in range(1,n+1):
        
        f[i] = f[i-1] * i
        f[i] %= mod
    
    return f

def inverse(n,f):
    
    i = [0]*(n+1)

    i[n] = pow(f[n],mod-2,mod)

    for j in range(n-1,-1,-1):
        
        i[j] = i[j+1] * (j+1)
        i[j] %= mod
    
    return i

def multiply(a,b,k,mod):
    
    result = [0]*(k+1)

    for i in range(len(a)):
        
        for j in range(len(b)):
            
            if i+j > k:
                
                break
            
            result[i+j] += (a[i]*b[j])%mod
    
    return result

mod = 998244353

k = int(input())

C = list(map(int,input().split()))

f = factorial(1000)

inv = inverse(1000,f)

#26개 다항식을 곱한 결과
A = [0]*(k+1)
A[0] = 1

for i in range(26):
    
    #inverse factorial을 계수로 가지는 다항식 1개를 생성
    g = [0]*(C[i]+1)

    for j in range(C[i]+1):
        
        g[j] = inv[j]
    
    #A와 g의 곱을 A로 두고...
    A = multiply(A,g,k,mod)

answer = 0

#A에는 26개 다항식의 곱의 K차항 계수까지 구해져있다

#1차부터 K차항 계수까지, 각 계수에 길이 i의 factorial값을 곱한 값을 다 더하면...
for i in range(1,k+1):
    
    answer += A[i]*f[i]
    answer %= mod

print(answer)