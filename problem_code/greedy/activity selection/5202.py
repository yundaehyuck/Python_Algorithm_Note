T = int(input())

for t in range(1,T+1):
    
    n = int(input())

    time = []

    for _ in range(n):
        
        s,e = map(int,input().split())

        time.append((s,e))
    
    ##종료시간(time[1])이 빠른 순서대로, 종료시간이 같다면 시작시간(time[0])이 빠른 순서대로 정렬
    time_sort = sorted(time,key = lambda item:[item[1],item[0]])

    b_e = 0

    ans = 0

    for s,e in time_sort:
        
        if s >= b_e: #이전 작업의 종료시간(b_e) 이상의 다음 작업의 시작시간(s)이면.. 선택
            
            ans += 1
            b_e = e #이전 작업의 종료시간을 다음 작업의 종료시간으로 변경
    
    print('#'+str(t),ans)