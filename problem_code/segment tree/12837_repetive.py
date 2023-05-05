from sys import stdin

def update(tree,index,value,n):
    
    index += n

    tree[index] += value

    while index > 1:
        
        index >>= 1

        tree[index] = tree[2*index] + tree[2*index+1]

def query(tree,n,left,right):
    
    left += n
    right += n

    m = 0

    while left < right:
        
        if left & 1:
            
            m += tree[left]
            left += 1
        
        if right & 1:
            
            right -= 1
            m += tree[right]
        
        left //= 2
        right //= 2
    
    return m

n,q = map(int,stdin.readline().split())

tree = [0]*(2*n)

for _ in range(q):
    
    a,b,c = map(int,stdin.readline().split())

    if a == 1:
        
        update(tree,b-1,c,n)
    
    else:
        
        print(query(tree,n,b-1,c))