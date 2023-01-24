from sys import stdin

class Trie:
    
    def __init__(self):
        
        self.head = {}
    
    def add(self,word):
        
        current_node = self.head
        
        for char in word:
            
            if '*' in current_node:
                
                return False

            if char not in current_node:
                
                current_node[char] = {}
            
            current_node = current_node[char]
        
        if current_node != {}:
            
            return False
        
        else:
            
            current_node['*'] = True

            return True

t = int(stdin.readline())

for _ in range(t):
    
    n = int(stdin.readline())

    trie = Trie()

    flag = True

    for _ in range(n):

        phone = stdin.readline().rstrip()

        if flag == False:
            
            continue

        flag = trie.add(phone)
    
    if flag:
        
        print('YES')
    
    else:
        
        print('NO')