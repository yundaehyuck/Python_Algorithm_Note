from sys import stdin

def binary_search(F,target,start,end):
    
    while start < end:
        
        mid = start + (end-start)//2

        if F[mid]*0.9 > target:
            
            end = mid
        
        else:
            
            start = mid + 1
    
    return end - 1

n = int(stdin.readline())

F = list(map(int,stdin.readline().split()))

F.sort()

count = 0

for i in range(n):
    
    k = binary_search(F,F[i],i+1,n)
        
    count += (k-i)

print(count)