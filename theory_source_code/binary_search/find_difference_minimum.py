from sys import stdin

#boj 17124

#특정 수보다 크면서 최소인 값

def lower_binary_search(B,target,start,end):
    
    while start < end:
        
        mid = start + (end - start)//2

        if B[mid] >= target:
            
            end = mid
        
        else:
            
            start = mid + 1
    
    return end

#특정 수보다 작으면서 최대인 값
def upper_binary_search(B,target,start,end):
    
    while start < end:
        
        mid = start + (end-start)//2

        if B[mid] > target:
            
            end = mid
        
        else:
            
            start = mid + 1

    return end - 1


t = int(stdin.readline())

for _ in range(t):
    
    n,m = map(int,stdin.readline().split())

    A = list(map(int,stdin.readline().split()))
    B = list(map(int,stdin.readline().split()))

    B.sort()

    C = []

    for i in range(n):
        
        lower = lower_binary_search(B,A[i],0,m)
        
        #배열의 마지막을 넘어가는 경우
        if lower == m:
            
            lower -= 1

        upper = upper_binary_search(B,A[i],0,m)
        
        #배열의 마지막을 넘어가는 경우
        if upper == m:
            upper -= 1
            
        #두 수 중의 절댓값이 작은 값이 정답
        x = abs(A[i] - B[lower])
        y = abs(A[i] - B[upper])


        if x > y:
            
            C.append(B[upper])
        
        elif x < y:
            
            C.append(B[lower])
        
        else:
            
            if B[lower] > B[upper]:
                
                C.append(B[upper])
            
            else:
                
                C.append(B[lower])
    
    print(sum(C))