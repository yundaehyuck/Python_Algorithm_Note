from sys import stdin

def create_segment(A,tree,n):
    
    for i in range(n):
        
        tree[n+i] = A[i]
    
    for i in range(n-1,0,-1):
        
        tree[i] = tree[2*i]+tree[2*i+1]

def update(tree,n,index,value):
    
    index += n

    tree[index] += value

    while index > 1:
        
        index = index >> 1

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

def binary_search(tree,target,start,end):
    
    while start < end:
        
        mid = start + (end-start)//2

        k = query(tree,n,0,mid+1) #[0,mid]까지 구간합
        
        #구간합이 배치할 군인의 군번 target보다 크거나 같다면? mid에 배치가능
        if k >= target: 
            
            end = mid
        
        #target보다 작다면... 배치해야할 부대 번호는 mid + 1 이후에 있다
        else:
            
            start = mid + 1
    
    #index는 0번부터 세는데.. 부대번호는 1번부터 세야하니까..
    return end+1

n = int(stdin.readline())

A = list(map(int,stdin.readline().split()))

tree = [0]*(2*n)

create_segment(A,tree,n)

m = int(stdin.readline())

for _ in range(m):
    
    q = stdin.readline().rstrip()

    if q[0] == '1':
        
        _,b,c = map(int,q.split())

        update(tree,n,b-1,c)
    
    else:
        
        _,b = map(int,q.split())

        print(binary_search(tree,b,0,n))