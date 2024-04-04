#팩토리얼의 소수 mod 모듈로 곱셈에 대한 역원
n = int(input())

mod = 10**9+7 #매우 큰 소수

#n! mod p를 모두 구해놓는다
factorial = [0]*(n+1)
factorial[0] = 1

for i in range(1,n+1):
    
    #n! mod p
    factorial[i] = factorial[i-1]*i
    factorial[i] %= mod #매 곱셈마다 mod로 나눈 나머지를 저장해야 연산이 빨라짐

#페르마의 소정리에 의해 n!^-1 mod p = (n!)^p-2
factorial_inverse = [0]*(n+1)
factorial_inverse[n] = pow(factorial[n], mod-2, mod)

#n!*(n!)^p-2 = (n-1)!*(n*(n!)^p-2) mod p이므로
#(n-1)!^-1 mod p = n!^-1 mod p * n
for i in range(n,0,-1):

    factorial_inverse[i-1] = factorial_inverse[i] * i
    factorial_inverse[i-1] %= mod
    
print(factorial[n])