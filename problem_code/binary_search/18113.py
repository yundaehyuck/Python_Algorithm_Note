from sys import stdin

def binary_search(array,m,start,end):

    max_m = sum(array)
    
    while start < end:
        
        mid = start + (end - start)//2

        total = 0

        for k in array:
            
            total += k//mid
            
             
        if total >= m:

            start = mid + 1

        else:
            
            end = mid
    
    if end == 1:
        
        if max_m < m:
            
            return -1

    return end - 1

n,k,m = map(int,stdin.readline().split())

kimbob = []

for i in range(n):
    
    L = int(stdin.readline())

    if L > k:
        
        if L < 2*k:
            
            kimbob.append(L-k)
        
        elif L > 2*k:
            
            kimbob.append(L-2*k)

if kimbob == []:
    
    print(-1)

else:
    
    kimbob.sort()

    print(binary_search(kimbob,m,1,kimbob[-1]+1))