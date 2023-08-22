#DFS를 이용한 bipartite matching
#Kuhn's Algorithm
def bpm(s):
    
    #방문 체크한 s번에서 또 연결을 체크한다면...
    if visited[s] == 1:
        
        return False
    
    #최초로 s번에서 연결을 시도한다면.. 방문체크를 해주고
    visited[s] = 1
    
    #improve technique
    #s와 연결된 모든 v에 대하여...
    for v in graph[s]:
        
        #v가 매칭되어 있지 않다면... s를 v에 매칭시키고 끝내버린다.
        if matching[v] == 0:
            
            matching[v] = s
            
            #s번이 연결에 성공했다면 True
            return True
    
    #s와 연결된 모든 v에 대하여...
    for v in graph[s]:
        
        #v가 매칭되어 있다면, 해당 매칭된 번호 matching[v]로 다시 들어가서 연결을 재조정 
        if bpm(matching[v]):
            
            #연결을 재조정하는데 성공했다면 s를 v에 연결
            matching[v] = s

            #s번은 연결에 성공했으니 True
            return True
    
    #연결에 실패했다면...
    return False

#n: 왼쪽 그룹 정점의 수
#m: 오른쪽 그룹 정점의 수
n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

matching = [0]*(m+1) #오른쪽 그룹이 왼쪽의 어떤 정점들과 매칭되어있는지..

#1번부터 n번까지 정점 i에 대하여..
for i in range(1,n+1):
    
    #0번 원소는 i번과 연결된 정점의 수
    #1번 ~ 나머지 원소는 i번과 연결된 정점 번호
    lines = list(map(int,input().split())) 

    for j in range(1,lines[0]+1):
        
        graph[i].append(lines[j]) #i번 정점들이 어떤 정점들과 연결되어 있는지..

count = 0

#1번부터 n번까지 순회하여 매칭을 시도
for i in range(1,n+1):
    
    visited = [0]*(n+1)
    
    if bpm(i) == True:
        
        count += 1

print()
print(f'최대 매칭 수: {count}')
print()

change = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E'}

for i in range(1,m+1):
    
    if matching[i] != 0:

        print(f'{matching[i]} -> {change[i]}')

"""
4 5
2 1 2
2 1 3
4 2 3 4 5
3 1 2 5

최대 매칭 수: 4

4 -> A
1 -> B
2 -> C
3 -> D
"""