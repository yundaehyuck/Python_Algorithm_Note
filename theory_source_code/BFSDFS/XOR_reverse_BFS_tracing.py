from collections import deque
from sys import stdin

#n개의 이진코드에서 서로 다른 두 이진코드간 해밍거리가 1인 코드끼리 이동가능
#두 노드 사이 최단 해밍경로 찾기
#해밍경로는 경로에서 인접한 노드간 해밍거리가 1

#BFS 경로 역추적
#prev배열을 이용해서 u에서 v로 이동가능할때, prev[v] = u로 표시해두는게 핵심
def bfs(queue):
    
    prev = [0]*(n+1)

    while queue:

        u = queue.popleft()

        for v in graph[u]:

            #prev[v] = 0인 경우만 검사하면 됨, prev[v] != 0인 경우는 검사할 필요가 없음
            #간선의 길이가 1이기 때문에 a > u > v로 가나 b > u > v로 가나 다를바가 없다는거임
            if prev[v] == 0: 

                if v == b: #b에 도달하는 경우만 찾으면 되므로 찾는 순간 바로 return

                    prev[b] = u
                    return prev

                else:

                    prev[v] = u
                    queue.append(v)

    
    return prev

n,k = map(int,stdin.readline().split())

A = {}

for i in range(1,n+1):

    s = stdin.readline().rstrip()
    s = int(s,2)
    A[s] = i

graph = [[] for _ in range(n+1)]

#xor을 이용한 비트 뒤집기

#핵심은 bit_a와 해밍거리가 1인 비트만 찾으면 됨
#i번째 비트가 서로 다른 비트인 코드가 bit_b라고 가정한다면, 어떻게 찾아야하는가?
#1과 1을 xor하면 0, 1과 0을 xor하면 1, 0과 1을 xor하면 1, 0과 0을 xor하면 0
#1과 어떤 비트를 xor하면 뒤집히고, 0과 어떤 비트를 xor하면 그대로 나온다는거
#1 << i와 bit_a의 xor한 비트가 존재하는지 검사하면 O(NK)에 가능
for bit_a in A:
    
    a = A[bit_a]
    
    for i in range(k):
        
        bit_b = bit_a ^ (1 << i)
        
        if A.get(bit_b,0) != 0:
            
            graph[a].append(A[bit_b])
            graph[A[bit_b]].append(a)

a,b = map(int,stdin.readline().split())
            
queue = deque([a])

prev = bfs(queue)

if prev[b] == 0:
    
    print(-1)

else:
    
    #prev배열을 찾으면 b에서부터 반대로 역추적 가능
    A = [b]

    u = b

    while 1:
        
        v = prev[u]
        A.append(v)

        if v == a:
            
            break
        
        u = v
    
    for i in range(len(A)-1,-1,-1):
        
        print(A[i],end= ' ')