from sys import stdin

def factorial_zero(n):
    
    answer = 0

    i = 1

    while 1:
        
        x = n//(5**i)

        if x == 0:
            
            break
        
        else:

            answer += x
            i += 1
    
    return answer

def binary_search(target,start,end):
    
    while start < end:
        
        mid = start + (end - start)//2

        if factorial_zero(mid) >= target:
            
            end = mid
        
        else:
            
            start = mid + 1
    
    return end
          
m = int(stdin.readline())

answer = binary_search(m,1,1000000001)

if factorial_zero(answer) != m:
    
    print(-1)

else:
    
    print(answer)