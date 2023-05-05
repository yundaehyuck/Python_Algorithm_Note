from sys import stdin

def update(tree,index,value,b):
    
    index += b

    tree[index] += value

    while index > 1:
        
        index >>= 1

        tree[index] = tree[2*index] + tree[2*index+1]

def query(tree,b,left,right):
    
    left += b
    right += b

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


T = int(stdin.readline())

for _ in range(T):
    
    b,p,q = map(int,stdin.readline().split())

    tree = [0]*(2*b)

    for _ in range(p+q):
        
        x,y,z = stdin.readline().rstrip().split()

        y = int(y)
        z = int(z)

        if x == 'P':
            
            update(tree,y-1,z,b)
        
        else:
            
            print(query(tree,b,y-1,z))