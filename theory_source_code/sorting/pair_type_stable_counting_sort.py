#stable counting sort(pair type)

#정렬하고자 하는 배열
x = [[5,2],[9,0],[10,1],[4,3],[7,5]]

n = len(x) #배열의 크기
m = 10 #나올 수 있는 원소 크기

#먼저 두번째 원소를 기준으로 정렬
counting = [0]*(m+1)

#counting배열에 두번째 원소 등장 횟수를 세고..
for i in range(n):
    
    counting[x[i][1]] += 1

#누적합 배열을 만들어서..
for i in range(1,m+1):
    
    counting[i] += counting[i-1]

#정렬된 두번째 원소의 인덱스를 저장
second = [0]*(n)

#원래 배열의 뒤에서부터 순회하여, 

#i >> x[i][1](두번째 원소 값에 접근) >> 
# >> counting[x[i][1]](누적합 배열에 접근) >> 
#second[counting[x[i][1]-1] = i(새로운 배열에 누적합배열-1번 인덱스에 순회중인 인덱스 i를 저장)
for i in range(n-1,-1,-1):
    
    second[counting[x[i][1]]-1] = i
    
    counting[x[i][1]] -= 1

#다음 첫번째 원소를 기준으로 정렬하는 단계

counting = [0]*(m+1)

#첫번째 원소의 등장 횟수를 counting배열에 저장
for i in range(n):
    
    counting[x[i][0]] += 1

#stable sort를 위한 누적합 배열 구성
for i in range(1,m+1):
    
    counting[i] += counting[i-1]

#새롭게 정렬된 결과를 담을 배열
new_x = [0]*(n)

#second배열의 뒤에서부터 순회
for i in range(n-1,-1,-1):
    
    #i >> second[i]:second 배열의 인덱스
    #>> x[second[i]][0]: 정렬전 배열의 첫번째 원소
    #counting[x[second[i]][0]]: 누적합 배열에 접근
    #new_x[counting[x[second[i]][0]]-1]: 새롭게 정렬할 배열의 (누적합 배열의 값-1)번 인덱스에
    #정렬 전 배열의 x[second[i]]값 저장
    new_x[counting[x[second[i]][0]]-1] = x[second[i]]

    #접근했던 누적합 배열의 원소 1 감소
    counting[x[second[i]][0]] -= 1

print(new_x)
[[4, 3], [5, 2], [7, 5], [9, 0], [10, 1]]