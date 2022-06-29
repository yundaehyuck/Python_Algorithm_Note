def solution(begin, target, words):
    
    from copy import deepcopy
    from collections import deque
    
    
    if not(target in words):
        
        return 0
    
    else:
        
        tf_list = deque([[begin,words,0]]) #시작, 탐색리스트, step수 형태로 deque 구성
        
        while 1:
            
            b,word_list,step = tf_list.popleft() #deque에서 하나씩 빼가면서 while 반복문 탐색
            
            for word in word_list:
                
                count = 0
                
                for x,y in zip(b,word):
                    
                    if x != y:
                        
                        count += 1
                    
                    if count >= 2:
                        break
                
                if count == 1:
                    
                    if word == target:
                    
                        return step+1
                    
                    else:
                    
                        copy_word = deepcopy(word_list)

                        copy_word.remove(word) 

                        tf_list.append([word,copy_word,step+1]) #deepcopy를 이용해서 원본은 바꾸지 않고 탐색리스트를 변경시켜 새로운 트리 경로를 생성시킴
