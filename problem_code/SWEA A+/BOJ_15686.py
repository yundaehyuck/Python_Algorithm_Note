from sys import stdin

def nCr(n,r,s):
    
    global min_value
    
    #r개를 모두 뽑았다면
    #치킨 거리를 구해본다
    if r == 0:
        
        city_chicken = 0 #도시 치킨거리

        for h_x,h_y in house_list: #모든 집을 순회하고,
            
            min_chicken = 100000000000000000000000 #현재 집의 치킨거리 최솟값 초기화

            for c_x,c_y in comb: #i개를 뽑은 치킨 집 좌표 순회
                
                distance = (abs(c_x-h_x)+abs(c_y-h_y)) #치킨 거리 구해서

                if min_chicken > distance: #현재 집의 치킨거리 최솟값 갱신
                    
                    min_chicken = distance
            
            city_chicken += min_chicken #최솟값을 구했으면 도시 치킨거리에 누적합
        
        if min_value > city_chicken: #전체 도시 치킨거리 최솟값 초기화
            
            min_value = city_chicken
                
    else:
        
        #기본 조합 부분
        for i in range(s,n-r+1):
            
            comb[r-1] = chicken[i]

            nCr(n,r-1,i+1)

n,m = map(int,stdin.readline().split())

maps = [list(map(int,stdin.readline().split())) for _ in range(n)]

house_list = []
chicken = []
c = 0 #치킨집의 수

#모든 치킨집과 집 좌표를 찾는다
for y in range(n):
    
    for x in range(n):
        
        if maps[y][x] == 1:
            
            house_list.append((x,y))
        
        elif maps[y][x] == 2:
            
            chicken.append((x,y))
            c += 1

min_value = 10000000000000000000000000000000

#치킨집을 1개부터 m개 선택해서 모든 경우에 대해 치킨 거리를 구해본다
for i in range(1,m+1):
    
    comb = [0]*i #i개를 뽑아 치킨 좌표를 넣을 조합

    nCr(c,i,0)


print(min_value)