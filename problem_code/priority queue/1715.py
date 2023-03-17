import heapq
from sys import stdin

n = int(stdin.readline())

q = []

count = n

answer = 0

for _ in range(n):
    
    a = int(stdin.readline())

    heapq.heappush(q,a)

while q:

    x = heapq.heappop(q)

    count -= 1

    if count == 0:

        break

    y = heapq.heappop(q)

    count -= 1

    answer += (x+y)

    if count != 0:

        heapq.heappush(q,(x+y))

        count += 1

print(answer)