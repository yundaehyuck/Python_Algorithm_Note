from sys import stdin

def histogram(A,start,end):
    
    if start > end:
        
        return 0
    
    if start == end:
        
        return A[start]
    
    #정복 과정
    #중간 지점 A[mid]을 기준으로
    #왼쪽 오른쪽에서 mid의 높이 일부를 포함하는 가장 큰 직사각형을 찾는다. 
    mid = start + (end-start)//2

    answer = A[mid] #현재 최대 넓이 = 중간 지점 직사각형 넓이
    count = 1 #현재 구간이 가지는 사각형 수
    min_h = A[mid] #현재 구간의 사각형 중 가장 낮은 높이

    i = mid-1 #왼쪽
    j = mid+1 #오른쪽

    #왼쪽 오른쪽을 보면서 직사각형의 높이가 덜 작아지는 방향으로 구간을 늘린다
    while i >= start and j <= end:
        
        if A[i] > A[j]: #왼쪽 사각형이 더 높은 경우, 왼쪽으로 늘리는게 유리하다.
            
            count += 1
            
            #구간의 최소 높이를 갱신 -현재 최소 높이와 새로 들어온 사각형 높이중 작은 값으로
            min_h = min(min_h,A[i])
            i -= 1 #왼쪽으로 늘리는건 i를 1 감소시키는 것
        
        else: #오른쪽 사각형이 더 높은 경우, 오른쪽으로 늘리는게 유리하다.
            
            count += 1
            min_h = min(min_h,A[j]) #구간의 최소 높이 갱신
            j += 1 #오른쪽으로 늘리는건 j를 1 증가시키는 것
        
        #매 반복마다, 구간의 최대 직사각형 넓이는 count(구간의 사각형 수 = 구간의 길이)*min_h(구간의 최소 높이)
        #현재 최대 넓이인 answer와 새로 갱신된 넓이 count*min_h중 최댓값으로 갱신
        answer = max(answer,count*min_h)
    
    #위 반복문을 탈출하면 왼쪽,오른쪽 구간중 한쪽이 끝에 도달한 상태

    #끝에 도달하지 못한 구간 중 하나를 끝까지 이동 시켜봐서 
    #넓이가 최대가 될 수 있는지, 조사하면서 최대 직사각형을 찾는다.
    
    #while 조건문에 의해 둘 중 하나는 거짓이고 실행이 안된다.
    while start <= i:
        
        count += 1
        min_h = min(min_h,A[i])
        i -= 1

        answer = max(answer,count*min_h)

    while j <= end:
        
        count += 1
        min_h = min(min_h,A[j])
        j += 1

        answer = max(answer,count*min_h)
    
    #mid를 기준으로 두 구간으로 분할하는 과정
    answer = max(answer, histogram(A,start,mid-1))
    answer = max(answer,histogram(A,mid+1,end))

    return answer

n = int(stdin.readline())

A = []

for _ in range(n):
    
    x = int(stdin.readline())

    A.append(x)


print(histogram(A,0,n-1))