#부모번호를 인덱스로 하여 자식 번호를 저장

v = int(input())

tree_left = [0]*(v+1)
tree_right = [0]*(v+1)

link = list(map(int,input().split()))

for i in range(0,2*(v-1),2):
    
    p,s = link[i],link[i+1]
    
    if tree_left[p] == 0: ###왼쪽 자식이 채워지지 않았다면
         
        tree_left[p] = s #현재 s는 왼쪽 자식
        
    else: #왼쪽 자식이 채워졌다면
        
        tree_right[p] = s #현재 s는 오른쪽 자식이다


#13
#1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

########전위순회

def preorder(tree_left,tree_right,node):
    
    print(node,end=' ')
    
    if tree_left[node] != 0 and tree_right[node] != 0:
        
        preorder(tree_left, tree_right, tree_left[node])
        
        preorder(tree_left, tree_right, tree_right[node])
    
    elif tree_left[node] != 0 and tree_right[node] == 0:
        
        preorder(tree_left, tree_right, tree_left[node])
    
    else:
        
        pass

preorder(tree_left,tree_right,1)
#1 2 4 7 12 3 5 8 9 6 10 11 13