##직관적인 시뮬레이션
##탐색 범위를 줄여 최적화

T = int(input())

for tc in range(1,T+1):
    
    n = int(input())

    before_maps = {}  ##시뮬레이션 시작 전에 배치된 원자 지도

    for _ in range(n):
        
        x,y,d,k = map(int,input().split())

        before_maps[(x,y)] = [(d,k)] ##원자 위치를 key로 방향과 에너지를 value로 하는 dictionary 생성

    ##시뮬레이션 시작
    ##최초 정수 위치에 주어지고 모든 원자가 1초에 1만큼 이동하므로
    ##만날 수 있는 최소한의 가능성은 0.5초 단위로 움직일때이다.
    
    delta = [[0.0,0.5],[0.0,-0.5],[-0.5,0.0],[0.5,0.0]] ##상,하,좌,우
    
    ans = 0  ##충돌후 에너지 총합

    ##0.5초씩 움직이고 최초 위치가 -1000이상 1000이하로 주어지므로
    ##최대한으로 늦게 부딪히는 가능성은 4000번이다.
    ##예를 들어 (-1000,1000)이 아래로 가고 (1000,-1000) 좌로 갈때 부딪히는 원자

    for _ in range(4000): 
        
        after_maps = {} #0.5초 후에 원자들의 배치
        
        ##0.5초 움직이기

        for (x,y),value in before_maps.items(): ##원자위치, [(방향,에너지)]
            
            for d,k in value:

                dx = x + delta[d][0]
                dy = y + delta[d][1] ##0.5초씩 움직인 좌표
                
                ##최초 주어진 위치가 1000이내라서
                ##원자들은 방향을 바꾸지 않으므로
                ##1000을 넘어가는 원자는 충돌 가능성이 없다
                if dx <= 1000 and dx >=-1000 and dy <=1000 and dy >= -1000: 

                    if after_maps.get((dx,dy),0) == 0: ##움직인 좌표에 아무것도 존재하지 않는다면..

                        after_maps[(dx,dy)] = [(d,k)] ##새로 리스트를 만들어 저장

                    else: ##이미 움직인 좌표에 원자가 존재한다면..

                        after_maps[(dx,dy)].append((d,k))  ##방향과 에너지를 넣는다
            
        ##충돌 에너지 계산

        del_point = [] ##충돌 후 dictionary에서 key를 삭제하기 위해

        for (x,y),value in after_maps.items():  ##충돌위치, (원자 방향,에너지)의 리스트
            
            if len(value) >= 2: ## 같은 위치에 2개 이상 존재한다면 충돌했다는 뜻이므로..
                
                del_point.append((x,y)) ##해당 위치를 삭제하기 위해 임시로 저장
                
                for d,k in value:
                    
                    ans += k ##모든 에너지 방출 합
        
        ##충돌 포인트를 dictionary에서 삭제
        ##for문 도는 중에 dictionary의 key를 삭제할 수가 없어서 따로 모아놓은다음에 삭제함
        
        for x,y in del_point:
            
            del after_maps[(x,y)] ##충돌한 위치 삭제
        
        
        ##필드에 원자가 하나이하만 존재한다면.. 더 이상 충돌할 수 없으므로
        ##시뮬레이션 중단

        if len(after_maps.keys()) <= 1:
            
            break
        
        ##다음 시뮬레이션으로 초기화
        before_maps = after_maps
    

    print('#'+str(tc),ans)