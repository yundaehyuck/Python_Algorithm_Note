from sys import stdin

def binary_search(array,target,start,end):
    
    while start < end:
        
        mid = start + (end - start)//2

        if array[mid] > target:
            
            end = mid 
        
        else:
            
            start = mid + 1
    
    return end
            
T = int(stdin.readline())

for _ in range(T):
    
    n,m = map(int,stdin.readline().split())

    A = list(map(int,stdin.readline().split()))

    B = list(map(int,stdin.readline().split()))

    A.sort()
    B.sort()

    count = 0

    for i in range(m):
        
        j = binary_search(A,B[i],0,n)

        if j == n:
            
            j -= 1
            break

        count += (n-(j+1)+1)

    print(count)    