from sys import stdin

def divide_and_conquer(A,start,end):
    
    if start > end:
        
        return 0
    
    if start == end:
        
        return A[start]*A[start]

    mid = start + (end - start)//2

    s = A[mid] #현재 구간의 수의 합
    m = A[mid] #현재 구간에 들어간 수들의 최솟값
    score = s*m #현재 최대 점수

    i = mid - 1
    j = mid + 1
    
    #왼쪽과 오른쪽을 보면서 구간에 들어간 수들의 최솟값이 최대한 덜 작아지도록 구간을 확장
    while i >= start and j <= end:

        if A[i] > A[j]: #왼쪽의 수가 더 큰 경우,

            s += A[i] #새로 들어온 수를 구간에 들어간 수들의 합에 누적해나감
            
            #구간의 수들의 최솟값은, 새로 들어온 수와 현재 구간 수들의 최솟값중 더 작은 값으로 갱신
            m = min(A[i],m)
            i -= 1 #왼쪽으로 늘린건 i를 1 감소시킨 것

        else: #오른쪽의 수가 더 큰 경우
            
            s += A[j] #새로 들어온 수를 구간에 들어간 수들의 합에 누적해나감
            m = min(A[j],m)
            j += 1 #오른쪽으로 늘린건 j를 1 증가시킨 것
        
        score = max(score,s*m) #매 반복마다 현재 최대 score와 갱신된 score중 더 큰 값을 최댓값으로
    
    #위 반복문이 끝나면, i가 start에 도달했거나 j가 end에 도달했거나
    #도달하지 못한 방향을 끝까지 탐색하며 최댓값이 발견되면 갱신
    while i >= start:

        s += A[i]
        m = min(A[i],m)
        i -= 1

        score = max(score,s*m)

    while j <= end:
        
        s += A[j]
        m = min(A[j],m)
        j += 1

        score = max(score,s*m)
    
    #mid를 기준으로 (start,mid-1)과 (mid+1,end)로 분할해서 분할정복
    score = max(score,divide_and_conquer(A,start,mid-1))
    score = max(score,divide_and_conquer(A,mid+1,end))

    return score   

n = int(stdin.readline())

A = list(map(int,stdin.readline().split()))

print(divide_and_conquer(A,0,n-1))