#정점 수와 간선이 주어질때 트리로 바꾸는 방법

def make_tree(current,parent): #현재 노드, 해당 노드의 부모 노드
    
    for node in edges[current]: #현재 노드와 연결된 노드들을 순회하여..
        
        if node != parent: #연결된 노드가 현재 노드의 부모가 아니라면...
            
            tree[current].append(node) #그 노드는 현재 노드의 자식 노드이다.
            make_tree(node,current)
            
n = int(input())

tree = [[] for _ in range(n+1)]
edges = [[] for _ in range(n+1)]

for _ in range(n-1):
    
    u,v = map(int,input().split())

    edges[u].append(v)
    edges[v].append(u)

make_tree(5,-1) #루트는 5번이고 루트의 부모는 없다(-1)

print(tree)

"""
9
1 3
4 3
5 4
5 6
6 7
2 3
9 6
6 8
[[], [], [], [1, 2], [3], [4, 6], [7, 9, 8], [], [], []]
"""