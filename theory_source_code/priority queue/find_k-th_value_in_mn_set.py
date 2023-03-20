import heapq

n,m,k = map(int,input().split())

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

#두 정수 배열을 오름차순 정렬
arr1.sort()
arr2.sort()

q = []

# 처음에는 n개의 원소에 대해 각각 
# 두 번째 수열의 첫 번째 원소를 대응시켜줍니다.
# 두 수의 합이 작은 값이 더 먼저 나와야 하므로
# +를 붙여서 넣어줍니다. 

#두 정수쌍의 합이 작은 순서대로 k번째 작은 합을 구해야하므로,
#두 정수쌍의 합과 두 정수의 index를 tuple로 구성
for i in range(n):

    heapq.heappush(q,(arr1[i]+arr2[0], i, 0))

# 1번부터 k - 1번까지 합이 작은 쌍을 골라줍니다.

#우선순위 큐에서 하나를 빼면 그것이 i번째 작은 합
#뺀 튜플에 든 2번째 array의 index를 이용해서 다음 index와 매칭시켜
#그것도 i+1번째 작은 합의 후보가 될 수 있다.
for _ in range(k-1):

    _,ind1,ind2 = heapq.heappop(q)

    #두번째 array에서 매칭 시킬 원소가 남아있다면...
    if ind2+1 < m:
        heapq.heappush(q,(arr1[ind1]+arr2[ind2+1],ind1,ind2+1))


#k-1번 빼고 나서, 1번 더 빼면 이것이 k번째 작은 합
value,_,_ = heapq.heappop(q)

print(value)