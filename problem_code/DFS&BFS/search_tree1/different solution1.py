def solution(begin, target, words):
    answer = 0
    
    Q = [begin]

    while True:
    
        temp_Q = []
        
        for word_1 in Q:
        
            if word_1 == target:
            
                 return answer
                    
            for i in range(len(words)-1, -1, -1): #pop을 하기 위해 역순으로 순회해서 인덱스가 꼬이지 않도록
            
                word_2 = words[i]
                
                if sum([x!=y for x, y in zip(word_1, word_2)]) == 1: #글자수 하나만 다른것을 탐색하는 방법을 한줄로 깔끔하게
                
                    temp_Q.append(words.pop(i))

        if not temp_Q:
        
            return 0
            
        Q = temp_Q
        
        answer += 1
