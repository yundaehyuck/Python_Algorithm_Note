import math
from sys import stdin

#값의 부호를 구하는 함수
def sign(x):
    
    if x > 0:
        return 1
    
    elif x < 0:
        return -1
    
    else:
        
        return 0
 
#세그먼트 트리를 만들때, 값의 부호를 저장한다
def create_segment(A,tree,tree_index,A_start,A_end):
    
    if A_start == A_end:
        
        tree[tree_index] = sign(A[A_start]) #값의 부호 저장
    
    else:
        
        A_mid = (A_start + A_end)//2

        create_segment(A,tree,2*tree_index,A_start,A_mid)
        create_segment(A,tree,2*tree_index+1,A_mid+1,A_end)
        
        #리프노드에 모두 값의 부호가 저장되어 있으니, 올라오면서 알아서 값의 부호끼리 곱셈이 된다
        tree[tree_index] = tree[2*tree_index]*tree[2*tree_index+1]

#트리의 노드에 값의 부호가 저장되어 있으니, 계산 결과는 무조건 값의 부호가 된다.
def query_product(tree,tree_index,start,end,left,right):
    
    if left > end or right < start:
        
        return 1
    
    if left <= start and end <= right:
        
        return tree[tree_index]
    
    mid = (start+end)//2

    left_product = query_product(tree,2*tree_index,start,mid,left,right)
    right_product = query_product(tree,2*tree_index+1,mid+1,end,left,right)

    return left_product * right_product

#리프노드까지 탐색하면서 새로운 값으로 바꿔줄때, 값의 부호를 넣어준다. 
def update(A,tree,tree_index,start,end,index,value):
    
    if index > end or index < start:
        
        return
    
    if start == end:
        
        A[index] = value
        tree[tree_index] = sign(value) #여기만 값의 부호를 넣어서 바꿔주면..
        return
    
    mid = (start+end)//2

    update(A,tree,2*tree_index,start,mid,index,value)
    update(A,tree,2*tree_index+1,mid+1,end,index,value)
    
    #자식에 모두 값의 부호로 되어 있으니까, 계산하면 값의 부호로 나온다.
    tree[tree_index] = tree[2*tree_index]*tree[2*tree_index+1]

while 1:
    
    try:
        
        N,k = map(int,stdin.readline().split())

        A = list(map(int,stdin.readline().split()))

        n = 2**(math.ceil(math.log2(N)+1))-1

        tree = [0]*(n+1)

        create_segment(A,tree,1,0,N-1)

        answer = []

        for _ in range(k):

            command = stdin.readline().rstrip().split()

            if command[0] == 'C':

                update(A,tree,1,0,N-1,int(command[1])-1, int(command[2]))

            elif command[0] == 'P':

                value = query_product(tree,1,0,N-1,int(command[1])-1,int(command[2])-1)

                if value == 0:

                    answer.append('0')

                elif value == 1:

                    answer.append('+')

                elif value == -1:

                    answer.append('-')

        print(''.join(answer))
    
    except:
        
        break