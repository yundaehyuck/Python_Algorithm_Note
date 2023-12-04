#트리의 경로 유일성
#s에서 e로 이동하는 트리의 경로를 찾는 방법
from sys import stdin

#DFS로 u에서 v로 이동할때, v가 u에서 왔다는것을 parent[v] = u로 표시
def find_path(u,target):

    visited = [0]*(n+1)
    stack = [u]
    parent = [-1]*(n+1)

    while stack:

        u = stack.pop()

        if visited[u] == 1:

            continue

        visited[u] = 1

        for v in tree[u]:

            if visited[v] == 0:

                if v == target:

                    parent[v] = u

                    return parent

                parent[v] = u
                stack.append(v)

n,s,e = map(int,stdin.readline().split())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):

    a,b = map(int,stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

path = find_path(s,e)

#경로 역추적
#도달 정점 e부터 시작해서 parent[e] = v이면 v > e이므로 [v,e]
#e를 v로 갱신하고 parent[v] = u이면 u > v > e이므로 [u,v,e]
#이런 식으로 반복문으로 찾는다
win_path = [e]

t = e

while path[t] != -1:

    p = path[t]
    win_path.append(p)

    t = p

#path = [e,an-1,an-2,...,a2,s] 형태로 거꾸로 되어있다
first = True

j = 1
for i in range(len(win_path)-1,-1,-1):
    
    if j % 2 == 0: #후공이 움직여야하는 정점 v

        v = win_path[i]
        
        if v == e: #이미 도달 정점이라면 조사할 필요가 없다
            continue
        
        #tree가 양방향으로 구현되어 있어서
        #tree[v]에는 부모 정점 u가 포함되어 있다
        #u 이외에도 다른 정점 v1,v2,.. 2개 이상이 포함(총 3개 이상)되어 있다면 후공의 승리
        #u 이외에도 다른 정점이 v1으로 1개라면 선공의 승리 가능성이 있다
        if len(tree[v]) >= 3:
            
            first = False
            break    
    j += 1

if first:
    
    print('First')

else:
    
    print('Second')