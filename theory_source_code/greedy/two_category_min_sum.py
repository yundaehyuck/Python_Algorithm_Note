#종류 1을 A개 종류 2를 B개 사면서, 가격 합이 최소가 되는 그리디 알고리즘
from sys import stdin

n,a,b = map(int,stdin.readline().split())

A = []

answer = 0

#종류 1을 N개 모두 사고, p1+p2+..+pn = s 일정한 상수
#종류 2와 종류 1의 차이 q1-p1, q2-p2,...,qn-pn을 오름차순 정렬
#여기서 작은것부터 b개씩 더하면, 일정한 상수에 최솟값들을 더해나갔으므로, 전체 합은 최소가 되며
#q1+q2+..+qb + p1+p2+...+pa로 p가 a개 q가 b개가 된다.

for i in range(n):

    p,q = map(int,stdin.readline().split())

    answer += p

    A.append(q-p)

A.sort()

for i in range(b):
    
    answer += A[i]

print(answer)