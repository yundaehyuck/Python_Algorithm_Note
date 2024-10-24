#모든 i,j에 대하여 (i-j)|ai-bj|의 합

#ai >= bj, ai < bj에 따라서 
#i|ai-bj| -j|ai-bj| = (i(ai-bj)+i(bj-ai)) - (j(ai-bj)+j(bj-ai))
#4 부분을 각각 구해서 합하면 될 것
n = int(input())

a = list(map(int,input().split()))

m = int(input())

b = list(map(int,input().split()))

#ai >= bj인 i,j를 찾기 위해 A,B를 정렬
#인덱스를 보존해야하므로 인덱스 포함
A = []

for i in range(len(a)):

    A.append((a[i],i+1))

B = []

for j in range(len(b)):

    B.append((b[j],j+1))

A.sort()
B.sort()

#누적합이 필요해서 미리 구해두고
p_a = [A[0][0]]

for i in range(1,n):
    
    p_a.append(p_a[-1]+A[i][0])

p_b = [B[0][0]]

for i in range(1,m):
    
    p_b.append(p_b[-1]+B[i][0])

#i를 고정시키면 i(ai-bj)+i(bj-ai)를 쉽게 구할 수 있다
#i = 0,1,2,..에 대하여 ai >= bj인 경우 j를 증가시키다가 ai < bj가 되면 멈추고
#0~j-1까지는 i(ai-bj), j~m-1까지는 i(bj-ai)
#j = 0인 경우는 0~m-1까지가 모두 ai < bj이므로 i(bj-ai)만 구하면 됨
#i가 고정되어 있으므로 B의 누적합만 알고 있으면 구할 수 있다
v1 = 0
v2 = 0
j = 0

for i in range(n):
    
    while j < m and A[i][0] > B[j][0]:

        j += 1
    
    if j == 0:

        v2 += (A[i][1]*(p_b[-1] - A[i][0]*m))

    else:
        
        v1 += (A[i][1]*(A[i][0]*j - p_b[j-1]))
        v2 += (A[i][1]*(p_b[-1] - p_b[j-1] - A[i][0]*(m-j)))

#j를 고정시키면 j(ai-bj)+j(bj-ai)를 쉽게 구할 수 있다
#j = 0,1,2,..에 대하여 ai < bj인 경우 i를 증가시키다가 ai >= bj가 되면 멈추고
#0~i-1까지는 i(bj-ai), i~n-1까지는 i(ai-bj)
#i = 0인 경우는 0~n-1까지가 모두 ai >= bj이므로 i(ai-bj)만 구하면 됨
#j가 고정되어 있으므로 A의 누적합만 알고 있으면 구할 수 있다
v3 = 0
v4 = 0
i = 0

for j in range(m):
    
    while i < n and A[i][0] <= B[j][0]:
        
        i += 1
    
    if i == 0:
        
        v3 += B[j][1]*(p_a[-1] - B[j][0]*n)
    
    else:
        
        v4 += B[j][1]*(B[j][0]*i - p_a[i-1] )
        v3 += B[j][1]*(p_a[-1] - p_a[i-1] - B[j][0]*(n-i))

print(v1 + v2 - v3 - v4)