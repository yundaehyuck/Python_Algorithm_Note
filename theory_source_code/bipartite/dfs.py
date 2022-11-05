#DFS로 이분 그래프를 판별하는 알고리즘

#이분그래프 판별

def dfs(v,group):
    
    visited[v] = group #방문한 정점에 그룹 할당

    for i in graph[v]: #현재 정점과 인접한 정점을 순회하여..
        
        if visited[i] == 0: #방문하지 않은 정점이라면...
            
            if not dfs(i,-group): #서로 다른 그룹을 부여하면서 방문을 시도
                
                return False # 재귀적 호출 결과가 False라면... 이분 그래프가 아니다

        elif visited[i] == visited[v]: #이미 방문한 정점인데, 현재 정점과 그룹이 같다면

            return False #이분 그래프가 아니다

    return True #모든 정점을 순회했더니 이상이 없으면 이분 그래프이다 

#정점의 수와 간선의 수
v,e = map(int,input().split())

#정점이 1~v인 그래프 생성
graph = [[] for _ in range(v+1)]

#방문한 정점을 체크하는 배열
visited = [0]*(v+1)

#간선을 입력받아 그래프 생성

for _ in range(e):
    
    a,b = map(int,input().split())

    graph[a].append(b)
    graph[b].append(a) #무방향 그래프

bipartite = True #이분 그래프 여부

#연결그래프, 비연결그래프를 모두 고려하여
#모든 정점을 순회하면서
for i in range(1,v+1):
    
    #아직 방문한 정점이 아니라면 시작 정점으로 삼는다
    if visited[i] == 0:
        
        bipartite = dfs(i,1)
        
        #이분 그래프가 아니라면, 반복을 종료
        if not bipartite:
            
            break

print(bipartite)
"""
9 11
1 2
2 3
3 4
3 5
4 6
5 6
5 7
7 8
6 8
9 8
5 9
True
"""