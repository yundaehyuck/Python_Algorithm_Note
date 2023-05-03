import math
from sys import stdin

#반복문으로 구현하는 세그먼트 트리
#배열 A의 크기가 n이면, 세그먼트 트리에서 필요한 노드 수는 2n-1개

def create_segment(A,tree,n):
    
    #세그먼트 트리의 리프 노드를 결정
    for i in range(n):
        
        tree[n+i] = A[i]
    
    #나머지 노드의 값을 아래에서부터 올라가면서 결정
    #부모 노드가 i이면, 왼쪽 자식은 2i, 오른쪽 자식은 2i+1
    for i in range(n-1,0,-1):
        
        tree[i] = tree[2*i] + tree[2*i+1]

def query_sum(tree,left,right,n):
    
    left += n
    right += n

    """ Basically the left and right indices
    will move towards right and left respectively
    and with every each next higher level and
    compute the minimum at each height change
    the index to leaf node first """
    
    result = 0 #합의 초기값

    while left < right:
        
        if left & 1: #left index가 홀수라면...
            
            result += tree[left]
            left += 1
        
        if right & 1: #right index가 홀수라면...
            
            right -= 1
            result += tree[right]
        
        #move to the next higher level
        left //= 2
        right //= 2
    
    return result

def update(tree,index,value,n):
    
    #change the index to leaf node first
    index += n

    #update the value at the leaf node, at the exact index
    tree[index] = value

    while index > 1:
        
        #move up one level at a time in the segment tree
        index >>= 1

        #update the value in the node in the next higher level
        tree[index] = tree[2*index] + tree[2*index+1]

N = int(stdin.readline())

A = []

for _ in range(N):
    
    h = int(stdin.readline())

    A.append(h)

n = 2*N - 1

tree = [0]*(n+1) #tree의 크기는 배열의 2배로 초기화

create_segment(A,tree,N)

t = int(stdin.readline())

for _ in range(t):
    
    q,a,b = stdin.readline().rstrip().split()

    a = int(a)
    b = int(b)

    if q[0] == 'U':

        update(tree,a-1,b,N)
    
    else:
        
        #[left,right] query를 구할때,
        #[left,right+1]을 넣어줘야한다
        print(query_sum(tree,a-1,b,N)) 