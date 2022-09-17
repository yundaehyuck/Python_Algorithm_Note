#https://www.acmicpc.net/problem/13706
from sys import stdin

def binary_search(array,target,start,end):
    
    while start <= end:
        
        mid = (start+end)//2

        if (array[mid])**2 == target:
            
            return array[mid]
        
        elif (array[mid])**2 > target:
            
            end = mid-1
        
        elif (array[mid])**2 < target:
            
            start = mid + 1
    
    return 0


n = int(stdin.readline())

print(binary_search(list(range(0,n)), n, 0, n-1))