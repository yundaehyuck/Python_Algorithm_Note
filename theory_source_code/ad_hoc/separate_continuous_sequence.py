#무작위로 섞인 수열에서
#왼쪽에서 오른쪽으로 연속으로 증가하는 정수 부분 수열의 개수
n = int(input())

A = list(map(int,input().split()))

visited = [0]*(n+2)

#연속하는 부분 수열의 개수
count = 0

for i in range(n):
    
    if visited[A[i]] == 0:
        
        count += 1
        visited[A[i]] = 1
    
    visited[A[i]+1] = 1


#2^y >= count인 y가 셔플 횟수
v = 1
y = 0

while v < count:
    
    v *= 2
    y += 1

print(y)