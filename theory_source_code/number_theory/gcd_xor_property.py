from sys import stdin

#gcd(a,b) = xor(a,b) <> gcd(a,b) = a-b = xor(a,b) 

T = int(stdin.readline())

for _ in range(T):

    n = int(stdin.readline())

    max_g = 1000000
    
    A = [0]*(max_g+1)

    for i in map(int,stdin.readline().split()):
        
        A[i] += 1

    count = 0

    #o(n^2) > o(nlogn)

    #A에서 i,j를 잡아 A[i],A[j]를 찾지 말고
    #g의 배수 gx, g(x+1)를 찾는다.
    #연속하는 두 자연수 x,x+1은 서로소이다.

    #g > 1~max_g, x > 1~max_g//g-1

    #gx와 gx+g의 개수의 곱만큼 순서쌍이 존재할것.

    for g in range(1,max_g+1):
        
        for x in range(1,max_g//g):
                            
            if g*(x+1) ^ g*x == g:
                
                count += (A[g*x] * A[g*(x+1)])
          
    print(count)
