#minimize sum of manhattan distance

#각 차원마다 배열을 만들어 좌표를 받아 저장
#각 배열을 정렬하여 중앙값이 모든 맨해튼 거리의 합을 최소로하게 하는 좌표 

from sys import stdin

n,m = map(int,stdin.readline().split())

points = [[] for _ in range(n)]

for _ in range(m):
    
    p = list(map(int,stdin.readline().split()))

    for i in range(n):
        
        points[i].append(p[i])

fermat = []

answer = 0

for point in points:
    
    point.sort()

    fermat.append(point[m//2])

    for p in point:
        
        answer += abs(p - fermat[-1])

print(answer)
print(' '.join(map(str,fermat)))