while 1:
    
    try:

        s = input()

        answer = [0,0,0,0]

        for c in s:
            
            if c.islower():
                
                answer[0] += 1
            
            elif c.isupper():
                
                answer[1] += 1
            
            elif c.isdigit():
                
                answer[2] += 1
            
            elif c == ' ':
                
                answer[3] += 1

        print(*answer)
    
    except:
        
        break