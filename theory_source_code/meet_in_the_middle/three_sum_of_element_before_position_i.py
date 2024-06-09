#현재 위치 i 이전의 세 수의 합이 현재 위치 i번째 수와 같은 경우를 세는 방법
n = int(input())

A = list(map(int,input().split()))

count = 0

#A가 -10만~10만이고, 두 수의 합이 저장된다
#-20만~20만을 저장할려면 크기가 40만이어야 한다
P = [0]*(4*10**5+1)

#A[i] = A[j] + A[k] + A[w], j,k,w < i인 i의 개수를 센다
#A[i] - A[j] = A[k] + A[w]이므로, 
#k,w < i인 A[k] + A[w]의 값이 저장된 배열이 있다면, 
#i = 0,1,2..,n-1, j = 0,1,2,..,i-1에 대해 A[i] - A[j]가 배열에 존재하는지 체크하면 된다

#이것을 O(N^2)에 하는 놀라운 테크닉
#검사를 먼저하고 저장하기
for i in range(n):
    
    a = A[i]
    
    #먼저 P에 A[i] - A[j]가 존재하면, counting
    for j in range(i):
        
        if P[a - A[j]] == 1:
            
            count += 1
            break
    
    #그리고 j = 0,1,2,..,i에 대하여 A[i] + A[j]를 표시
    for j in range(i+1):

        P[a+A[j]] = 1
    
    #이렇게 하면 다음에는 i+1에서 검사하게 될거고
    #배열 P에는 i+1 이전의 j = 0,1,2,.,i, k= 0,1,2..,i에 대하여 A[j] + A[k]의 값이 저장되어 있다

print(count)