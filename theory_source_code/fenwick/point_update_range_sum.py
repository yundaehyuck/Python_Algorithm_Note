#fenwick tree 기본

from sys import stdin

#i번째 수에 value만큼 더하는 함수
def point_update(i,value):
    
    #현재 i에 value를 더하고,
    #0이 아닌 마지막 비트 (i & -i)만큼 이동하여 그곳에 value를 더해줌
    #i가 마지막 인덱스를 넘어가면 종료
    while i <= n:
        
        tree[i] += value
        i += (i & -i)

#1~i번 index까지 누적합을 구하는 함수
def range_sum(i):
    
    result = 0

    #현재 i번의 값을 더해주고
    #0이 아닌 마지막 비트 (i & -i)만큼 빼주면서 다음 i로 이동
    #i가 첫번째 인덱스보다 밑으로 넘어가면 종료
    while i > 0:
        
        result += tree[i]

        i -= (i & -i)
    
    return result

n,m,k = map(int,stdin.readline().split())

A = [0]

#binary indexed tree를 만드는 방법
#1번부터 n번 index
tree = [0]*(n+1)

for i in range(1,n+1):
    
    a = int(stdin.readline())
    A.append(a)
    point_update(i,a) #i번째 index를 a로 바꿔줌

for _ in range(m+k):
    
    a,b,c = map(int,stdin.readline().split())

    if a == 1:
        
        #b번째 원소를 c로 바꾼다
        #A[b-1] = k이면, A[b-1] = c로 바꿀려면?
        #A[b-1]에 c-k를 더한다. 
        point_update(b,c-A[b])
        A[b] = c
    
    else:
        
        print(range_sum(c) - range_sum(b-1))