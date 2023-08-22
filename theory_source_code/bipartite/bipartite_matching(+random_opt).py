#DFS를 이용한 bipartite matching
#Kuhn's Algorithm
def bpm(s):
    
    #방문 체크한 s번에서 또 연결을 체크한다면...
    if visited[s] == 1:
        
        return False
    
    #최초로 s번에서 연결을 시도한다면.. 방문체크를 해주고
    visited[s] = 1
    
    #s와 연결된 모든 v에 대하여...
    for v in graph[s]:
        
        #v가 매칭되어 있지 않거나
        #v가 매칭되어 있다면, 해당 매칭된 번호 matching[v]로 다시 들어가서 연결을 재조정 
        if matching[v] == 0 or bpm(matching[v]):
            
            #매칭되어 있지 않거나, 연결을 재조정하는데 성공했다면 s를 v에 연결
            matching[v] = s

            #s번은 연결에 성공했으니 True
            return True
    
    #연결에 실패했다면...
    return False

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

matching = [0]*(m+1)

for i in range(1,n+1):
    
    lines = list(map(int,input().split()))

    for j in range(1,lines[0]+1):
        
        graph[i].append(lines[j])

#improve technique
#arbitrary matching
#simple heuristic algorithm
random_visited = [0]*(n+1)

for i in range(1,n+1):
    
    for s in graph[i]:
        
        if matching[s] == 0:
            
            matching[s] = i
            random_visited[i] = 1
            break

#bipartite matching
count = 0

#1번부터 n번까지 매칭을 시도
for i in range(1,n+1):
    
    #i번에서 이미 위에서 수행한 랜덤매칭이 수행되어 있다면, 넘겨준다.
    if random_visited[i] == 1:
        continue
    
    #랜덤매칭이 되어있지 않다면, i번에 대해 bipartite matching을 시도
    visited = [0]*(n+1)
    bpm(i)

#matching배열을 모두 순회하여, 
#정점 번호는 1번부터 시작하니 matching[i]가 0이 아니면 매칭이 된 상태이다.
for i in range(1,m+1):
    
    if matching[i] != 0:
        
        count += 1
        
print(count)