from sys import stdin

def air_clean(x,y,air_y,after_dust_dict,mode,delta,i):
    
    #움직일 먼지

    air_dust = after_dust_dict.get((x,y),0)

    #최초 위치는 0으로 만들어 준다

    after_dust_dict[(x,y)] = 0

    while 1:

        if mode == 0:
            
            while 1:

                dx = x + delta[mode][0]
                dy = y + delta[mode][1]
                
                if dx <= c-1:

                    temp = after_dust_dict.get((dx,dy),0) #움직여야하는 자리의 먼지를 임시 저장해두고

                    after_dust_dict[(dx,dy)] = air_dust
                
                else: ##범위를 벗어나는 경우..
                    
                    mode = 1 #위쪽으로 움직이도록
                    
                    break #움직이지 않고
                

                air_dust = temp #다음에 움직여야할 먼지 양
                
                x = dx
                y = dy
            
        
        elif mode == 1: #위쪽 혹은 아래쪽으로 움직이는 단계
            
            while 1:
                
                dx = x + delta[mode][0]
                dy = y + delta[mode][1]

                if i == 0:
                    
                    if dy >= 0:
                    
                        temp = after_dust_dict.get((dx,dy),0)

                        after_dust_dict[(dx,dy)] = air_dust
                    
                    else:
                        
                        mode = 2
                        break

                
                else:
                    
                    if dy <= r-1:
                        
                        temp = after_dust_dict.get((dx,dy),0)

                        after_dust_dict[(dx,dy)] = air_dust
                        
                    else:
                        
                        mode = 2 #왼쪽으로 움직이는 단계
                        break
                
                air_dust = temp

                x = dx
                y = dy
        
        elif mode == 2: #왼쪽으로 움직이는 단계
            
            while 1:
                
                dx = x + delta[mode][0]
                dy = y + delta[mode][1]

                if dx >= 0:
                    
                    temp = after_dust_dict.get((dx,dy),0)

                    after_dust_dict[(dx,dy)] = air_dust
                
                else:
                    
                    mode = 3
                    break
                
                air_dust = temp

                x = dx
                y = dy
        
        elif mode == 3: #위쪽 혹은 아래쪽으로 움직이는 단계

            
            while 1:
                
                dx = x + delta[mode][0]
                dy = y + delta[mode][1]

                if i == 0:

                    if dy < air_y:
                        
                        temp = after_dust_dict.get((dx,dy),0)

                        after_dust_dict[(dx,dy)] = air_dust
                    
                    elif dy == air_y:
                        
                        return after_dust_dict
                
                else:
                    
                    if dy > air_y:
                        
                        temp = after_dust_dict.get((dx,dy),0)

                        after_dust_dict[(dx,dy)] = air_dust
                    
                    elif dy == air_y:
                        
                        return after_dust_dict
                                
                air_dust = temp

                x = dx
                y = dy
    


r,c,t = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(r)]

##미세먼지와 공기청정기를 찾는다

dust_dict = {}
air_list = []

for y in range(r):
    
    for x in range(c):
        
        if maps[y][x] >= 1:
            
            dust_dict[(x,y)] = maps[y][x]
        
        elif maps[y][x] == -1:
            
            air_list.append((x,y))


delta = [[0,1],[1,0],[0,-1],[-1,0]]

#시뮬레이션 시작

for _ in range(t):
    
    #미세먼지 확산단계

    after_dust_dict = {}

    for (x,y),dust in dust_dict.items():
        
        diff_count = 0 #확산되는 수

        diffusion = dust//5 #확산되는 양

        if diffusion != 0: #확산되는 양이 0이면.. 확산이 안일어남

            for ni,nj in delta:
                
                dx = x + ni
                dy = y + nj
                
                #확산 범위를 벗어나는지, 공기청정기가 있는지

                if dx >= 0 and dx <= c-1 and dy >= 0 and dy <= r-1 and maps[dy][dx] != -1: 
                    
                    diff_count += 1 #확산이 일어났고

                    after_dust_dict[(dx,dy)] = after_dust_dict.get((dx,dy),0) + diffusion
        
        #하나의 미세먼지가 확산이 끝나면 현재 자리에 남아있는 양을 체크함

        remain = dust - (diffusion * diff_count)

        after_dust_dict[(x,y)] = after_dust_dict.get((x,y),0) + remain

    #공기청정기 단계

    air_delta = [[[1,0],[0,-1],[-1,0],[0,1]],[[1,0],[0,1],[-1,0],[0,-1]]]

    for i in range(2):

        x = air_list[i][0]+1
        y = air_list[i][1]

        air_y = air_list[i][1]

        after_dust_dict = air_clean(x,y,air_y,after_dust_dict,0,air_delta[i],i)
    
    dust_dict = after_dust_dict #다음 단계로 넘어가기 전 초기화

#모든 시뮬레이션이 끝나면

print(sum(dust_dict.values()))