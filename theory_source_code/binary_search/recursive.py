#이진 탐색 재귀적 구현

def binary_search(array, target, start, end):
    
    if start > end:
        
        return None
    
    mid = (start + end)//2

    #중간점 데이터와 target이 동일하면 중간점 index를 반환
    if array[mid] == target:
        
        return mid
    
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽을 확인
    elif array[mid] > target:
        
        #end를 중간점의;왼쪽으로 보낸다
        return binary_search(array, target, start, mid-1)
    
    #중간점의 값보다 찾고자 하는 값이 큰 경우에 오른쪽을 확인
    else:
        
        #start를 중간점의 오른쪽으로 보낸다
        return binary_search(array, target, mid+1, end)