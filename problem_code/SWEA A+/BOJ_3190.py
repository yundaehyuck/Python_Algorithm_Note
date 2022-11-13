from collections import deque
from sys import stdin

#보드 크기
n = int(stdin.readline())

#사과 개수
k = int(stdin.readline())

maps = [[0]*n for _ in range(n)]

for _ in range(k):
    
    #사과 위치는 행,열
    y,x = map(int,stdin.readline().split())

    maps[y-1][x-1] = 1 #사과를 배치

L = int(stdin.readline())

#방향전환 리스트
dir_list = deque()

for _ in range(L):
    
    x,c = stdin.readline().rstrip().split()

    dir_list.append((int(x),c)) #증가하는 순서대로 주어진다

#뱀의 자취를 deque에 순서대로 담는다
#0번이 뱀의 꼬리
#-1번이 뱀의 머리
snake = deque([(0,0,0)])

#우, 좌 , 하, 상
delta = [[1,0],[-1,0],[0,1],[0,-1]]

#방향전환 사전

change_dir = {0:{'L':3, 'D':2}, 1:{'L':2, 'D':3}, 2:{'L':0, 'D': 1}, 3:{'L':1,'D':0}}

visited = [[0]*n for _ in range(n)]

visited[0][0] = 1 #최초 맨 좌측에 위치

#시뮬레이션
t = 1 #시작시간

while 1:
    
    x,y,d = snake.pop()

    #머리를 다음칸에 위치시킨다

    dx = x + delta[d][0]
    dy = y + delta[d][1]

    #x,y,d는 꼬리(몸통)가 되니까 다시 꼬리(몸통)는 deque에 넣어주고
    snake.append((x,y,d))

    if dx >= 0 and dx <= n-1 and dy >= 0 and dy <= n-1: #배열의 범위를 벗어나지 않는 경우,
        
        if visited[dy][dx] == 1: #자기 자신의 몸과 부딪힌다면?

            break #게임 종료
        
        else: #자기 자신의 몸과 부딪히지 않는다면...
            
            visited[dy][dx] = 1

            if maps[dy][dx] == 1: #맵에 사과가 존재한다면...
                
                maps[dy][dx] = 0 #사과 먹고

            else: #사과가 존재하지 않는다면...
                
                t_a,t_b,tail_d = snake.popleft() #꼬리를 한칸 줄이고

                visited[t_b][t_a] = 0 #꼬리를 줄였으니, 자취에서 제거
    
    else: #배열의 범위를 벗어나는 경우
        
        break #게임 끝

    
    #방향 전환 여부
    turn = False

    for i in range(L): 
        
        if dir_list[i][0] == t: #방향전환 시간이 현재 시간과 일치하는 경우를 만나면..
            
            d = change_dir[d][dir_list[i][1]]
            turn = True
            break
    
    if turn:
        
        dir_list.popleft() #증가하는 시간 순이므로, 최초 turn을 하면, 사용한 원소이므로 제거
        L-=1 #원소 1개 감소했으므로
    

    snake.append((dx,dy,d)) #머리를 넣어주고

    t += 1 #다음 시간으로 이동


print(t)