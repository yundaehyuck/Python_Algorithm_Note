from sys import stdin

#두 점 a,b의 거리를 구하는 함수
def distance(a,b):
    
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)

n = int(stdin.readline())

points = []

for _ in range(n):
    
    x,y = map(int,stdin.readline().split())

    points.append((x,y))


#가능한 두 점 사이의 거리의 총 합을 개수로 나눠 평균을 구한다
total = 0
count = 0

for i in range(n-1):
    
    for j in range(i+1,n):
        
        total += distance(points[i],points[j])
        count += 1

mean = total/count

#기댓값의 선형성을 이용하면 N!가지의 모든 경우에 대한 기댓값을 구하게 된다
print((n-1)*mean)