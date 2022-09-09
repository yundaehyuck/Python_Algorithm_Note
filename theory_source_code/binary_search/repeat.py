#이진 탐색 반복문 구현

def binary_search(array, target, start, end):
    
    #시작점이 끝점보다 작거나 같을때만 반복
    #시작점이 끝점보다 커지면 반복을 종료
    while start <= end:
        

        mid = (start + end)//2 #중간점을 구한다

        #중간점의 데이터가 찾고자 하는 값과 일치하면 중간점 인덱스를 반환
        if array[mid] == target:
            
            return mid

        #중간점의 데이터가 찾고자하는 값보다 크다면 오른쪽은 볼 필요도 없다
        #끝점을 중간점-1로 옮긴다 
        elif array[mid] > target:
            
            end = mid-1
        
        #중간점의 데이터가 찾고자하는 값보다 작다면 왼쪽은 볼 필요도 없다.
        #시작점을 중간점+1로 옮긴다
        else:
            
            start = mid+1
    
    #찾지 못하면 반복문이 탈출되어 None을 반환
    return None