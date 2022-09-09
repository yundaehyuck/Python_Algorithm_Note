#https://www.acmicpc.net/problem/1920

from sys import stdin

def binary_search(array,target,start,end):
    
    while start <= end:
        
        mid = (start+end)//2

        if array[mid] == target:
            
            return 1
        
        elif array[mid] > target:
            
            end = mid-1
        
        else:
            
            start = mid+1
    
    return 0

n = int(stdin.readline())

array = list(map(int,stdin.readline().split()))

m = int(stdin.readline())

m_array = list(map(int,stdin.readline().split()))

array.sort()

for target in m_array:
    
    print(binary_search(array,target,0,n-1))