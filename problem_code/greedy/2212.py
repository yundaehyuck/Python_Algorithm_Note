from sys import stdin

n = int(stdin.readline())

k = int(stdin.readline())

sensor = list(map(int,stdin.readline().split()))

#n < k이면, k개 집중국을 모두 n개의 좌표 위에 세우면 되니 길이 합이 0
if n < k:
    
    print(0)

# n >= k
else:
    
    #센서 좌표를 오름차순 정렬
    sensor.sort()
    
    #초기 비용을 최대 - 최소로 초기화
    max_cost = sensor[-1] - sensor[0]
    
    #인접한 원소간 차이를 구해서 정렬하고
    minus = []

    for i in range(n-1):

        minus.append(sensor[i+1]-sensor[i])

    minus.sort()
    
    #인접한 원소간 차이를 큰 값부터 k - 1개 선택해서 초기 비용에서 빼나가면
    #그것이 k개를 설치했을때 수신 가능 영역 길이의 합의 최소이다.
    while k > 1:

        max_cost -= minus.pop()
        k -= 1

    print(max_cost)