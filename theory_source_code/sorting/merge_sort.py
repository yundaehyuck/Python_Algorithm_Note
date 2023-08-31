from sys import stdin

def merge(A,start,mid,end):
    
    merged_list = [0]*(end-start+1) #병합된 배열

    #분할된 배열은 A[start,....,mid], A[mid+1,....,end]

    i = start #분할된 첫번째 배열의 시작 index
    j = mid+1 #분할된 두번째 배열의 시작 index

    k = 0 #병합된 배열의 시작 index

    #분할된 두 배열이 각각 가리키는 index에서 원소 크기를 비교함
    #더 작은 원소를 병합된 배열에 집어넣고, 집어넣은 배열의 index를 1칸 오른쪽으로 이동
    #집어넣었을경우, 다음 위치로 집어넣기 위해 집어넣어야할 위치 k도 1칸 오른쪽 이동
    while i <= mid and j <= end:
        
        if A[i] > A[j]:
            
            merged_list[k] = A[j]
            k += 1
            j += 1
        
        else:
            
            merged_list[k] = A[i]
            k += 1
            i += 1

    #반복문이 끝나면 둘 중 하나의 분할된 배열의 모든 원소는 병합된 배열에 들어감 
    #들어가지 않은 둘 중 하나의 배열의 나머지 원소를 모두 집어넣는 과정
    while i <= mid:
        
        merged_list[k] = A[i]
        i += 1
        k += 1
    
    while j <= end:
        
        merged_list[k] = A[j]
        j += 1
        k += 1
    
    #마지막으로 정렬된 상태를 원래 배열에 넣어주는 과정
    for s in range(start,end+1):
        
        A[s] = merged_list[s-start]

def merge_sort(A,start,end):
    
    if start == end:
        
        return
    
    mid = start + (end - start)//2

    merge_sort(A,start,mid)
    merge_sort(A,mid+1,end)
    merge(A,start,mid,end)

n = int(stdin.readline())

A = [int(stdin.readline()) for _ in range(n)]

merge_sort(A,0,n-1)

print('\n'.join(map(str,A)))