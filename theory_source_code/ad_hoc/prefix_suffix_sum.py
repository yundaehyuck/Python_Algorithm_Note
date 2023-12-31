#배열에서 한 원소를 제거하고 인접한 원소간 절댓값 차이 합을 최소로 만드는 방법
n,k = map(int,input().split())

A = list(map(int,input().split()))

#직관적으로 원소를 오름차순 정렬한 다음, 인접한 원소끼리 차이 합을 구하는게 최적이다.
#[1,1,2,2,3,3,...,N,N] 형태로 배열을 재구성
#A에 존재하는 K개의 원소는 제거해야하므로..
visited = [0]*(n+1)

for i in range(k):
    
    visited[A[i]] = 1 #A의 원소는 미리 표시해두고

B = []

for i in range(1,n+1):
    
    if visited[i] == 0: #A의 원소가 아니라면 한번 더 넣어주고

        B.append(i)

    B.append(i)    

answer = 0

#2N-K가 짝수라면, 그냥 B배열에서 i+1번째 원소 - i번째 원소 합이 최소이다.
if (2*n-k) % 2 == 0:

    for i in range(0,len(B)-1,2):

        answer += (B[i+1]-B[i])

#2n-k가 홀수라면...
else:
    
    s = []
    e = []
    
    #마지막 원소를 제외하고 i+1번째 - i번째 원소 차이를 모두 구해놓는다
    #s1,s2,s3,...,sn
    for i in range(0,len(B)-1,2):
        
        s.append(B[i+1]-B[i])
    
    answer = sum(s)
    
    #첫번째 원소를 제외하고 i+1번째 - i번째 원소 차이를 모두 구해놓는다
    #e1,e2,e3,...,en
    for i in range(1,len(B),2):
        
        e.append(B[i+1]-B[i])
    
    k = answer
    
    #s1+s2+s3+...+sn에서 시작해서, 
    #s1+s2+s3+...sn-1 +sn - sn + en
    #s1+s2+s3+...+sn-2+sn-1 - sn-1 + en-1 + en
    #s1+s2+s3+...+sn-3+sn-2 - sn-2 + en-2 + en-1 + en
    #... 으로 모두 조사해보면 된다
    for i in range(len(s)-1,-1,-1):

        k = k - s[i] + e[i]    
        
        if answer > k:
            
            answer = k
    
print(answer)