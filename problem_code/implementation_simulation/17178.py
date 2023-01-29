from sys import stdin

n = int(stdin.readline())

lines = []

orders = []

for _ in range(n):
    
    line = stdin.readline().rstrip().split()

    lines.append(line)

    for m in line:
        
        #- 기준으로 split
        a,b = m.split('-')
        
        #알파벳, 숫자형으로 바꾼 숫자, 합체된 번호를 넣어준다
        orders.append([a,int(b),m])

#정렬하면 알파벳 기준으로 사전순이 앞으로
#알파벳이 동일하면 숫자가 작은게 앞으로
#동일한 티켓은 없으니 마지막 m은 정렬에 영향 없다
orders.sort()

wait = []

num = 0

for line in lines:
    
    for m in line:
        
        success = False

        if orders[num][2] == m:
            
            success = True
            num += 1

        while wait:
            
            if wait[-1] == orders[num][2]:
                
                wait.pop()
                num += 1
            
                if success == False:

                    if orders[num][2] == m:

                        success = True
                        num += 1
            
            else:
                
                break
        
        if success == False:
                
            wait.append(m)
        

if wait == []:
    
    print('GOOD')

else:
    
    print('BAD')