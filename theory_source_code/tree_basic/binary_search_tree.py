#node class 정의

class Node:
    
    def __init__(self,data):
        
        self.data = data
        self.left = None
        self.right = None

#이진탐색트리 class 정의
class BST:
    
    def __init__(self):
        
        self.root = None
    
    #탐색 연산
    def search(self,target):
        
        #루트부터 탐색을 시작함
        
        now = self.root
        cnt = 0
        
        while now: #루트 노드가 없어질때까지 탐색을 계속
            
            print(now.data) #node 출력
            
            if target == now.data: #목표를 찾았으면
                
                return now
            
            elif target < now.data: #목표가 현재 노드보다 더 작다면
                
                now = now.left  #현재 노드를 왼쪽으로 이동함
            
            elif target > now.data: #목표가 현재 노드보다 더 크다면
                
                now = now.right #현재 노드를 오른쪽으로 이동
            
            cnt += 1 #탐색 횟수?
        
        return now #반복이 끝났는데도 찾는 target이 존재하지 않는 경우
    
    #삽입 연산
    def insert(self,node):
    
        #루트부터 탐색을 시작
        
        now = self.root
        
        if now == None: #루트부터 존재하지 않으면, 바로 삽입하고 return함
            
            self.root = node
            return
        
        while 1: #탐색을 수행하여, 탐색을 실패한 지점에 노드를 삽입함
            
            p = now
            
            #넣고 싶은 데이터 node.data가 현재 node값인 now.data보다 작다면
            if node.data < now.data:
                
                now = now.left #왼쪽으로 이동하고
                
                if not now: #왼쪽으로 갔는데, 왼쪽이 존재하지 않는다면(None)
                    
                    #여기서 p는 왼쪽으로 이동하기 전에 저장해놓은 now이다
                    #왼쪽으로 이동했더니 now가 None이면, 이동하기 전인 p의 왼쪽에
                    #삽입을 하면 된다
                    p.left = node
                    return
            
            #넣고 싶은 데이터 node.data가 현재 node값인 now.data보다 크다면
            #당연히 삽입은 넣고 싶은 데이터가 존재하지 않는다는 것을 보장한 상태에서 수행해야함
            else: 
                
                now = now.right #오른쪽으로 이동함
                
                if not now: #오른쪽으로 이동했더니 오른쪽이 존재하지 않는다면(None)
                
                    #여기서 p는 오른쪽으로 이동하기 전에 저장해놓은 now이다
                    #오른쪽으로 이동했더니 now가 None이면, 이동하기 전인 p의 오른쪽에
                    #삽입을 하면 된다
                    p.right = node
                    return

####################################
bst = BST()

data_list = [9,4,12,3,6,15,13,17] #[9,12,4,6,3,13,15,17]

node_list = [Node(i) for i in data_list]

#삽입
for node in node_list:
    
    bst.insert(node)

#오른쪽
bst.search(17)

#왼쪽
bst.search(3)

"""
9
12
15
17
9
4
3
<__main__.Node at 0x7f541c6d2e10>"""