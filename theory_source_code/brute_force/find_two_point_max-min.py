#A*B인 직사각형 내부에서 점의 크기의 최댓값 - 최솟값의 차이의 최댓값 찾기
from sys import stdin

n,a,b = map(int,stdin.readline().split())

A = []

for i in range(n):
    
    r,c,s = map(int,stdin.readline().split())

    A.append((r,c,s))

answer = 0

#두 점 i,j를 최댓값, 최솟값이라고 하고 이 두 점이 크기 A*B인 직사각형 내부에 존재하는지 검사
#그러한 직사각형 내부에는 여러개의 점이 있을 수 있고 i,j가 최대,최소가 아닐 수도 있지만
#브루트포스로 모든 두 점 쌍을 체크하면 동일한 직사각형 내부에 다른 최대,최소를 검사해서 갱신하게 되니 괜찮
for i in range(n):
    
    r,c,s = A[i]

    for j in range(n):
        
        rr,cc,ss = A[j]

        if abs(r-rr) <= a-1 and abs(c - cc) <= b-1:
    
            if answer < s - ss:

                answer = s - ss

print(answer)