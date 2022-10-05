#이제는 맵에 배치하지도 말아

#약품의 위치는 미생물의 좌표만 알면 바로 알 수 있어

#미생물의 정보를 좌표만 넣으면 바로 알 수 있게 dictionary에 따로 관리

#그러면 n*n 이중 for문 순회하는것도 제거가 될것

T = int(input())

for tc in range(1,T+1):
    
    n,m,k = map(int,input().split())

    before_maps = {}
    
    ##최초 미생물 배치

    for _ in range(k):
        
        y,x,c,d = map(int,input().split())

        #좌표를 key로 해서 미생물의 정보를 바로 가져오도록

        before_maps[(x,y)] = (c,d,c) ##(x,y)에 모인 미생물 군집의 미생물 수의 총합, 움직이는 방향, 군집에 모인 미생물 종류별로 가지는 미생물 수 중 가장 큰 미생물 수
    
    #약품에 위치하면 바꿔야할 방향
    #상 > 하, 하> 상, 좌> 우, 우>좌
    change_dir = {1:2, 2:1, 3:4, 4:3}

    #시뮬레이션 시작

    #상하좌우 델타배열

    delta = [[0,-1],[0,1],[-1,0],[1,0]]

    for _ in range(m): ##m시간만 돌면 되니까

        #이동 후에 배치되는 맵

        after_maps = {}

        ##이제는 n*n 배열을 순회하는게 아니라 dictionary만 순회하면 이동하지 않은 미생물을 찾을 수 있다

        for (x,y),(c,d,max_c) in before_maps.items(): #좌표, 미생물 정보를 나누어서 unpack

            ##이동할 좌표 구하기

            dx = x + delta[d-1][0]
            dy = y + delta[d-1][1]

            ##이제는 map에 배치하는 것이 아니라 0,1,미생물이 존재로 나눌 수는 없다
            ##하지만 좌표만 알면 약품이 존재하는지 아닌지는 알 수 있다
            ##그런데 미생물이 결합하는 위치는 약품이 존재하는 곳에서는 절대로 불가능하다

            ##이동한 위치에 약품이 존재한다면..

            if dx == 0 or dx == n-1 or dy == 0 or dy == n-1:
                
                c = c//2 #미생물 절반 소멸시키고

                if c != 0: ##미생물이 존재한다면...
                    
                    d = change_dir[d] #방향을 바꾸고

                    after_maps[(dx,dy)] = (c,d,c) #이동후 배치하는 map에 저장
            
            else: #약품이 존재하지 않는다면...
                
                ## 약품이 존재하지 않는 위치에는 미생물이 존재하거나, 존재하지 않거나

                ##이동했던 미생물이 존재하거나, 이동하지 않은 미생물이 존재하거나, 아무런 미생물도 존재하지 않거나

                ##하지만 이동후와 이동하기 전을 따로 관리하므로, 애초에 서로 영향을 주지 않기때문에 이동하지 않은 미생물이 존재하는지는 고려할 필요없다

                if (dx,dy) in after_maps.keys(): #이동한 위치에 이동했던 미생물이 존재한다면...
                    
                    ##결합과정을 거쳐야함

                    old_c, old_d, old_max = after_maps[(dx,dy)]

                    if old_max < c: #존재했던 미생물 군집들 중 미생물 수의 최댓값보다 새로 들어온 미생물의 수가 더 크다면
                        
                        old_max = c ##최댓값을 갱신하고

                        old_d = d ##방향도 더 많은 미생물을 가진 미생물 군집 방향으로 갱신하고
                    
                    old_c += c ##미생물 수를 늘리고

                    after_maps[(dx,dy)] = (old_c,old_d,old_max) ##미생물 배치

                
                else: ##이동한 곳에 이동했던 미생물이 존재하지 않는다면
                    
                    after_maps[(dx,dy)] = (c,d,c) ##그냥 이동만 시키면 된다
        
        before_maps = after_maps #다음 시간으로 넘어가기 전에 맵 초기화
    
    ans = 0

    #이제는 미생물 총 수를 셀때 이중 for문을 순회할 필요도 없다
    #dict의 value를 순회하면 바로 미생물 수를 얻는다

    for (c,d,max_c) in after_maps.values():
        
        ans += c

    
    print('#'+str(tc),ans)