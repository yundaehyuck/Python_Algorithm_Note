import math
from sys import stdin

def update(tree,tree_index,start,end,index,value):
    
    if index < start or index > end:
        
        return
    
    if start == end:
        
        tree[tree_index] += value
        return
    
    mid = (start+end)//2

    update(tree,2*tree_index,start,mid,index,value)
    update(tree,2*tree_index+1,mid+1,end,index,value)

    tree[tree_index] = tree[2*tree_index] + tree[2*tree_index+1]

def query(tree,tree_index,start,end,left,right):
    
    if left > end or right < start:
        
        return 0
    
    if left <= start and end <= right:
        
        return tree[tree_index]
    
    mid = (start+end)//2

    left_sum = query(tree,2*tree_index,start,mid,left,right)
    right_sum = query(tree,2*tree_index+1,mid+1,end,left,right)

    return left_sum + right_sum

N,q = map(int,stdin.readline().split())

n = 2**(math.ceil(math.log2(N))+1)-1

tree = [0]*(n+1)

for _ in range(q):
    
    a,b,c = map(int,stdin.readline().split())

    if a == 1:
        
        update(tree,1,0,N-1,b-1,c)
    
    else:
        
        print(query(tree,1,0,N-1,b-1,c-1))