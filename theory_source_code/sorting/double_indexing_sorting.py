#n개의 원소 중 4개를 골라 2개씩 짝지어 합한 다음 만든 두 원소의 크기 차이가 최소가 되도록

n = int(input())

H = list(map(int,input().split()))

#먼저 가능한 모든 H[i]+H[j]를 만든다
#인덱스도 같이 저장
A = []

for i in range(n-1):

    for j in range(i+1,n):

        A.append((H[i] + H[j],i,j))

#합을 담은 배열을 정렬하고
A.sort()

answer = 10**18

#정렬된 배열에서 인접한 두 원소 차이가 최솟값
#모든 가능한 i = 0,1,2,..에 대해 검사
#고른 두 원소가 포함하는 4개 인덱스가 모두 달라야함
for i in range(len(A)-1):

    a,x,y = A[i]
    b,z,w = A[i+1]

    ind = set([x,y,z,w])

    if len(ind) == 4:

        if answer > b-a:

            answer = b-a

print(answer)