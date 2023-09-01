#find strongly connected component
#kosaraju's algorithm

from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)

#첫번째 DFS
def dfs1(s,graph,visited):

    global num

    for u in graph[s]:
        
        #아직 방문하지 않은 정점이면, 방문 체크를 하고 다음 정점으로 이동
        
        #주의! 
        #한번의 visitied로 해결해야하기 때문에, dfs1 끝나고 나서 visited[u] = 0으로 하면 안된다.
        if visited[u] == 0:
        
            visited[u] = 1
            dfs1(u,graph,visited)
    
    #s에서 더 이상 이동할 수 없는 경우
    #현재 num값을 s에 기록한다.
    #중요한 점은 num_list[num] = s로 기록해야한다. 
    #두번째 DFS에서 num값이 큰 정점부터 시작해야하는데, num_list[s] = num으로 하면 정렬해야하지만
    #num_list[num] = s로 한다면 index의 역순으로 순회하기만 하면 되니까 간단해짐
    num_list[num] = s
    num += 1

#두번째 DFS
def dfs2(s,visited,graph):

    stack = [s]

    scc = []

    while stack:

        u = stack.pop()

        if visited[u] == 1:

            continue

        visited[u] = 1
        scc.append(u) #s부터 시작해서 방문하는 정점 u마다 SCC를 이루므로 append해준다.

        for w in graph[u]:

            if visited[w] == 0:

                stack.append(w)

    return scc,visited #한번의 visited로 해결해야하므로, 재활용해야함

#kosaraju algorithm
def kosaraju(v,graph,reverse):
    
    #첫번째 DFS
    #num_list를 만든다.
    visited = [0]*(v+1)

    for i in range(1,v+1):

        if visited[i] == 0:

            visited[i] = 1
            dfs1(i,graph,visited)
    
    #두번째 DFS
    #모든 SCC를 찾는다.
    visited = [0]*(v+1)

    scc_list = []
    
    #num_list의 index의 역순으로 순회하면 num_list[i]는 num값이 큰 정점 번호를 나타낸다.
    for i in range(v,0,-1):

        if visited[num_list[i]] == 0:

            scc,visited = dfs2(num_list[i],visited,reverse) #주의: 반전된 그래프를 사용해야한다.
            scc.sort() #문제에서 오름차순으로 정렬해서 출력하라했으므로,
            scc_list.append(scc)

    return scc_list

v,e = map(int,stdin.readline().split())

graph = [[] for _ in range(v+1)]
reverse = [[] for _ in range(v+1)]

for _ in range(e):

    x,y = map(int,stdin.readline().split())

    graph[x].append(y)
    reverse[y].append(x) #두번째 dfs에 필요하므로 반전된 그래프를 미리 만든다

num = 1
num_list = [0]*(v+1)

scc_list = kosaraju(v,graph,reverse)

scc_list.sort() #문제에서 오름차순으로 출력하라고 해서

print(len(scc_list))

for scc in scc_list:

    scc.append(-1)

    print(' '.join(map(str,scc)))