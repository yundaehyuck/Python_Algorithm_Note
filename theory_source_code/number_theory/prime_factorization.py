from sys import stdin

n = int(stdin.readline())

p = 2

#최대로 나누어 떨어지는 정수는 n**(1/2)
while p*p <= n:
    
    if n % p == 0:
        
        n = n//p
        print(p) #n이 p로 나누어 떨어지면, p는 소인수
    
    else:
        
        p += 1

#반복문 탈출 후에, n > 1이면.. n은 소인수
if n > 1:
    
    print(n)