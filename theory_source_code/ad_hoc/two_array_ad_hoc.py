#m개의 원소를 n개의 원소에 조건에 맞게 배치하는 방법

#A[i] <= B[j]이면 i번 사람은 B[j]를 먹는다
#B[j] 각각 누가 먹었는지 체크
n,m = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

r = max(B)

id = [-1]*(r+1)

#A[i] <= r이면, A[i],A[i]+1,...,r 초밥은 i번 사람이 모두 먹을 수 있고,
#i+1번 사람부터는 A[i]-1이하의 초밥만 먹을 수 있다.

for i in range(n):
    
    if A[i] <= r:
        
        for j in range(A[i],r+1):
            
            id[j] = i+1

        r = A[i] - 1

for i in range(m):
    
    print(id[B[i]])