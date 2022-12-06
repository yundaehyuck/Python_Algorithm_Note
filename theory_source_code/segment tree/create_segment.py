#return을 사용하지 않는 재귀함수
def create_segment(A,tree,A_start,A_end,tree_index):
    
    #리프노드라면, 배열의 해당 수를 트리 노드에 저장해야함
    if A_start == A_end:
        
        tree[tree_index] = A[A_start]
    
    #리프노드가 아닌경우
    else:
        
        #왼쪽과 오른쪽을 구분하기 위해 
        A_mid = (A_start+A_end)//2
        
        #부모 인덱스가 tree_index이고 [A_start,A_end]를 저장한다면
        
        #왼쪽 구간은 [A_start,A_mid]
        #왼쪽 자식의 노드 인덱스는 2*tree_index
        create_segment(A,tree,A_start,A_mid,2*tree_index)
        
        #오른쪽 구간은 [A_mid+1,A_end]
        #오른쪽 자식의 노드 인덱스는 2*tree_index+1
        create_segment(A,tree,A_mid+1,A_end,2*tree_index+1)
        
        #부모 인덱스에 저장된 값은, 왼쪽 자식과 오른쪽 자식의 합이다.
        tree[tree_index] = tree[2*tree_index] + tree[2*tree_index+1]

"""       
#return을 사용하는 재귀함수
def create_segment(A,tree,A_start,A_end,tree_index):
    
    #리프노드라면, 배열의 해당 수를 트리 노드에 저장해야함
    if A_start == A_end:
        
        tree[tree_index] = A[A_start]
        
        return tree[tree_index]
    
    #리프노드가 아닌경우
    else:
        
        #왼쪽과 오른쪽을 구분하기 위해 
        A_mid = (A_start+A_end)//2
        
        #부모 인덱스가 tree_index이고 [A_start,A_end]를 저장한다면
        
        #왼쪽 구간은 [A_start,A_mid]
        #왼쪽 자식의 노드 인덱스는 2*tree_index
        left_node = create_segment(A,tree,A_start,A_mid,2*tree_index)
        
        #오른쪽 구간은 [A_mid+1,A_end]
        #오른쪽 자식의 노드 인덱스는 2*tree_index+1
        right_node = create_segment(A,tree,A_mid+1,A_end,2*tree_index+1)
        
        #부모 인덱스에 저장된 값은, 왼쪽 자식과 오른쪽 자식의 합이다.
        tree[tree_index] = left_node + right_node
        
        return tree[tree_index]
"""

import math

A = [1,2,3,4,5,6,7,8,9,10]

#배열의 크기 N
N = len(A)

#세그먼트 트리의 노드 수
n = 2**(math.ceil(math.log2(N))+1)-1

#세그먼트 트리의 크기
#[0]*n으로 하면... 0~n-1까지만 가능이라
#[0]*(n+1)로 해서 노드 인덱스가 1~n까지 가능하게

tree = [0]*(n+1)

#전체 구간은 [0,N-1]
#루트 노드의 인덱스는 1번

create_segment(A,tree,0,N-1,1)

print(tree)
[0, 55, 15, 40, 6, 9, 21, 19, 3, 3, 4, 5, 13, 8, 9, 10, 1, 2, 0, 0, 0, 0, 0, 0, 6, 7, 0, 0, 0, 0, 0, 0]