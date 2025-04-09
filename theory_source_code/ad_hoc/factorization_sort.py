#인접한 두 수 A[i],A[i+1]을 a*b = A[i]*A[i+1], a+b != A[i]+A[i+1]인 두 수 a,b로 바꿀때
#배열 A를 비내림차순으로 정렬할 수 있는가?
def get_prime(n):
    
    result = [1]*(n+1)
    result[0] = 0
    result[1] = 0

    for i in range(2,int(n**(1/2))+1):
        
        if result[i] == 1:
            
            for j in range(i*i,n+1,i):
                
                result[j] = 0
    
    return result

def check(A):
    
    x = A[0]

    for i in range(1,n):
        
        if x > A[i]:
            
            return False
        
        x = A[i]
    
    return True

n = int(input())

A = list(map(int,input().split()))

prime = get_prime(10**6)

no = True

#인접한 두 수의 곱이 합성수인 쌍이 하나라도 존재한다면,
#(1,A[i]*A[i+1])로 바꾸고, 다시 (A[i]*A[i+1],A[i+2])도 곱이 합성수가 되므로
#(1,1,1,...A[i]*A[i+1]*A[i+2]....)로 바꿀 수 있어서 비내림차순이 된다
for i in range(n-1):
    
    x,y = A[i],A[i+1]

    if (x == 1 and prime[y] == 1) or (prime[x] == 1 and y == 1) or (x == 1 and y == 1):
        
        continue
    
    else:
        
        no = False
        break

if no:
    
    if check(A):
        
        print('YES')
    
    else:

        print('NO')

else:
    
    print('YES')