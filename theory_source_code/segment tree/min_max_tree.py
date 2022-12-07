import math
from sys import stdin

#method = 0이면 min_tree
#method = 1이면 max_tree
def create_segment(A,tree,tree_index,A_start,A_end,method):
    
    if A_start == A_end:
        
        tree[tree_index] = A[A_start]
    
    else:
        
        A_mid = (A_start+A_end)//2

        create_segment(A,tree,2*tree_index,A_start,A_mid,method)
        create_segment(A,tree,2*tree_index+1,A_mid+1,A_end,method)

        if method == 0:

            tree[tree_index] = min(tree[2*tree_index],tree[2*tree_index+1])
        
        elif method == 1:
            
            tree[tree_index] = max(tree[2*tree_index],tree[2*tree_index+1])

#method = 0이면 min
#method = 1이면 max
def query(tree,tree_index,start,end,left,right,method):
    
    if left > end or right < start:
        
        if method == 0:
            
            return 1000000001 #A배열 수들의 최댓값보다 크도록
        
        elif method == 1:
            
            return 0 #A배열 수들의 최솟값보다 작게
    
    if left <= start and end <= right:
        
        return tree[tree_index]
    
    mid = (start+end)//2
    
    left_value = query(tree,2*tree_index,start,mid,left,right,method)
    right_value = query(tree,2*tree_index+1,mid+1,end,left,right,method)

    if method == 0:
        
        return min(left_value,right_value)
    
    elif method == 1:
        
        return max(left_value,right_value)

    


N,m = map(int,stdin.readline().split())

A = []

for _ in range(N):
    
    a = int(stdin.readline())

    A.append(a)

n = 2**(math.ceil(math.log2(N))+1)-1

min_tree = [0]*(n+1)
max_tree = [0]*(n+1)

create_segment(A,min_tree,1,0,N-1,0)
create_segment(A,max_tree,1,0,N-1,1)
    
for _ in range(m):
    
    a,b = map(int,stdin.readline().split())
    
    print(query(min_tree,1,0,N-1,a-1,b-1,0),query(max_tree,1,0,N-1,a-1,b-1,1))