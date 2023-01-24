from sys import stdin

class Trie:
    
    def __init__(self):
        
        self.head = {}
    
    def add(self,word):
        
        current_node = self.head

        name = []
        end = False

        for char in word:
            
            if char not in current_node:
                
                current_node[char] = {}

                if end == False:

                    name.append(char)
                    end = True

            current_node = current_node[char]

            if end == False:
                
                name.append(char)
        
        current_node['*'] = True

        return ''.join(name)

n = int(stdin.readline())

nicknames = []
count_dict = {}

trie = Trie()

for _ in range(n):
    
    name = stdin.readline().rstrip()

    nicknames.append(name)
    count_dict[name] = count_dict.get(name,0) + 1

    if count_dict[name] == 1:

        print(trie.add(name))
    
    else:
        
        print(trie.add(name)+str(count_dict[name]))