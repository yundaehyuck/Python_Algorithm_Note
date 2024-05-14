#배열을 이용한 trie의 단어 삽입

n = int(input())

S = input().split()

L = 0 #가능한 모든 문자의 개수, 가능한 노드 번호의 최댓값

for s in S:
    
    L += len(s)

#trie[문자열 집합 내에 존재하는 모든 문자의 최대 개수][문자의 종류]
trie = [[-1]*26 for _ in range(L+1)]
end = [0]*(L+1)

num = 1 #아직까지 사용하지 않은 노드 번호(삽입할때 사용할 노드 번호)

for s in S:
    
    current_node = 0 #현재 노드 번호

    for c in s:
        
        v = ord(c) - ord('a') #현재 문자
        
        #현재 노드 번호 current_node의 자식 trie[current_node]
        #trie[current_node][v] = -1이라는 것은,
        #current_node의 자식으로 현재 문자 v가 없다는 것
        if trie[current_node][v] == -1:
            
            #현재 노드의 자식에 현재 문자 v가 없으면
            #아직 사용하지 않은 노드 번호 num을 만들어주고, num += 1해서 다음에 사용
            trie[current_node][v] = num
            num += 1
        
        #v를 삽입하고, v의 노드 번호로 이동
        current_node = trie[current_node][v]
    
    end[current_node] = 1 #모든 문자를 삽입했으면, 끝났다는 표시
            
print(trie)
print(end)