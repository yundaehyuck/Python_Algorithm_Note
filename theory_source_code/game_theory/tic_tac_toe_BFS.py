#x가 먼저 시작할때 틱택토 게임의 최종상태로 가능한 모든 경우를 찾는 방법

from collections import deque
from sys import stdin

#i번째 칸에 두었을때 게임이 끝났는가?
#i번째 칸을 중심으로 가로, 세로, 대각선 중 한줄(3개)이라도 같으면 게임 끝
def check(state,i):
    
    #row
    if i == 0 or i == 1 or i == 2:
        
        if state[0] == state[1] and state[1] == state[2]:

            return True

    elif i == 3 or i == 4 or i == 5:

        if state[3] == state[4] and state[4] == state[5]:

            return True

    else:

        if state[6] == state[7] and state[7] == state[8]:

            return True
    
    #col

    if i == 0 or i == 3 or i == 6:
        
        if state[0] == state[3] and state[3] == state[6]:
            
            return True
    
    elif i == 1 or i == 4 or i == 7:
        
        if state[1] == state[4] and state[4] == state[7]:
            
            return True
    
    else:
        
        if state[2] == state[5] and state[5] == state[8]:
            
            return True
    
    #diag

    if i == 0 or i == 8:
        
        if state[0] == state[4] and state[4] == state[8]:
            
            return True
    
    elif i == 2 or i == 6:

        if state[2] == state[4] and state[4] == state[6]:

            return True
    
    elif i == 4:
        
        if state[0] == state[4] and state[4] == state[8]:
            
            return True
        
        elif state[2] == state[4] and state[4] == state[6]:
            
            return True
    
    return False
  
queue = deque([(['.']*9,'X')]) #첫 시작은 X

total = {} #X가 먼저 두었을 때 최종 게임판으로 가능한 것들

next_turn = {'X':'O', 'O':'X'}

while queue:
    
    state,turn = queue.popleft()

    find = False #현재 게임판에서 수를 둘 수 있는가?

    for i in range(9): #게임판의 상태를 순회해서 둘 수 있는 곳 '.'을 찾는다

        if state[i] == '.':

            find = True        
            dstate = state[:]
            dstate[i] = turn #현재 사람이 두고

            f = check(dstate,i) #게임이 끝났는지 검사

            if f == True:
                
                total[''.join(dstate)] = 1 #게임이 끝났다면 최종상태가 된다
            
            else:
                
                queue.append((dstate,next_turn[turn])) #끝나지 않았다면 큐에 넣는다
    
    if find == False: #더 이상 둘 수 있는 곳이 없어서 무승부난 경우
        
        total[''.join(state)] = 1
    
while 1:
    
    s = stdin.readline().rstrip()
    
    if s == 'end':
        
        break
        
    if total.get(s,0) == 0:
        
        print('invalid')
    
    else:
        
        print('valid')