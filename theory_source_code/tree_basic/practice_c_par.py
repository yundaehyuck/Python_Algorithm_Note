#자식번호를 인덱스로 하고 부모번호를 저장

v = int(input())

tree = [0] * (v+1)

link = list(map(int,input().split()))

for i in range(0,2*(v-1),2):
    
    p,s = link[i],link[i+1]

    tree[s] = p

#13
#1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

########전위순회


def preorder(tree,node,v):
    
    print(node,end=' ')

    ##자식 node의 번호를 찾는다

    c_list = []

    for i in range(v):
        
        if tree[i] == node:
            
            c_list.append(i)
    
    #자식 수에 따른 전위순회

    if len(c_list) == 1: #자식이 하나 존재하면
        
        preorder(tree,c_list[0],v)
    
    elif len(c_list) == 2: #자식이 2개 존재하면
        
        preorder(tree,c_list[0],v)
        preorder(tree,c_list[1],v)
    
    else:  #자식이 존재하지 않으면
        
        pass

preorder(tree,1,v+1)
#1 2 4 7 12 3 5 8 9 6 10 11 13