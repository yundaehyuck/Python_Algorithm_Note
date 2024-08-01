from sys import stdin

#데이터의 개수 n, 원하는 합 m
n,m = map(int,stdin.readline().split())

#수열
num_list = list(map(int,stdin.readline().split()))

#필요한 변수

count = 0 #수열의 개수
interval_sum = 0 #누적 부분합
end = 0 #끝점 포인터

#시작점은 반복문을 돌면서 0~n-1로 증가시킨다
for start in range(n):
    
    #end는 부분수열 합이 m보다 작으면 1 증가한다
    #이때, end는 인덱스 최댓값인 n-1을 넘어가면 안된다

    while interval_sum < m and end < n:
        
        interval_sum += num_list[end]
        end += 1
    
    #반복문을 탈출했다면, end를 1 증가시킬 수 없음
    #반복문을 탈출했다면, 부분합 interval_sum은 m이상임
    #반복문을 탈출했다면, start를 1 증가시킬 차례임
    
    #부분합이 m과 같다면 카운팅 1 증가
    if interval_sum == m:
        
        count += 1
    
    #start를 1 증가시키기 이전에, 현재 start 원소를 빼주고 1을 증가
    interval_sum -= num_list[start]

print(count)