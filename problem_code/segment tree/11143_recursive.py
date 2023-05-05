import math
from sys import stdin

def update(A,tree,tree_index,start,end,index,value):
    
    if index < start or end < index:
        
        return
    
    if start == end:
        
        A[index] += value
        tree[tree_index] += value
        return
    
    mid = (start + end)//2
    
    update(A,tree,2*tree_index,start,mid,index,value)
    update(A,tree,2*tree_index+1,mid+1,end,index,value)

    tree[tree_index] = tree[2*tree_index] + tree[2*tree_index+1]

def query_sum(tree,tree_index,start,end,left,right):
    
    if right < start or end < left:
        
        return 0
    
    if left <= start and end <= right:
        
        return tree[tree_index]
    
    mid = (start+end)//2

    left_sum = query_sum(tree,2*tree_index,start,mid,left,right)
    right_sum = query_sum(tree,2*tree_index+1,mid+1,end,left,right)

    return left_sum + right_sum
    

T = int(stdin.readline())

for _ in range(T):
    
    b,p,q = map(int,stdin.readline().split())

    A = [0]*(b)

    n = 2**(math.ceil(math.log2(b))+1)-1

    tree = [0]*(n+1)

    for _ in range(p+q):
        
        q,x,y = stdin.readline().rstrip().split()

        x = int(x)
        y = int(y)

        if q == 'P':
            
            update(A,tree,1,0,b-1,x-1,y)
        
        else:
            
            print(query_sum(tree,1,0,b-1,x-1,y-1))