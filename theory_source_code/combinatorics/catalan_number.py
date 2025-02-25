#원 위의 2n개의 점이 서로 교차하지 않도록 선분을 긋는 방법의 수
#카탈란 수 Cn = sum(c(k)c(n-1-k)) = 2nCn/n+1과 같다
n = int(input())//2

c = [0]*(n+1)
c[0] = 1

mod = 987654321

for i in range(1,n+1):
    
    for k in range(i):
        
        c[i] += c[k]*c[i-1-k]
        c[i] %= mod
        
print(c[n] % mod)

"""
n = int(input())

f = [0]*(n+1)
f[0] = 1

for i in range(1,n+1):
    
    f[i] = f[i-1] * i

mod = 987654321

print(f[n]//(f[n//2]*f[n//2]*(n//2+1)) % mod)"""