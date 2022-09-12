#class 정의
class Node:
    
    def __init__(self,data):
        
        self.data = data
        self.left = None
        self.right = 

v = int(input())

#가능한 node 번호 instance를 모두 리스트에 담아둔 다음에

#0번부터 v까지 모두 넣어
#0은 필요없는것 같기는 한디
tree = [Node(i) for i in range(v+1)]

link = list(map(int,input().split()))

for i in range(0,2*(v-1),2):
    
    p,s = link[i],link[i+1]
    
    ##### 반복문을 활용해서 instance에 붙여준다
    
    if tree[p].left:      ##tree[p] === Node(p)이고 이것의 left 속성이 존재한다면..
        
        tree[p].right = tree[s] ## 오른쪽 자식이 s이므로, tree[s] == Node(s)를 불러와 붙여준다
    
    else:  ##왼쪽 자식이 존재하지 않는다면..
        
        tree[p].left = tree[s] ### 왼쪽 자식이 s이므로, tree[s] == Node(s)를 불러와 왼쪽에 붙여줌



#13
#1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

########전위순회


def preorder(node):
    
    if node:
        
        print(node.data,end=' ')
        preorder(node.left)
        preorder(node.right)


preorder(tree[1])
#1 2 4 7 12 3 5 8 9 6 10 11 13 