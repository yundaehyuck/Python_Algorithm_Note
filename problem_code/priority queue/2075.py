import heapq
from sys import stdin

n = int(stdin.readline())

min_heap = []

q = list(map(int,stdin.readline().split()))

for i in q:
    
    heapq.heappush(min_heap,i)

for _ in range(n-1):
    
    q = list(map(int,stdin.readline().split()))

    for i in q:
        
        heapq.heappush(min_heap,i)
        heapq.heappop(min_heap)
    
print(heapq.heappop(min_heap))