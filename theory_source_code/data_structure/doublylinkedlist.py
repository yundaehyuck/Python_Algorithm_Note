#Node class를 만든다

class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.next = None
        self.prev = None


#이중 연결리스트 class를 만든다

class DoublyLinkedList:
    
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.node_num = 0
    

    #원소를 맨 앞에 넣는 메소드
    def push_front(self, new_data):
        
        #새로운 노드를 만든다
        new_node = Node(new_data)

        #새로운 노드의 next값을 현재 head로 변경
        new_node.next = self.head

        #기존 이중연결리스트가 비어있지 않다면..
        if self.head != None:
            
            #현재 head의 prev를 새로운 node로 변경
            self.head.prev = new_node

            #head를 새로운 노드로 변경
            self.head = new_node

            #head로 들어가는 노드의 prev는 없다
            new_node.prev = None
        
        #기존 이중연결리스트가 비어있다면..
        else:
            
            #새로들어온 노드가 head이면서 tail
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
        
        #새로 값이 들어왔으니까
        self.node_num += 1
    

    #원소를 맨 끝 위치에 넣는 메소드
    def push_back(self,new_data):
        
        #새로운 노드를 만든다
        new_node = Node(new_data)

        #새로운 노드의 prev값을 현재 리스트의 tail로 변경
        new_node.prev = self.tail

        #현재 리스트가 비어있지 않다면
        if self.tail != None:
            
            #이전 tail의 next를 새로운 노드로 바꾸고
            self.tail.next = new_node

            #tail을 새로운 노드로 변경
            self.tail = new_node

            #새로운 노드의 next는 없다
            new_node.next = None
        
        #기존 리스트가 비어있다면
        else:
            
            #head와 tail이 새로만든 노드와 동일
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        
        self.node_num += 1
    

    #첫번째 수를 빼면서 동시에 그 수를 반환하는 메소드

    def pop_front(self):
        
        #노드가 없다
        if self.head == None:
            
            print("List is empty")
        
        #노드가 오직 하나
        elif self.head.next == None:
            
            temp = self.head

            #head,tail 모두 삭제하고 노드 수는 0개
            self.head = None
            self.tail = None
            self.node_num = 0

            return temp.data
        
        #노드가 2개이상
        else:
            
            temp = self.head
            
            #temp.next의 prev(현재 head)를 지워주고
            temp.next.prev = None

            #head를 현재 head의 next로 변경
            self.head = temp.next

            #현재 head인 temp의 next를 지워주고
            temp.next = None

            self.node_num -= 1
            return temp.data
    

    #맨 끝에 있는 수를 빼면서 동시에 그 수를 반환

    def pop_back(self):
        
        #노드가 하나도 없다
        if self.tail == None:
            
            print("List is empty")
        
        #노드가 오직 하나
        elif self.tail.prev == None:
            
            temp = self.tail

            #head,tail 모두 삭제, node_num을 0으로
            self.head = None
            self.tail = None
            self.node_num = 0

            return temp.data
        
        #노드가 둘 이상
        else:
            
            temp = self.tail

            #새로 tail이 될 노드의 next값을 지워준다
            temp.prev.next = None

            #tail을 갱신
            self.tail = temp.prev

            #이전 tail이 든 temp의 prev를 제거해서 이전 tail을 완전히 삭제
            temp.prev = None

            #노드 하나 지웠으니 노드 수 하나 감소
            self.node_num -= 1
            return temp.data
    
    #노드의 수를 반환
    def size(self):
        
        return self.node_num
    
    #연결리스트가 비었는지 여부
    def empty(self):
        
        return self.node_num == 0
    
    #첫번째 수를 단순히 반환

    def front(self):
        
        if self.head == None:
            
            print("List is empty")
        
        else:
            
            return self.head.data
    

    #마지막 수를 반환

    def back(self):
        
        if self.tail == None:
            print("List is empty")
        else:
            return self.tail.data


l = DoublyLinkedList()

l.push_front(3)
l.push_front(5)

print(l.front()) #5
print(l.back()) #3

l.push_back(9)
print(l.back()) #9

l.pop_front()
print(l.front()) #3

print(l.size()) #2