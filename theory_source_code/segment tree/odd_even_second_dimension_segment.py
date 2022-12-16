import math
from sys import stdin

#[[0,0] for _ in range(n+1)] 형태로 트리 생성

def create_segment(A,tree,tree_index,A_start,A_end):
    
    if A_start == A_end:
        
        #0번에 짝수의 개수를 저장하고
        
        if A[A_start] % 2 == 0:
            
            tree[tree_index][0] += 1
        
        #1번에 홀수의 개수를 저장
        elif A[A_start] % 2 == 1:
            
            tree[tree_index][1] += 1
    
    else:
        
        A_mid = (A_start+A_end)//2

        create_segment(A,tree,2*tree_index,A_start,A_mid)
        create_segment(A,tree,2*tree_index+1,A_mid+1,A_end)
        
        #부모 노드의 짝수 개수는, 자식 노드의 짝수 개수의 합
        #홀수 개수는, 자식 노드의 홀수 개수의 합

        tree[tree_index][0] = tree[2*tree_index][0] + tree[2*tree_index+1][0]
        tree[tree_index][1] = tree[2*tree_index][1] + tree[2*tree_index+1][1]

def query(tree,tree_index,start,end,left,right,number):
    
    if left > end or right < start:
        
        return 0
    
    if left <= start and end <= right:
        
        #number = 2이면, 짝수개수
        #number = 3이면, 홀수개수
        return tree[tree_index][number-2]
    
    mid = (start+end)//2

    left_num = query(tree,2*tree_index,start,mid,left,right,number)
    right_num = query(tree,2*tree_index+1,mid+1,end,left,right,number)

    return left_num+right_num

def update(A,tree,tree_index,start,end,index,value):
    
    if index < start or index > end:
        
        return
    
    if start == end:
        
        #기존의 값 A[index]가 짝수이면
        if A[index] % 2 == 0:
            
            tree[tree_index][0] -= 1
        #홀수이면..
        elif A[index] % 2 == 1:
            
            tree[tree_index][1] -= 1
        
        #기존 값 제거후에 업데이트하고
        A[index] = value
        
        #업데이트한 값이 짝수인지 홀수인지에 따라
        if value % 2 == 0:
            
            tree[tree_index][0] += 1
        
        elif value % 2 == 1:

            tree[tree_index][1] += 1
        
        return
    
    mid = (start+end)//2

    update(A,tree,2*tree_index,start,mid,index,value)
    update(A,tree,2*tree_index+1,mid+1,end,index,value)

    tree[tree_index][0] = tree[2*tree_index][0]+tree[2*tree_index+1][0]
    tree[tree_index][1] = tree[2*tree_index][1]+tree[2*tree_index+1][1]

N = int(stdin.readline())

A = list(map(int,stdin.readline().split()))

m = int(stdin.readline())

n = 2**(math.ceil(math.log2(N))+1)-1

tree = [[0,0] for _ in range(n+1)]

create_segment(A,tree,1,0,N-1)

for _ in range(m):
    
    a,b,c = map(int,stdin.readline().split())

    if a == 1:
        
        update(A,tree,1,0,N-1,b-1,c)
    
    else:
        
        print(query(tree,1,0,N-1,b-1,c-1,a))