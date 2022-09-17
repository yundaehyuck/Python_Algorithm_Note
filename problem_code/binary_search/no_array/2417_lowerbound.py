#https://www.acmicpc.net/problem/2417

from sys import stdin

def lower_bound(target,start,end):
    
    while start < end:
        
        mid = (start+end)//2

        if mid**2 < target:
            
            start = mid+1
        
        else:
            
            end = mid
    
    return end

n = int(stdin.readline())

if n == 0:
    
    print(0)

else:

    print(lower_bound(n,0,n+1))