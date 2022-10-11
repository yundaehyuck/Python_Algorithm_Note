#버블정렬

array = [7,5,9,0,3,1,6,2,4,8]

n = len(array) #배열의 길이

for i in range(n-1,0,-1): ##비교 구간의 끝지점 선택
    
    for j in range(0,i): ##비교 원소 선택
        
        if array[j] > array[j+1]: ##왼쪽 원소가 더 크다면..
            
            array[j],array[j+1] = array[j+1],array[j] ##두 원소의 자리를 바꾼다

print(array)