class Trie:
    
    def __init__(self):
    
        self.head = {} #문자가 저장되는 Trie
        
    #단어 추가
    def add(self, word):
        
        #현재 노드
        current_node = self.head

        #현재 들어온 단어 word를 문자 char별로 순차적으로 확인

        for char in word:
            
            #현재 노드에 문자가 존재하지 않는다면...
            if char not in current_node:
                
                #현재 노드에 문자 char을 넣어준다
                current_node[char] = {}
            
            #현재 노드를 방금 넣어준 문자 노드로 교체
            #다음에 볼 문자를 현재 문자 노드의 자식 노드에 넣어줄 수 있도록
            current_node = current_node[char]
        
        #모든 문자를 넣었다면 마지막이라는 flag표시
        current_node['*'] = True
    

    #단어 찾기

    def search(self,word):
        
        current_node = self.head

        #찾고자 하는 단어의 문자를 순차적으로 확인

        for char in word:
            
            #현재 노드에 문자가 존재하지 않는다면..
            if char not in current_node:
                
                return False #그 단어는 자료구조에 저장되어 있지 않다
            
            #존재한다면..
            #현재 노드를 그 문자의 노드로 변경해서
            #그 문자의 자식 노드를 확인할 수 있도록
            current_node = current_node[char]
        
        #모든 문자를 순회했더니
        #마지막 flag가 존재한다면..
        if '*' in current_node:
            
            return True
        
        #마지막 flag가 존재하지 않는다면..
        #hello에서 he만 본것처럼.. 단순히 부분문자열로만 존재하고 있다
        else:
            
            return False