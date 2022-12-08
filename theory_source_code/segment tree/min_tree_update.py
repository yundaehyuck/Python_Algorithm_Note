import math
from sys import stdin

def create_segment(A,tree,tree_index,A_start,A_end):
    
    if A_start == A_end:
        
        tree[tree_index] = A[A_start]
    
    else:
        
        A_mid = (A_start + A_end)//2

        create_segment(A,tree,2*tree_index,A_start,A_mid)
        create_segment(A,tree,2*tree_index+1,A_mid+1,A_end)

        tree[tree_index] = min(tree[2*tree_index],tree[2*tree_index+1])

def query_min(tree,tree_index,start,end,left,right):
    
    if left > end or right < start:
        
        return 10000000000
    
    if left <= start and end <= right:
        
        return tree[tree_index]
    
    mid = (start+end)//2

    left_min = query_min(tree,2*tree_index,start,mid,left,right)

    right_min = query_min(tree,2*tree_index+1,mid+1,end,left,right)

    return min(left_min,right_min)

#배열 A의 값을 업데이트 하는 함수
def update(A,tree,tree_index,start,end,index,value):
    
    if index > end or index < start:
        
        return
    
    if start == end:
        
        A[index] = value
        tree[tree_index] = value
        return ##return을 하지 않으면 에러난다
    
    mid = (start+end)//2

    update(A,tree,2*tree_index,start,mid,index,value)
    update(A,tree,2*tree_index+1,mid+1,end,index,value)

    tree[tree_index] = min(tree[2*tree_index],tree[2*tree_index+1])
        
N = int(stdin.readline())

A = list(map(int,stdin.readline().split()))

m = int(stdin.readline())

n = 2**(math.ceil(math.log2(N))+1)-1

tree = [0]*(n+1)

create_segment(A,tree,1,0,N-1)

for _ in range(m):
    
    a,b,c = map(int,stdin.readline().split())

    if a == 1:
        
        update(A,tree,1,0,N-1,b-1,c)
    
    elif a == 2:
        
        print(query_min(tree,1,0,N-1,b-1,c-1))