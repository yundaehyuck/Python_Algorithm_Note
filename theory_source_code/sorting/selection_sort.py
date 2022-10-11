##선택정렬

array = [7,5,9,0,3,1,6,2,4,8]

n = len(array) ##배열의 길이

for i in range(n):
    
    min_index = i ##현재 단계에서 가장 작은 원소의 인덱스

    for j in range(i+1,n): ##i번 말고 나머지 중에서 가장 작은 원소를 찾는 과정
        
        if array[min_index] > array[j]: ##i번 원소보다 더 적은 j번 원소를 찾으면..
            
            min_index = j ##최솟값을 j번이라고 갱신
    
    ##현재 단계에서 최솟값과 i번 원소를 교체

    array[i],array[min_index] = array[min_index],array[i]

print(array)