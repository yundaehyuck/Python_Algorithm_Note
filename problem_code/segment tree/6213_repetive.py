from sys import stdin

def create_segment(A,tree,n):
    
    for i in range(n):
        
        tree[n+i][0] = A[i]
        tree[n+i][1] = A[i]
    
    for i in range(n-1,0,-1):
        
        tree[i][0] = min(tree[2*i][0],tree[2*i+1][0])
        tree[i][1] = max(tree[2*i][1],tree[2*i+1][1])

def query(tree,n,left,right):
    
    left += n
    right += n

    m1 = 1000001
    m2 = 0

    while left < right:
        
        if left & 1:
            
            m1 = min(m1,tree[left][0])
            m2 = max(m2,tree[left][1])
            left += 1
        
        if right & 1:
            
            right -= 1
            m1 = min(m1,tree[right][0])
            m2 = max(m2,tree[right][1])
        
        left //= 2
        right //= 2
    
    return m2-m1

n,q = map(int,stdin.readline().split())

A = []

for _ in range(n):
    
    a = int(stdin.readline())
    A.append(a)

tree = [[0]*2 for _ in range(2*n)]

create_segment(A,tree,n)

for _ in range(q):
    
    a,b = map(int,stdin.readline().split())

    print(query(tree,n,a-1,b))