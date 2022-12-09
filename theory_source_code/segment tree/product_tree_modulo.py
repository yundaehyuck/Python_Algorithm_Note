import math
from sys import stdin

#세그먼트 트리를 만드는 함수
def create_segment(A,tree,tree_index,A_start,A_end):
    
    if A_start == A_end:
        
        tree[tree_index] = A[A_start]
    
    else:
        
        A_mid = (A_start+A_end)//2
        create_segment(A,tree,2*tree_index,A_start,A_mid)
        create_segment(A,tree,2*tree_index+1,A_mid+1,A_end)
        
        #곱을 1000000007로 나눈 나머지를 저장

        tree[tree_index] = (tree[2*tree_index] * tree[2*tree_index+1]) % 1000000007

#임의의 구간의 곱을 구하는 함수
def query_product(tree,tree_index,start,end,left,right):
    
    if left > end or right < start:
        
        return 1
    
    if left <= start and end <= right:
        
        return tree[tree_index]
    
    mid = (start+end)//2

    left_product = query_product(tree,2*tree_index,start,mid,left,right)
    right_product = query_product(tree,2*tree_index+1,mid+1,end,left,right)
    
    #곱을 1000000007로 나눈 나머지를 저장
    
    return (left_product*right_product)% 1000000007

#A배열의 특정 인덱스의 값을 바꾸는 함수
def update(A,tree,tree_index,start,end,index,value):
    
    if index < start or index > end:
        
        return
    
    if start == end:
        
        A[index] = value
        tree[tree_index] = value
        return
    
    mid = (start+end)//2
    
    update(A,tree,2*tree_index,start,mid,index,value)
    update(A,tree,2*tree_index+1,mid+1,end,index,value)
    
    #곱을 1000000007로 나눈 나머지를 저장

    tree[tree_index] = (tree[2*tree_index]*tree[2*tree_index+1])% 1000000007
    

N,m,k = map(int,stdin.readline().split())

A = []

for _ in range(N):
    
    a = int(stdin.readline())

    A.append(a)

n = 2**(math.ceil(math.log2(N))+1)-1

tree = [0]*(n+1)

create_segment(A,tree,1,0,N-1)

for _ in range(m+k):
    
    a,b,c = map(int,stdin.readline().split())

    if a == 1:
        
        update(A,tree,1,0,N-1,b-1,c)
    
    elif a == 2:
        
        print(query_product(tree,1,0,N-1,b-1,c-1))