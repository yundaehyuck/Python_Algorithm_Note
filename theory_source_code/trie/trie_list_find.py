s = 'black'

current_node = 0 #root인 0번 노드부터 시작

no = False

for c in s:
    
    v = ord(c) - ord('a')
    
    #현재 노드의 자식 trie[current_node]중 문자 c가 존재하는지 체크
    if trie[current_node][v] == -1:
        no = True
        break #존재하지 않는다면 바로 반복문 탈출
    
    #존재한다면 다음 자식 노드 trie[current_node][v]로 이동
    current_node = trie[current_node][v]

if no:
    
    print('NO')

else:
    
    #마지막으로 도달한 노드 current_node가 실제로 끝난 노드인지 검사
    if end[current_node] == 1:
    
        print('YES')
    
    else:
        
        print('NO')