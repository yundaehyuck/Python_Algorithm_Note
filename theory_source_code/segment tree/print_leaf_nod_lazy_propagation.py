import math
from sys import stdin

def create_segment(A,tree,tree_index,A_start,A_end):
    
    if A_start == A_end:
        
        tree[tree_index] = A[A_start]

    else:
        
        A_mid = (A_start+A_end)//2

        create_segment(A,tree,2*tree_index,A_start,A_mid)
        create_segment(A,tree,2*tree_index+1,A_mid+1,A_end)
        
        #아무 연산도 하지 않는다

def update_lazy(tree,lazy,tree_index,start,end):
    
    if lazy[tree_index] != 0:
        
        tree[tree_index] += (end-start+1)*lazy[tree_index]

        if start != end:
            
            lazy[2*tree_index] += lazy[tree_index]
            lazy[2*tree_index+1] += lazy[tree_index]
        
        lazy[tree_index] = 0


def query_print(tree,lazy,tree_index,start,end,index):
    
    update_lazy(tree,lazy,tree_index,start,end)
    
    if index > end or index < start:
        
        return
    
    #원하는 리프노드 index에 도달하면... 해당 값을 return
    if start == end and index == end:
        
        return tree[tree_index]
    
    mid = (start+end)//2
    
    #왼쪽으로 들어간 경로와 오른쪽으로 들어간 경로는 둘 중 하나
    #None이거나, A[index]

    left_value = query_print(tree,lazy,2*tree_index,start,mid,index)
    right_value = query_print(tree,lazy,2*tree_index+1,mid+1,end,index)

    if left_value == None:
        
        return right_value
    
    elif right_value == None:
        
        return left_value

def update_range(tree,lazy,tree_index,start,end,left,right,value):
    
    update_lazy(tree,lazy,tree_index,start,end)
    
    if left > end or right < start:
        
        return
    
    if left <= start and end <= right:
        
        tree[tree_index] += (end-start+1)*value

        if start != end:
            
            lazy[2*tree_index] += value
            lazy[2*tree_index+1] += value
        
        return
    
    mid = (start+end)//2

    update_range(tree,lazy,2*tree_index,start,mid,left,right,value)
    update_range(tree,lazy,2*tree_index+1,mid+1,end,left,right,value)
    
    #아무 연산도 하지 않는다
    

N = int(stdin.readline())

A = list(map(int,stdin.readline().split()))

m = int(stdin.readline())

n = 2**(math.ceil(math.log2(N))+1)-1

tree = [0]*(n+1)
lazy = [0]*(n+1)

create_segment(A,tree,1,0,N-1)

for _ in range(m):
    
    query = list(map(int,stdin.readline().split()))

    if query[0] == 1:
        
        update_range(tree,lazy,1,0,N-1,query[1]-1,query[2]-1,query[3])
    
    elif query[0] == 2:
        
        print(query_print(tree,lazy,1,0,N-1,query[1]-1))