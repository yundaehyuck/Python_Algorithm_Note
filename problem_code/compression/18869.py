from sys import stdin

m,n = map(int,stdin.readline().split())

universe = []

compression = {}

for i in range(m):
    
    A = list(map(int,stdin.readline().split()))
    
    #i번째 우주에 대한 compression map
    compression[i] = {}
    
    #value:index로 mapping
    for j in range(n):
        
        compression[i][A[j]] = j
    
    #A를 정렬
    A.sort()
    
    #value를 index로 바꾸는 value compression 수행
    for j in range(n):
        
        A[j] = compression[i][A[j]]
   
    universe.append(A)

answer = 0

for i in range(m-1):
    
    for j in range(i+1,m):
        
        A = universe[i]
        B = universe[j]

        ok = True

        for a in range(n-1):
            
            if A[a] == B[a] and A[a+1] == B[a+1]:
              
                continue
            
            else:
                ok = False
                break
        
        if ok == True:
            
            answer += 1

print(answer)