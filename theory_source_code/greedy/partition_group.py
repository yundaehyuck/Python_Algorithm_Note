#boj 13164
from sys import stdin

n,k = map(int,stdin.readline().split())

#주어진 배열을 먼저 정렬하고,
height = list(map(int,stdin.readline().split()))

height.sort()

#초기 상태의 비용을 구한다
max_cost = height[-1] - height[0]

#인접한 원소간 차이를 구하고 정렬해서
minus = []

for i in range(n-1):
    
    minus.append(height[i+1] - height[i])

minus.sort()

#인접한 원소간 차이가 가장 큰값부터 k-1개를 차례대로 원래 비용에서 빼면
#그것이 k개의 그룹간 비용합의 최솟값
while k > 1:

    max_cost -= minus.pop()
    k -= 1

print(max_cost)