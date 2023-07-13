#1/x + 1/y = 1/(n!)의 정수(x,y)해
#n!^2 = pq이면, x = p + n, y = q + n이 일반해
def get_prime(n):
    
    result = [1]*(n+1)

    for i in range(2,int((n**(1/2))+1)):
        
        if result[i] == 1:
            
            for j in range(i*i,n+1,i):
                
                result[j] = 0
    
    return [i for i in range(2,n+1) if result[i] == 1]

n = int(input())

answer = 1

#n이하의 모든 소수를 찾고,
primes = get_prime(n)

#n!이 가지는 p의 지수를 찾는다.
#이를 이용해 n!^2이 가지는 p의 지수를 찾고, 지수+1을 누적곱하여 약수의 개수를 구한다
for p in primes:
    
    k = p
    count = 0

    while n//k != 0:
        
        count += n//k

        k *= p
    
    count *= 2
    answer *= (count+1)

print(answer)