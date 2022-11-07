from collections import deque
from sys import stdin

n,k = map(int,stdin.readline().split())

belt = deque(map(int,stdin.readline().split()))

#로봇은 1~n인 곳에만 움직인다
robot = [0]*n

robot = deque(robot)

#시뮬레이션 수행

stage = 1

while 1:
    
    #벨트를 회전시키면서 로봇도 회전시킴

    belt.rotate(1)
    robot.rotate(1)

    if robot[n-1] == 1: ##로봇이 n-1번으로 이동해버리면
        
        robot[n-1] = 0 #로봇을 내린다

    #로봇을 순회해서 이동할 수 있는지 검사하고 로봇을 이동
    #0번째 칸과 n-1번째 칸에는 존재할리 없으니 빼고 검사

    for i in range(n-2,0,-1):
        
        #i번째 칸에 로봇이 존재한다면...
        if robot[i] == 1:
            
            if robot[i+1] == 0 and belt[i+1] >= 1: #다음 칸에 로봇이 존재하지 않고, 내구도가 1 이상
                
                robot[i+1] = robot[i] #i번째 로봇을 옮겨주고
                robot[i] = 0 #i번째 위치는 0으로 만들고
                belt[i+1] -= 1 #이동하면 내구도 1을 감소시킨다
        
        #내리는 위치로 로봇이 이동하면 즉시 내린다.

        if robot[n-1] == 1:
            
            robot[n-1] = 0
    
    #올리는 위치에 로봇이 존재하지 않으면..
    if robot[0] == 0:
        
        #올리는 위치의 내구도가 0이 아니라면, 
        if belt[0] != 0:
            
            #로봇을 올리고
            robot[0] = 1

            belt[0] -= 1 #내구도를 1 감소함
    
    #내구도가 0인 칸이 몇개인지 검사

    zero = 0

    end = False

    for d in belt:
        
        if d == 0:
            
            zero += 1
        
        #내구도가 0인 칸이 k개 이상이면 종료
        if zero >= k:
            
            end = True
            break
    

    if end == True:
        
        break
    
    else:
        
        stage += 1 #종료하지 않으면 stage를 1 증가


print(stage)