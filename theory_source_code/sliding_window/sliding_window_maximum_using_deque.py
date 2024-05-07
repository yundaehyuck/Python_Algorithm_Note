#deque를 이용한 구간 최댓값 트릭
#배열 A에서 모든 길이 k인 연속 부분구간 내의 최댓값을 찾는 방법

#deque의 첫번째 원소를 구간의 최댓값 원소의 인덱스로 저장
from collections import deque

n,k = map(int,input().split())

A = list(map(int,input().split()))

queue = deque()

#0~k-1을 먼저 순회해서, 
for i in range(k):
    
    #deque의 맨 오른쪽 원소보다, 추가해야하는 원소 A[i]가 더 크거나 같다면..
    #deque의 오른쪽을 제거
    while queue and A[i] >= A[queue[-1]]:
            
        queue.pop()
    
    queue.append(i) #이번에 추가해야할 원소의 인덱스를 추가

#이제 k~n-1을 순회해서..
for i in range(k,n):
    
    #이전 구간 [i-k,i-1]에서 최댓값은 A[deque[0]]
    print(A[queue[0]],end=' ')
    
    #버려야할 원소의 인덱스는 i-k
    #i-k보다 작거나 같은 deque의 왼쪽에 있는 인덱스를 모두 제거
    while queue and i-k >= queue[0]:
        
        queue.popleft()
    
    #추가해야할 원소는 A[i]
    #A[i]가 deque의 오른쪽 원소보다 크거나 같다면 deque의 오른쪽을 계속 제거
    while queue and A[i] >= A[queue[-1]]:
        
        queue.pop()
    
    queue.append(i) #이제 i 인덱스를 추가

#모든 반복이 끝나면, 마지막 구간 [n-k-1,n-1]에서 최댓값은 A[deque[0]]
print(A[queue[0]],end=' ')