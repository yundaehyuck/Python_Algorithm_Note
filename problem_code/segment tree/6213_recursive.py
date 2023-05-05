import math
from sys import stdin

def max_create_segment(A,max_tree,tree_index,start,end):
    
    if start == end:
        
        max_tree[tree_index] = A[start]
    
    else:
        
        mid = (start+end)//2

        max_create_segment(A,max_tree,2*tree_index,start,mid)
        max_create_segment(A,max_tree,2*tree_index+1,mid+1,end)

        max_tree[tree_index] = max(max_tree[2*tree_index],max_tree[2*tree_index+1])

def min_create_segment(A,min_tree,tree_index,start,end):
    
    if start == end:
        
        min_tree[tree_index] = A[start]
    
    else:
        
        mid = (start+end)//2

        min_create_segment(A,min_tree,2*tree_index,start,mid)
        min_create_segment(A,min_tree,2*tree_index+1,mid+1,end)

        min_tree[tree_index] = min(min_tree[2*tree_index],min_tree[2*tree_index+1])


def query(tree,tree_index,start,end,left,right,ind):
    
    if left > end or right < start:
        
        return
    
    if left <= start and end <= right:
        
        return tree[tree_index]
    
    mid = (start + end)//2

    left_value = query(tree,2*tree_index,start,mid,left,right,ind)
    right_value = query(tree,2*tree_index+1,mid+1,end,left,right,ind)

    if ind == 0:
        
        if left_value == None:
            
            return right_value
        
        elif right_value == None:
            
            return left_value
        
        else:

            return min(left_value,right_value)
    
    else:
        
        if left_value == None:
            
            return right_value
        
        elif right_value == None:
            
            return left_value
        
        else:

            return max(left_value,right_value)



        
N,q = map(int,stdin.readline().split())

A = []

for _ in range(N):
    
    a = int(stdin.readline())
    A.append(a)

n = 2**(math.ceil(math.log2(N))+1)-1

max_tree = [0]*(n+1)
min_tree = [0]*(n+1)

max_create_segment(A,max_tree,1,0,N-1)
min_create_segment(A,min_tree,1,0,N-1)

for _ in range(q):
    
    a,b = map(int,stdin.readline().split())

    print(query(max_tree,1,0,N-1,a-1,b-1,1) - query(min_tree,1,0,N-1,a-1,b-1,0))