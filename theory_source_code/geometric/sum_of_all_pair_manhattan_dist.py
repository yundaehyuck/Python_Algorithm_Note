#sum of manhattan distance between all pairs of points
from sys import stdin

def distance(x1,x2,y1,y2):
    
    # always x2 > x1, y2 > y1
    return x2-x1 + y2-y1

n = int(stdin.readline())

x_points = []
y_points = []

for _ in range(n):
    
    x,y = map(int,stdin.readline().split())

    x_points.append(x)
    y_points.append(y)

answer = 0

#i번과 나머지 0,1,2,...,i-1번끼리 맨해튼 거리의 합은..
#|xi - x0| + |xi - x1| + ... +|xi - x(i-1)| + |yi - y0| + ... + |yi - y(i-1)|

#x,y좌표 각각 정렬해둔다면.. x0 < x1 < x2 <... <xn, y0<y1<y2<...<yn

#그러므로, i*xi - (x0 + x1 + ... + xi-1) = i*xi - Si-1로 바꿔 계산가능하다.

x_points.sort()
x_sum = x_points[0]
y_points.sort()
y_sum = y_points[0]

for i in range(1,n):

    answer += (x_points[i]*i - x_sum)
    x_sum += x_points[i]  
    answer += (y_points[i]*i - y_sum)
    y_sum += y_points[i]

print(answer)