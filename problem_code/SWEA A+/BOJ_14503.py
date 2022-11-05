from sys import stdin

def search_left(r,c,d,n,m,delta,maps,clean):

    #해당 방향으로 이동해보고
        
    dr = r + delta[d][0]
    dc = c + delta[d][1]
        
    #벽이 아니고, 청소할 공간이 존재한다
    if maps[dr][dc] == 0 and clean[dr][dc] == 0:
        
        return 1
                
    #청소할 공간이 존재하지 않음
    else:
        return 0
    

def simulation(r,c,d,change_left,clean,delta,maps):
    
    clean_count = 0

    while 1:
        
        #현재 위치 청소

        if clean[r][c] == 0: #아직 청소하지 않았다면,

            clean[r][c] = 1 #청소했다고 명시하고
            clean_count += 1 #청소한 구역의 수 counting

        #왼쪽 방향에 청소할 공간 존재하는지 탐색함

        examine_direction = 0  #어느 방향, 몇번이나 탐색했는지,

        while 1:
            
            examine_direction += 1

            #왼쪽 방향전환

            change_d = change_left[d]
            
            #탐색해보기
            find = search_left(r,c,change_d,n,m,delta,maps,clean)

            if find == 1: #청소할 공간이 존재함
                
                r = r + delta[change_d][0]
                c = c + delta[change_d][1] #그 방향으로 전진
                d = change_d
                break
        
            if examine_direction == 4: #모두 청소가 되어 있는 경우
                
                #한칸 후진
                r = r - delta[change_d][0]
                c = c - delta[change_d][1]
                
                examine_direction = 0
            
                if maps[r][c] == 1: #뒤쪽 후진했더니 벽이면..
                    
                    return clean_count #작동 멈추기
                
            d = change_d

n,m = map(int,stdin.readline().split())

r,c,d = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

#청소 했는지 안했는지 여부를 나타내는 배열
clean = [[0]*m for _ in range(n)]

#0:북,1:동,2:남,3:서

delta = [[-1,0],[0,1],[1,0],[0,-1]]

change_left = {0:3,1:0,2:1,3:2}

clean_count = simulation(r,c,d,change_left,clean,delta,maps)

print(clean_count)