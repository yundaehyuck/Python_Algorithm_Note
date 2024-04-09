#prefix sum만 누적합이 아니다1
n,m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

A = [0]*(100001)
B = [0]*(100001)

#A,B팀 각각이 10만 이내에 보유한 점수들을 counting
for i in range(n):
    
    A[a[i]] += 1

for i in range(m):
    
    B[b[i]] += 1

answer = [0,0,0] #A팀 승, B팀 승, 무승부

#A,B팀이 현재 i점보다 작은 점수를 가진 팀원 수 누적합
a = 0 
b = 0

for i in range(1,100001):
    
    #현재 i점에서 A[i]가 0이 아니고, B[i]가 0인 경우?
    if A[i] != 0 and B[i] == 0:
        
        answer[0] += b*A[i] #A팀은 i점보다 작은 모든 B팀에 대해 이긴다
        a += A[i]
    
    #현재 i점에서 B[i]가 0이 아니고, A[i]가 0인 경우?
    elif B[i] != 0 and A[i] == 0:
        
        answer[1] += a*B[i] #B팀은 i점보다 작은 모든 A팀에 대해 이긴다
        b += B[i]
    
    #A[i],B[i] 둘다 0이 아니라면?
    #현재 i점을 보유한 A,B팀은 A*B만큼 무승부가 나고
    #A는 i점보다 작은 b에 대해 이길 수 있고
    #B는 i점보다 작은 a에 대해 이길 수 있고
    elif A[i] != 0 and B[i] != 0:
        
        answer[0] += A[i]*b
        answer[1] += B[i]*a
        answer[2] += A[i]*B[i]

        a += A[i]
        b += B[i]

print(*answer)