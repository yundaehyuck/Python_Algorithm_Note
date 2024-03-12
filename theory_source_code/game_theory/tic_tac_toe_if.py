#주어진 틱택토 게임판이 최종 상태로 가능한가?
def check(s):
    
    line = []
    num = 0

    a = 0 #X의 수
    b = 0 #O의 수
    c = 0 #.의 수

    A = set()
    for i in range(len(s)):
        
        #판에서 X,O,'.'의 수를 센다
        if s[i] == 'X':
            
            a += 1
        
        elif s[i] == 'O':
            
            b += 1
        
        else:
            
            c += 1
            
        A.add(s[i])
        
        #0행, 1행, 2행 각각이 서로 같은지를 조사한다
        if i % 3 == 2:
            
            if len(A) == 1:
                
                A =list(A)
                
                if A[0] == 'X':
                    
                    line.append(False)
                    num += 1
                
                elif A[0] == 'O':
                    
                    line.append(True)
                    num += 1
                
            A = set()
    
    #0열 1열 2열이 서로 같은지를 조사한다
    A = set()
    for i in range(3):
        
        A.add(s[i])
        A.add(s[i+3])
        A.add(s[i+6])

        if len(A) == 1:
            
            A =list(A)
                
            if A[0] == 'X':
                
                line.append(False)
                num += 1
            
            elif A[0] == 'O':
                
                line.append(True)
                num += 1
            
        A = set()
    
    #대각선으로 서로 같은지를 조사한다
    diag = 0
    A = set()
    A.add(s[0])
    A.add(s[4])
    A.add(s[8])

    if len(A) == 1:
        
        A =list(A)
                
        if A[0] == 'X':
            
            o = False
            diag += 1
        
        elif A[0] == 'O':
            
            o = True
            diag += 1
        
    A = set()
    A.add(s[2])
    A.add(s[4])
    A.add(s[6])

    if len(A) == 1:
        
        A =list(A)
                
        if A[0] == 'X':
            
            o = False
            diag += 1
        
        elif A[0] == 'O':
            
            o = True
            diag += 1
    
    #대각선 한 줄이 서로 같은 경우
    if diag == 1:
        
        if o == True: #대각선 한줄이 O로 같다
            
            if a == b: #O와 X의 개수가 서로 같아야한다
            
                return True
            
            else:
                
                return False
        
        else: #대각선 한줄이 X로 같다
            
            if a == (b+1): #X의 개수가 O의 개수보다 1개 더 많다
                
                return True
            
            else:
                
                return False
    
    #가로줄,세로줄에 대한 검사
    
    #두줄이 서로 같은 경우
    if num == 2:

        if len(set(line)) == 2: #XXX, OOO로 되는 경우는 불가능하다

            return False

        else: #XXX,XXX나 OOO,OOO로 서로 같은 경우
        
            #XXX, XXX만 가능하다.
            if line[0] == False and line[1] == False: 
                
                #XXX
                #X??
                #X??으로 하더라도, 게임이 결정될려면 개수도 맞아야한다.
                
                #X가 5개이고 O가 0개이면 불가능한 경우니까
                if a == 5 and b == 4:
                    
                    return True
    
    #가로줄이 1줄이 같거나 세로줄이 1줄로 서로 같은 경우
    elif num == 1:
        
        o = line[0]
        if o == True: #OOO로 서로 같은 경우
            
            if a == b: #O의 개수와 X의 개수가 서로 같아야한다
                
                return True
        
        else: #XXX로 서로 같은 경우
            
            if a == (b + 1): #X의 개수가 O의 개수보다 1개 더 많다
                
                return True
    
    else: #승부가 결정나지 않는 경우, X의 개수가 5개, O의 개수가 4개여야한다.

        if a == 5 and b == 4:
            
            return True
    
    return False