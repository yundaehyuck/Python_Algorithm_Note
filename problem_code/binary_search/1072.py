from sys import stdin

def binary_search(target,start,end,x,y):
    
    while start < end:
        
        mid = start + (end-start)//2

        new_y = y + mid-x

        new_z = new_y*100//mid

        if new_z != target:
            
            end = mid
        
        else:
            
            start = mid + 1
    
    return end

MAX = 10**18

x,y = map(int,stdin.readline().split())

z = y*100//x

answer = binary_search(z,x+1,MAX+1,x,y)

if answer > MAX:
    
    print(-1)

else:
    
    print(answer - x)