#convex hull - monotone chain
from sys import stdin

def ccw(x,y):
    
    return x[0]*y[1] - x[1]*y[0]

def monotone(points):
    
    #점을 x좌표 순으로, 같으면 y좌표 순으로 오름차순 정렬
    points.sort()

    n = len(points)
    
    #0번, 1번점을 윗껍질, 아래껍질에 넣고
    upper = [0,1]
    lower = [0,1]
    
    #2번점부터 차례대로 순회하여...
    for i in range(2,n):
        
        #윗 껍질을 구하는 과정
        #스택의 길이가 최소 2이상일때만 반복문 수행
        #(-2번,-1번,i번)점이 CW를 이루면 append하고 break
        #그 외에는 pop하고 반복
        while len(upper) >= 2:

            x = [points[upper[-1]][0] - points[upper[-2]][0], points[upper[-1]][1] - points[upper[-2]][1]]
            y = [points[i][0] - points[upper[-2]][0], points[i][1] - points[upper[-2]][1]]

            k = ccw(x,y)

            if k >= 0:

                upper.pop()

            else:

                upper.append(i)
                break

        if len(upper) <= 1:

            upper.append(i)
        
        #아래 껍질을 구하는 과정
        #스택의 길이가 최소 2이상일때만 반복문 수행
        #(-2번,-1번,i번)점이 CCW를 이루면 append하고 break
        #그 외에는 pop하고 반복
        while len(lower) >= 2:

            x = [points[lower[-1]][0] - points[lower[-2]][0], points[lower[-1]][1] - points[lower[-2]][1]]
            y = [points[i][0] - points[lower[-2]][0], points[i][1] - points[lower[-2]][1]]

            k = ccw(x,y)

            if k <= 0:

                lower.pop()

            else:

                lower.append(i)
                break

        if len(lower) <= 1:

            lower.append(i)
    
    #시작점, 끝점은 upper, lower에 동시에 포함되어 있으니 2개를 빼줘야함
    return len(upper)+len(lower)-2

n = int(stdin.readline())

points = []

for _ in range(n):
    
    x,y = map(int,stdin.readline().split())
    points.append((x,y))

print(monotone(points))