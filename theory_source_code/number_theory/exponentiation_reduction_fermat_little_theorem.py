from sys import stdin

n,p = map(int,stdin.readline().split())

A = list(map(int,stdin.readline().split()))

A_dict = {}

f1 = 0

#페르마의 소정리에 의해, k^n mod p = k^(n%p) mod p
#차수가 같은 항끼리 묶어서 계수를 미리 계산해 N+1 > p-1개의 항으로 압축
for i in range(n+1):
    
    A[i] %= p

    f1 += A[i]

    r = (n-i) % (p-1)

    A_dict[r] = A_dict.get(r,0) + A[i]
    A_dict[r] %= p

print(A[-1]) #f(0) mod p
print(f1 % p) #f(1) mod p

#i = 2,3,...,p-1에 대해 f(i) mod p를 계산
#A_dict에 차수가 k=0,1,2,..p-1인 항의 계수 v가 계산되어있다
#k 차수 항은 v*i^k mod p로 계산 가능
#분할정복을 이용한 거듭제곱으로 빠르게
for i in range(2,p):

    answer = 0

    for k,v in A_dict.items():
        
        answer += pow(i,k,p)*v
        answer %= p
    
    print(answer)