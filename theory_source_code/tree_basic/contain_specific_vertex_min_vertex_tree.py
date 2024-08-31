#특정한 정점 V1,V2,...,VK를 모두 포함하는 최소 정점 트리
n,k = map(int,input().split())

tree = [set() for _ in range(n+1)] #정점에 연결된 정점들을 set으로 관리

for _ in range(n-1):
    
    a,b = map(int,input().split())
    tree[a].add(b)
    tree[b].add(a)

V = list(map(int,input().split()))
V = {v:1 for v in V}

#리프 노드를 찾는 방법
#연결된 정점 수가 1개인 정점들이 리프노드
leaf = []

for i in range(1,n+1):
    
    v = tree[i]
    
    if len(v) == 1:
        
        leaf.append(i)

#더 이상 불가능할 때까지 v1,v2,..,vk가 아닌 리프 노드들을 밑에서부터 반복적으로 제거해나감
answer = n

for v in leaf:
    
    if V.get(v,0) == 1:
        
        continue
    
    #트리에 연결된 정점을 set으로 관리하기 때문에
    #.pop()은 set에서 랜덤하게 하나를 제거
    vv = tree[v].pop()
    tree[vv].discard(v) #discard는 set에서 특정 정점 v를 O(1)에 제거

    answer -= 1

    #v를 제거하고 나서 vv가 리프노드가 된다면 leaf에 추가해줌
    if len(tree[vv]) == 1:
        
        leaf.append(vv)
    
print(answer)