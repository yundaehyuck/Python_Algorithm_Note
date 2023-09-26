import math
from sys import stdin

def ccw(x,y):
    
    return x[0]*y[1] - x[1]*y[0]

#두 점 사이 거리
def distance(x,y):
    
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**(1/2)

#monotone chain으로 convex hull을 구하는 알고리즘
def monotone(points,r):
    
    points.sort()

    upper = [0,1]
    lower = [0,1]

    for i in range(2,n):
        
        while len(upper) >= 2:
            
            x = [points[upper[-1]][0] - points[upper[-2]][0], points[upper[-1]][1] - points[upper[-2]][1]]
            y = [points[i][0] - points[upper[-2]][0], points[i][1] - points[upper[-2]][1]]

            v = ccw(x,y)

            if v < 0:
                
                upper.append(i)
                break
            
            else:
                
                upper.pop()
        
        if len(upper) <= 1:
            
            upper.append(i)
        
        while len(lower) >= 2:
            
            x = [points[lower[-1]][0] - points[lower[-2]][0], points[lower[-1]][1] - points[lower[-2]][1]]
            y = [points[i][0] - points[lower[-2]][0], points[i][1] - points[lower[-2]][1]]

            v = ccw(x,y)

            if v > 0:
                
                lower.append(i)
                break
            
            else:
                
                lower.pop()
        
        if len(lower) <= 1:
            
            lower.append(i)
    
    #upper의 0~len(upper)-1까지는 윗껍질
    #lower의 len(lower)-2부터 1까지는 아래 껍질이므로, 이를 윗껍질에 append하면 전체 convex hull
    for i in range(len(lower)-2,0,-1):
        
        upper.append(lower[i])
    
    answer = 0

    upper.append(upper[0])
    upper.append(upper[1])
    
    #전체 convex hull의 둘레의 길이는.. 
    
    ##두 꼭짓점 사이 직선 거리를 구하고
    for i in range(len(upper)-2):

        answer += distance(points[upper[i]], points[upper[i+1]])
    
    #convex hull은 결국 하나의 중심을 기준으로 한바퀴 도는 것과 같으므로
    #모든 부채꼴의 호의 길이 합은, 결국 원기둥의 밑면의 둘레의 길이와 같으니까
    #꼭짓점끼리 직선거리 합에 반지름이 r인 원의 둘레의 길이를 합하면 된다
    answer += 2*math.pi*r

    return answer     
        
n,r = map(int,stdin.readline().split())

points = []

for _ in range(n):
    
    x,y = map(int,stdin.readline().split())

    points.append((x,y))

circum = monotone(points,r)

print(circum)