#1부터 n까지 이어서 쓴 문자열에서 k번째 정수를 찾는 방법

#1부터 n까지 이어쓴 문자열의 길이
def count(n):
    
    m = len(str(n))

    result = 0

    for i in range(1,m):
        
        result += i*(9*(10**(i-1)))
    
    result += m*(n-(10**(m-1))+1)
    
    return result

#x이하까지 이어쓴 문자열의 길이가 k이면 정수 x에 정답이 있다
n,k = map(int,input().split())

start,end = 1,n+1

while start < end:
    
    mid = (start + end)//2

    c = count(mid)

    if c >= k:
        
        end = mid
    
    else:
        
        start = mid + 1

if end >= n+1: #범위를 넘어간경우 해당 범위에 정답이 없다
    
    print(-1)

else:
    
    #범위 안에 end가 있다면, end-1까지 길이를 구하고
    c = count(end-1)
    #end값을 하나하나 순회해서 길이가 k가 맞으면 그 정수를 출력
    for j in str(end):
        
        if c+1 == k:
            
            break
        
        c += 1
    
    print(j)