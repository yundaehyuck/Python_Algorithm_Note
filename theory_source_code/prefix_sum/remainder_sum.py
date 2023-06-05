import math
from sys import stdin

n,m = map(int,stdin.readline().split())

A = list(map(int,stdin.readline().split()))

prefix = [0]*(n+1)
group = [[] for _ in range(m)]
group[0].append(0)

for i in range(1,n+1):
    
    #prefix sum을 구해준다.
    prefix[i] = prefix[i-1] + A[i-1]
    
    #prefix sum 각각을 m으로 나눈 나머지를 구하고 각 그룹 내에 prefix sum값을 저장한다.
    group[prefix[i]%m].append(prefix[i])

answer = 0

#m으로 나눈 나머지가 동일한 그룹에서 2개를 뽑는 방법의 수를 전부 더하면,
#모든 경우에 [i,j]의 구간합이 m으로 나눈 나머지가 0인 경우가 된다.
for j in range(m):
    
    x = len(group[j])

    answer += math.comb(x,2)

print(answer)