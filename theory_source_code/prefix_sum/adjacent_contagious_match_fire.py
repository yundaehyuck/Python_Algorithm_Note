#각 성냥에 불을 붙이고 높이가 작거나 같은 성냥으로 양쪽으로 불을 옮길 때,
#최대로 불을 옮길 수 있는 개수?

n = int(input())

A = list(map(int,input().split()))

left = [1]*n
right = [1]*n

#각 성냥이 왼쪽 방향으로 불을 옮길 수 있는 개수
for i in range(1,n):
    
    #i-1번 원소가 i번 원소보다 높이가 작거나 같다면
    #i번 원소는 i-1번 원소가 왼쪽으로 옮길 수 있는 개수만큼 더 옮길 수 있다
    if A[i] >= A[i-1]:
        
        left[i] += left[i-1]

#각 성냥이 오른쪽 방향으로 불을 옮길 수 있는 개수
for i in range(n-2,-1,-1):
    
    #i+1번 원소가 i번 원소보다 높이가 작거나 같다면
    #i번 원소는 i+1번 원소가 오른쪽으로 옮길 수 있는 개수만큼 더 옮길 수 있다
    if A[i] >= A[i+1]:
        
        right[i] += right[i+1]

answer = 0

for i in range(n):
    
    #각 성냥이 옮길 수 있는 개수는 left[i] + right[i] - 1
    #left,right 초기화가 1이므로 left[i] + right[i]에 자기 자신이 2번 더해짐
    v = left[i]+right[i]-1

    if answer < v:
        
        answer = v

print(answer)