from sys import stdin

n,m = map(int,stdin.readline().split())

num_list = list(map(int,stdin.readline().split()))

#시작점과 끝점 포인터
s = 0
e = 0

#최초 부분수열의 합
sum_value = num_list[0]

cnt = 0

while 1:
    
    #만약 누적합이 m과 같다면...
    if sum_value == m:
        
        #카운팅을 하고
        cnt += 1
        
        #s를 1 증가시킨다
        #1 증가시킨다는 것은 증가 이전에 원소를 누적합에서 빼준다는 뜻
        sum_value -= num_list[s]
        s += 1
    
    #만약 누적합이 m보다 크다면...
    elif sum_value > m:
        
        #s를 1 증가시킨다
        #1 증가시킨다는 것은 증가 이전에 원소를 누적합에서 빼준다
        sum_value -= num_list[s]
        s += 1
    
    #만약 누적합이 m보다 작다면...
    else:
        
        #end를 1 증가시킨다.
        e += 1
        
        #만약 end가 n 이상으로 배열 범위를 벗어난다면
        #더 이상 조사할 수열이 없다는 뜻이다.
        if e >= n:
            break #반복문을 탈출
        
        #범위를 벗어난 것이 아니라면, end의 원소를 누적합해준다.
        sum_value += num_list[e]

#반복문을 탈출하면 수열 개수를 출력
print(cnt)