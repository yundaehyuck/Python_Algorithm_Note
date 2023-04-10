from sys import stdin

s = stdin.readline().rstrip()

len_s = len(s)

#일차항이 존재하는 지 검사
find = False

for i in range(len_s):
    
    if s[i] == 'x':
        
        find = True
        break

#일차항이 없다면, 미분은 0
if find == False:
    
    print(0)

#일차항이 있다면,
else:
    
    #0번 원소가 x라면.. 계수는 1
    if i == 0:
        
        print(1)
    
    #1번 원소가 x라면...
    elif i == 1:
        
        #"-x+a"같은 경우
        if s[0] == '-':
            
            print(-1)
        
        #"bx+a"같은 경우
        else:
            
            print(s[0])
    
    #2번 이후에 x가 존재한다면...
    elif i >= 2:
        
        num = s[:i]
        
        #먼저 -로 split해보고
        num_list = num.split('-')
        
        #["","3000"]이나 ["","300","","200"]이나 ["200",""]같은 경우...
        if len(num_list) >= 2:
            
            #-1번에 x의 계수가 존재하는데... ''이라면 -1
            if num_list[-1] == '':
                
                print(-1)
            
            #''이 아니라면, -를 붙여서 출력
            else:
                
                print(-int(num_list[-1]))
        
        #-로 split해도 길이가 1이라면...
        elif len(num_list) == 1:
            
            #["300+200"]이나 ["300+"]같은 경우이다..
            num_list = num_list[0].split('+')
            
            #["300","","200"]이나 ["300",""] 같은 경우..
            if len(num_list) >= 2:
                
                #-1번 원소에 x의 계수가 있는데.. ''이라면.. 1
                if num_list[-1] == '':
                    
                    print(1)
                
                #''이 아니라면... -1번 원소를 그대로 출력
                else:

                    print(num_list[-1])
            
            #["1000"]같은 경우 +로 split해도 소용없다.
            elif len(num_list) == 1:
                
                #0번 원소를 그대로 출력
                print(num_list[0])