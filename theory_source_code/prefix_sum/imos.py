#[a,b]에 c를 더하는 구간 쿼리 해결하는 누적합 테크닉 imos법

from sys import stdin

n,m = map(int,stdin.readline().split())

h = list(map(int,stdin.readline().split()))

#[a,b]가 주어질때, a-1번 위치에 +k를 더해주고
#b번에 -k를 더해준다.
#b가 n 이상이면 없는 위치이므로 무시해도 된다
offset = [0]*n

for _ in range(m):
    
    a,b,k = map(int,stdin.readline().split())

    offset[a-1] += k

    if b < n:

        offset[b] += -k

#모든 쿼리를 해결하고 오프셋 배열을 누적합
for i in range(1,n):
    
    offset[i] += offset[i-1]

#누적합된 오프셋 배열의 원소를 원래 배열 원소에 대응하는 위치마다 더해준다
for i in range(n):
    
    h[i] += offset[i]

print(' '.join(map(str,h)))