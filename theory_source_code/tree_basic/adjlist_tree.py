#트리의 인접리스트 표현

v = int(input())

tree = [[] for _ in range(v+1)]

link = list(map(int,input().split()))

#간선의 수가 v-1개이므로
#나열된 번호는 총 2(v-1)개

#0,2,4,6,...,2(v-1)-1까지 순회하고 싶음

for i in range(0,2*(v-1),2):
    
    p,s = link[i], link[i+1]
    
    tree[p].append(s)


#13
#1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

########전위순회

def preorder(tree,node):
    
    print(node, end=' ')
    
    if tree[node]:
        
        try:
            
            preorder(tree,tree[node][0])
        
        except:
            
            pass
        
        try:
            
            preorder(tree,tree[node][1])
        
        except:
            
            pass
            
preorder(tree,1)
1 2 4 7 12 3 5 8 9 6 10 11 13

def preorder(tree,node):
    
    print(node,end=' ')
    
    if tree[node]:
        
        if len(tree[node]) == 1:
            
            preorder(tree,tree[node][0])
        
        else:
            
            preorder(tree,tree[node][0])
            preorder(tree,tree[node][1])

preorder(tree,1)
1 2 4 7 12 3 5 8 9 6 10 11 13