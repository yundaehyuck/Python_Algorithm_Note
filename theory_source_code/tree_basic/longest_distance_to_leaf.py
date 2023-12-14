from sys import stdin,setrecursionlimit
setrecursionlimit(200000)

#현재 노드 u에서 가장 먼 자식 노드까지의 거리
#리프 노드까지 쭉 내려간 다음, 그 때 값을 0으로 두고,
#1씩 올리면서 return
#여러 방향으로 내려갈 수 있으므로, 얻은 값의 최댓값으로 갱신해나가기
def dfs(u):
    
    dist = 0

    for v in tree[u]:

        if visited[v] == 0:

            visited[v] = 1
            
            d = dfs(v)

            if dist < d:
                
                dist = d
                
    child[u] = dist

    return dist+1

n,s,d = map(int,stdin.readline().split())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):

    a,b = map(int,stdin.readline().split())

    tree[a].append(b)
    tree[b].append(a)

visited = [0]*(n+1)
child = [0]*(n+1)
visited[s] = 1
dfs(s) #각 노드에서 가장 먼 자식 노드까지 거리를 모두 구한다

count = 0

#가장 먼 자식 노드까지 거리가 d이상인 노드만 방문하면 된다
for i in range(1,n+1):
    
    if child[i] >= d:
        
        count += 1

#d가 매우 커서, 아무 노드도 방문하지 않은 경우 2*count-2 < 0인데, 
#아무 노드도 방문하지 않으면 이동 거리는 0이어야하니..
print(max(2*count-2,0))