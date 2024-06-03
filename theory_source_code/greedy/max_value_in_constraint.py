#기간 제한이 있는 과제들을 적절하게 수행해서 최대 가치를 얻는 방법
import heapq
from sys import stdin

n = int(stdin.readline())

A = []

for _ in range(n):
    
    x,y = map(int,stdin.readline().split())
    A.append((x,y))

#기간 제한이 빠른 순으로 오름차순 정렬
A.sort()

queue = []

for x,y in A:
    
    #일단 과제를 계속 수행하면서
    heapq.heappush(queue,y)
    
    #수행한 과제수(현재 날짜)가 현재 과제를 처리해야하는 제한보다 많아지면?
    #수행한 과제들 중 점수가 가장 작은걸 제거
    if len(queue) > x:
        
        heapq.heappop(queue)

#끝나면 큐에 남아있는 점수 합이 최댓값
total = sum(queue)

print(total)