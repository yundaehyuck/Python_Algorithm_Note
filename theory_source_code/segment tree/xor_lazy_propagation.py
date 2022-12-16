import math
from sys import stdin

def create_segment(A,tree,tree_index,A_start,A_end):
    
    if A_start == A_end:
        
        tree[tree_index] = A[A_start]

    else:
        
        A_mid = (A_start+A_end)//2

        create_segment(A,tree,2*tree_index,A_start,A_mid)
        create_segment(A,tree,2*tree_index+1,A_mid+1,A_end)
        
        #아무 연산도 수행하지 않는다

def update_lazy(tree,lazy,tree_index,start,end):
    
    if lazy[tree_index] != 0:
        
        #리프노드가 아니라면, 두 자식 노드에 xor연산을 하면서 lazy값을 누적 전달
        if start != end:
            
            lazy[2*tree_index] ^= lazy[tree_index]
            lazy[2*tree_index+1] ^= lazy[tree_index]
        
        #리프노드라면, 해당 노드의 값에 lazy값을 xor연산해서 갱신
        elif start == end:
            
            tree[tree_index] ^= lazy[tree_index]
        
        lazy[tree_index] = 0


def query_print(tree,lazy,tree_index,start,end,index):
    
    #lazy배열 업데이트
    update_lazy(tree,lazy,tree_index,start,end)

    if index > end or index < start:
        
        return
    
    if start == end and index == end:
        
        return tree[tree_index]
    
    mid = (start+end)//2

    left_value = query_print(tree,lazy,2*tree_index,start,mid,index)
    right_value = query_print(tree,lazy,2*tree_index+1,mid+1,end,index)
    
    #둘중 하나는 None이고, 하나는 리프노드값
    if left_value == None:
        
        return right_value
    
    elif right_value == None:
        
        return left_value

def update_range(tree,lazy,tree_index,start,end,left,right,value):
    
    update_lazy(tree,lazy,tree_index,start,end)

    if left > end or right < start:
        
        return
    
    if left <= start and end <= right:
        
        #리프노드가 아니라면, 두 자식노드의 lazy배열에 value값을 전달
        if start != end:
            
            lazy[2*tree_index] ^= value
            lazy[2*tree_index+1] ^= value
        
        #리프노드에 도달했다면 해당 노드에 value를 연산
        elif start == end:
            
            tree[tree_index] ^= value

        return
    
    mid = (start+end)//2

    update_range(tree,lazy,2*tree_index,start,mid,left,right,value)
    update_range(tree,lazy,2*tree_index+1,mid+1,end,left,right,value)

N = int(stdin.readline())

A = list(map(int,stdin.readline().split()))

m = int(stdin.readline())

n = 2**(math.ceil(math.log2(N))+1)-1

tree = [0]*(n+1)
lazy = [0]*(n+1)

create_segment(A,tree,1,0,N-1)

for _ in range(m):
    
    q = list(map(int,stdin.readline().split()))

    if q[0] == 1:
        
        update_range(tree,lazy,1,0,N-1,q[1],q[2],q[3])
    
    elif q[0] == 2:
        
        print(query_print(tree,lazy,1,0,N-1,q[1]))