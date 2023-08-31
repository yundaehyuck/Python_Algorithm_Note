#counting inversion
from sys import stdin

def merge(a,start,mid,end):
    
    merged_list = [0]*(end - start + 1)

    i = start
    j = mid + 1
    k = 0

    count = 0
    right = 0

    while i <= mid and j <= end:
        
        if a[i] > a[j]:
            
            merged_list[k] = a[j]
            j += 1
            k += 1
            right += 1 #오른쪽 배열의 수가 병합 배열로 이동하면 화살표 수를 1 증가
        
        else:
            
            #왼쪽 배열의 수가 병합 배열로 이동하면 inversion 수를 지금까지 센 화살표 수만큼 증가
            merged_list[k] = a[i]
            i += 1
            k += 1
            count += right
    
     #왼쪽 배열의 수가 병합 배열로 이동하면 inversion 수를 지금까지 센 화살표 수만큼 증가
    while i <= mid:
        
        merged_list[k] = a[i]
        i += 1
        k += 1
        count += right
    
    #오른쪽 배열의 수가 병합 배열로 이동하면 화살표 수를 1 증가
    #하는데... 여기서는 왼쪽 수는 이미 다 이동했으므로, 더 이상 교점이 안생기니 굳이 안해도 됨
    while j <= end:
        
        merged_list[k] = a[j]
        j += 1
        k += 1
    
    for s in range(start,end+1):
        
        a[s] = merged_list[s-start]
    
    return count

def merge_sort(a,start,end):
    
    global answer

    if start == end:
        
        return

    mid = start + (end - start)//2

    merge_sort(a,start,mid)
    merge_sort(a,mid+1,end)
    
    answer += merge(a,start,mid,end)

n = int(stdin.readline())

A = list(map(int,stdin.readline().split()))
B = list(map(int,stdin.readline().split()))

#B 배열 수들의 index를 알아내는 과정
b = {}

for i in range(n):
    
    b[B[i]] = i

#A 배열 수들을 B배열 수들의 index로 변환
a = []

for i in range(n):
    
    a.append(b[A[i]])

answer = 0

#A의 index 배열을 merge sort한다는 것은
#A 배열의 수들을 B배열 수들의 위치로 이동시킨다는 의미
merge_sort(a,0,n-1)

print(answer)