s = input()

n = len(s)

#현재 오리 상태가 0이면 q를 받아야하고, 1이면 u를 받아야하고 2면 a를 받아야하고...
order = {'q':0,'u':1,'a':2,'c':3,'k':4}

if s[0] != 'q':
    
    print(-1)

else:
    
    #오리를 담은 배열
    #각 오리는 0(k),1(q),2(u),3(a),4(c) 상태를 가진다
    
    answer = [1]
    no = False #불가능한 문자열 여부

    for i in range(1,n):
        
        if s[i] == 'q': #q가 나온다면.. 이미 가지고 있는 오리 배열을 순회
            
            find = False

            for j in range(len(answer)):
                
                #이미 다 운 오리가 있다면.. 그 오리가 새로 운다고 보는게 유리하다
                if answer[j] == 0:
                    
                    answer[j] = 1
                    find = True
                    break
                    
             #가지고 있는 오리 중에 다 운 오리가 없다면.. 새로운 오리가 울었다고 보는게 맞다
            if find == False:
                
                answer.append(1)
        
        else:

            find = False
            
            #q 이외의 문자가 온다면...
            #오리들의 상태를 순회해서 현재 문자에 맞는 오리가 있는지 검사

            for j in range(len(answer)):
                
                if answer[j] == order[s[i]]: #있다면 그 오리에 배정하면 끝
                    
                    answer[j] += 1

                    if answer[j] == 5: #배정하다가 5가 된다면 0으로 바꿔주고
                        
                        answer[j] = 0

                    find = True
                    break
                    
            #발견하지 못하면 올바른 문자열이 아니다
            if find == False:
                no = True
                break
    
    if no: #애초에 올바르지 않은 문자열이라면...
        
        print(-1)
    
    else:
        
        #오리 배열을 순회해서..
        
        c = 0

        for i in range(len(answer)):
            
            if answer[i] != 0: #올바른 문자열이라면 모든 원소가 0이어야한다
                
                c = -1
                break
            
            else:
                
                c += 1
        
        print(c)