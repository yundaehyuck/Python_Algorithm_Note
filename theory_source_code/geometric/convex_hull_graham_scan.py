#convex hull - graham scan
import math
from sys import stdin

#CCW
def ccw(x,y):

    return - (x[0]*y[1]) + (x[1]*y[0])

#find convex hull using graham scan 
def graham(points):
    
    #기준점과 시작점을 볼록 껍질에 넣어주고.
    scan = [0,1]
    
    #정렬된 점을 2번부터 순회하여...
    for i in range(2,n):
        
        #(-2번,-1번,i번 점)의 CCW여부 체크
        while scan:
        
            p = points[scan[-2]]

            x = [points[scan[-1]][0] - p[0], points[scan[-1]][1] - p[1]]
            y = [points[i][0] - p[0], points[i][1] - p[1]]

            v = ccw(x,y)
            
            #CCW를 이루면 볼록껍질에 넣어주고 바로 반복문 탈출
            if v < 0:

                scan.append(i)
                break
            
            #일직선을 이루면.. 선분의 양 끝점만 가지고 가라 했으므로.. 중간의 점을 제거하고
            #i번 점을 넣어주고 반복문 탈출
            #정렬되어 있으니 -1번 점이 중간의 점이고 pop한 다음 바로 append(i)하면 된다.
            elif v == 0:

                scan.pop()
                scan.append(i)
                break
            
            #CW를 이루면 -1번 점을 pop하고 다시 위 과정을 반복
            else:

                scan.pop()
    
    #모든 점을 순회하고 스택에 남아 있는 점들이 볼록 껍질을 이룬다
    return scan

n = int(stdin.readline())

points = []

for _ in range(n):
    
    x,y = map(int,stdin.readline().split())

    points.append((x,y))

#점들을 y좌표가 작은 순, y좌표가 같으면 x좌표가 작은 순으로 오름차순 정렬
points.sort(key = lambda item: [item[1],item[0]])

#기준점은 y좌표가 가장 작고 x좌표가 가장 작은 좌표
p = points[0]

#각도순 정렬
#기준점을 중심으로 해당 점이 x축 양의 방향과 이루는 각도 크기로 오름차순 정렬
#math.atan2(y,x)로 각도 크기를 구한다.
points.sort(key = lambda item: math.atan2(item[1]-p[1],item[0]-p[0]))

scan = graham(points)

print(len(scan))