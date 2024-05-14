s = 'black'

current_node = 0

find = True

for c in s:
    
    v = ord(c) - ord('a')

    if trie[current_node][v] == -1:
        
        find = False
        break
    
    current_node = trie[current_node][v]

if find:
    
    end[current_node] = 0