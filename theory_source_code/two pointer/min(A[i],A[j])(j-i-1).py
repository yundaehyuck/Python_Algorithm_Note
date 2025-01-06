#min(A[i],A[j]) * (j - (i-1)-2)의 최댓값

#i = 0, j = n-1에서 시작해서 양쪽에서 간격을 좁혀가며 투포인터

#A[i] > A[j]일때 i를 1 증가시키면, j-(i-1)-2는 1 감소하지만
#A[i+1] > A[J]라고 한다면 min(A[i],A[j])는 변하지 않으므로 value가 감소
#A[i+1] < A[j]라고 한다면 min(A[i],A[j])는 감소하므로 value가 감소

#반대로 j를 1 감소하면 j- (i-1)-2는 1 감소하지만
#A[i] > A[j-1]이라고 한다면 min(A[i],A[j])는 A[j-1] > A[j]이면 커질 가능성이 있다
#A[i] < A[j-1]이라고 한다면 min(A[i],A[j])는 A[i]인데 A[j]보다 커지므로 커질 가능성이 있다
#따라서 j를 1 감소시키면 커지는 경우가 존재한다

#A[i] <= A[j]이면 반대로 i를 1 증가시키면 된다

n = int(input())

A = list(map(int,input().split()))

i = 0
j = n-1

answer = 0

while i <= j:
    
    if A[i] > A[j]:

        v = A[j] * (j-(i-1)-2)
        j -= 1
    
    else:
        
        v = A[i] * (j-(i-1)-2)
        i += 1

    if answer < v:

        answer = v    

print(answer)