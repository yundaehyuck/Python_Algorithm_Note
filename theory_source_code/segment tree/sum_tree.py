import math
from sys import stdin

#세그먼트 트리 생성

def create_segment(A,tree,tree_index,A_start,A_end):
    
    #리프 노드라면

    if A_start == A_end:
        
        tree[tree_index] = A[A_start]
    
    else: #리프노드가 아니라면
        
        A_mid = (A_start + A_end) // 2

        create_segment(A,tree,2*tree_index, A_start, A_mid)
        create_segment(A,tree,2*tree_index+1, A_mid+1, A_end)

        tree[tree_index] = tree[2*tree_index] + tree[2*tree_index+1]

#구간의 합을 구하는 함수
def query_sum(tree,tree_index,start,end,left,right):
    
    #[left,right]가 [start,end]를 벗어났다

    if left > end or right < start:
        
        return 0
    
    #[left,right]가 [start,end]를 포함한다

    if left <= start and end <= right:
        
        return tree[tree_index]
    
    #그 이외의 경우 왼쪽, 오른쪽 탐색

    mid = (start+end)//2

    left_sum = query_sum(tree,2*tree_index, start,mid,left,right)
    right_sum = query_sum(tree,2*tree_index+1,mid+1,end,left,right)

    return left_sum + right_sum

#배열의 값을 바꾸는 함수

def update_tree(tree,tree_index,start,end,index,value,difference):
    
    #index가 [start,end]에 포함되지 않는다
    
    if index < start or index > end:
        
        return
    
    #index가 [start,end]에 포함된다
    
    tree[tree_index] = tree[tree_index] + difference

    #리프노드가 아니라면 왼쪽, 오른쪽으로 나누어 탐색

    mid = (start + end) // 2

    if start != end: #이 부분 까먹었는데... 주의

        update_tree(tree,2*tree_index, start, mid, index, value, difference)
        update_tree(tree,2*tree_index+1,mid+1,end, index, value, difference)

def update(A,tree,N,index,value):
    
    difference = value - A[index]

    A[index] = value

    update_tree(tree,1,0,N-1,index,value,difference)

N,m,k = map(int,stdin.readline().split())

#A배열 만들기

A = []

for _ in range(N):
    
    a = int(stdin.readline())

    A.append(a)

#세그먼트 트리 초기화

n = 2**(math.ceil(math.log2(N))+1) -1

tree = [0]*(n+1)

create_segment(A,tree,1,0,N-1)

for _ in range(m+k):
    
    a,b,c = map(int,stdin.readline().split())

    if a == 1:
        
        update(A,tree,N,b-1,c)
    
    elif a == 2:
        
        print(query_sum(tree,1,0,N-1,b-1,c-1))