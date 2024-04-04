#정수 n의 어떤 수 p 모듈로 곱셈에 대한 역원
n = int(input())

mod = 10**9+7 #매우 큰 소수

inverse = [0]*(n+2)
inverse[1] = 1

#p = (p//n)*n + p%n (p를 n으로 나눈 몫과 n으로 나눈 나머지를 이용한 표현)
#0 = (p//n)*n + p%n mod p(양변을 mod p 연산)
#-(p//n)n = p%n (mod p)
#(-(p//n)n)^-1 = (p%n)^-1 (mod p)
#n^-1 mod p = (-p//n) * (p%n)^-1 mod p(양변에 -p//n을 곱함)
for i in range(1,n+1):
    
    #n^-1 mod p = -p//n * (p%n)^-1 mod p
    inverse[i+1] = -(mod//(i+1)) * inverse[mod % (i+1)]
    inverse[i+1] %= mod