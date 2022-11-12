from collections import deque
from sys import stdin

#기본세팅
#사용 편의를 위해 x,y를 y,x로 바꿔줌

n,m,y,x,k = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

order_list = list(map(int,stdin.readline().split()))

#델타배열
#1,2,3,4는 동,서,북,남
delta = [0,[1,0],[-1,0],[0,-1],[0,1]]

#0번을 밑바닥이라고 한다면, 2번이 윗면
#주사위가 남,북으로 구르면 up_down
#주사위가 동,서로 구르면 left_right

up_down = deque([0,0,0,0])
left_right = deque([0,0,0,0])

#시뮬레이션 시작

#이동을 하고 회전시키면, 위,아래의 값을 다른 deque도 그대로 가져가야함
for order in order_list:
    
    #주사위의 좌표 이동

    dx = x + delta[order][0]
    dy = y + delta[order][1]

    #배열의 범위를 벗어나지 않는 경우에만 이동

    if dx >= 0 and dx <= m-1 and dy >= 0 and dy <= n-1:
        
        #동쪽으로 이동하라고 한다면..
        #1번과 3번은 그대로 있지만,
        #left_right가 동쪽으로 움직이고나서 0번 2번을 그대로 가져감
        if order == 1:
            
            left_right.rotate(-1) #동쪽으로 1칸 이동

            #이동한 칸에 쓰인 수가 0이라면..

            if maps[dy][dx] == 0:
                
                maps[dy][dx] = left_right[0] #주사위 바닥면을 맵에 복사
            
            else:
                
                left_right[0] = maps[dy][dx] #주사위 바닥면에 맵 칸을 복사

                maps[dy][dx] = 0 #맵 칸은 0으로

            print(left_right[2]) #윗면 출력


            #다른 deque의 아래 위인 0,2번을 교체
            up_down[0] = left_right[0]
            up_down[2] = left_right[2]
        
        #서쪽으로 이동하라고 하면..
        
        elif order == 2:

            left_right.rotate(1)

            #이동한 칸에 쓰인 수가 0이라면..

            if maps[dy][dx] == 0:
                
                maps[dy][dx] = left_right[0] #주사위 바닥면을 맵에 복사
            
            else:
                
                left_right[0] = maps[dy][dx] #주사위 바닥면에 맵 칸을 복사

                maps[dy][dx] = 0 #맵 칸은 0으로

            print(left_right[2])

            up_down[0] = left_right[0]
            up_down[2] = left_right[2]
        
        #북쪽으로 이동하라고 한다면..
        elif order == 3:

            up_down.rotate(1)

            #이동한 칸에 쓰인 수가 0이라면..

            if maps[dy][dx] == 0:
                
                maps[dy][dx] = up_down[0] #주사위 바닥면을 맵에 복사
            
            else:
                
                up_down[0] = maps[dy][dx] #주사위 바닥면에 맵 칸을 복사

                maps[dy][dx] = 0 #맵 칸은 0으로

            print(up_down[2])

            left_right[0] = up_down[0]
            left_right[2] = up_down[2]
        
        #남쪽으로 이동하라고 한다면..
        else:

            up_down.rotate(-1)

            #이동한 칸에 쓰인 수가 0이라면..

            if maps[dy][dx] == 0:
                
                maps[dy][dx] = up_down[0] #주사위 바닥면을 맵에 복사
            
            else:
                
                up_down[0] = maps[dy][dx] #주사위 바닥면에 맵 칸을 복사

                maps[dy][dx] = 0 #맵 칸은 0으로

            print(up_down[2])

            left_right[0] = up_down[0]
            left_right[2] = up_down[2]
            

        x = dx
        y = dy