mod = 10**9+7

m = int(input())

factorial = [0]*(2*m+1)

factorial[0] = 1

for i in range(1,2*m+1):
    
    factorial[i] = factorial[i-1] * i
    factorial[i] %= mod

answer = 0

#sum(mCk*nCr-k) = m+nCr 
#sum(nCr^2) = 2nCn
for n in range(3,m+1):
    
    answer += factorial[2*n]*pow(factorial[n]*factorial[n], mod-2, mod)

    answer %= mod

print(answer)