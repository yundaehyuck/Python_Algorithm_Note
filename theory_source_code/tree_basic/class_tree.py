class Node:
    
    def __init__(self,data):
        
        self.data = data
        self.left = None
        self.right = None

#Node 클래스로 트리 생성

root = Node(1)

#root의 left, right node를 만드는 방법

root.left = Node(2)
root.right = Node(3)

###root.left = 2라고만 하면... 그냥 데이터 2를 넣는거고 root.left = Node(2)를 하면 Node(2)라는 인스턴스를 넣는거. 클래스 안에 클래스 안에 클래스 안에... 재귀적으로 들어감

#그러면 4와 5를 2번 노드에 붙이는 방법

root.left.left = Node(4)
root.left.right = Node(5)