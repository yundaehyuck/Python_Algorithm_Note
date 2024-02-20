#n과 m중 어느 하나만으로 나누어 떨어지는 k번째 양의 정수 찾기
def gcd(a,b):
    
    while b != 0:
        
        a,b = b,a%b
    
    return a

def lcm(a,b):
    
    return a*b//gcd(a,b)

#x이하에 n이나 m중 어느 하나만으로 나누어 떨어지는 양의 정수의 개수가 k 이하이면
#그러한 x가 정답이므로
#start,end를 설정하고 X = mid로 하면 이분탐색으로 바꿀 수 있다
n,m,k = map(int,input().split())

x = lcm(n,m)

start,end = 1,10**20+1

while start < end:
    
    mid = start + (end - start)//2

    #1부터 mid 이하에 n이나 m중 어느 하나만으로 나누어 떨어지는 정수의 개수
    #mid//n + mid//m - 2*(mid//(lcm(n,m)))
    y = mid//n + mid//m - (mid//x)*2

    if y >= k:
        
        end = mid
    
    else:
        
        start = mid + 1

print(end)