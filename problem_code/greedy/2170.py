from sys import stdin

n = int(stdin.readline())

points = []

for i in range(n):
    
    x,y = map(int,stdin.readline().split())

    points.append((x,y))

#왼쪽 좌표를 기준으로 오름차순 정렬
points.sort()

answer = 0

#가장 왼쪽의 좌표와 가장 오른쪽의 좌표를 기억하고
min_x,max_y = points[0]

#정렬된 좌표 리스트를 왼쪽부터 순회하기 시작
for i in range(1,n):
    
    x,y = points[i]
    
    #이미 정렬되었으므로, x < min_x일수는 없다.
    #(min_x,max_y)와 (x,y)가 겹치기 위해서는 (x <= max_y)이다 
    if x <= max_y:
        
        #겹쳤다면, 가장 오른쪽의 좌표를 갱신해준다
        if max_y < y:
            
            max_y = y
    
    #더이상 겹치지 않는다면, 그동안 겹쳐진 구간의 최대 길이를 더해주고,
    else:
        
        answer += (max_y - min_x)
        
        #새롭게 가장 왼쪽의 좌표와 오른쪽의 좌표를 갱신한다
        min_x,max_y = x,y
        
#모든 for문을 수행하면, 마지막 구간의 길이는 더해져있지 않으므로 더해주는것 잊지말기
answer += (max_y - min_x)

print(answer)