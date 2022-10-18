import heapq
from sys import stdin

n = int(stdin.readline())

##모든 수업을 (시작시간, 종료시간)으로 우선순위 큐를 만들어준다
q = []

for _ in range(n):
    
    s,t = map(int,stdin.readline().split())

    heapq.heappush(q,(s,t))

##먼저 시작시간이 가장 빠른 수업을 강의실 우선순위 큐에 배치한다
s,t = heapq.heappop(q)

cnt_q = []

heapq.heappush(cnt_q,(t,s))

##수업을 강의실에 배치하기 시작
while q:
    
    ##배치해야할 새로운 수업
    s,t = heapq.heappop(q)
    
    ##현재 강의실에서 가장 빨리 종료하는 수업
    b_t,b_s = heapq.heappop(cnt_q)
    
    ##새로운 수업의 시작시간이, 가장 빨리 종료하는 수업의 종료시간 이상이라면?
    if s >= b_t:
        
        #그 수업은 종료시키고, 그 강의실에 새로운 수업을 배치합니다.
        heapq.heappush(cnt_q,(t,s))
    
    ##새로운 수업의 시작시간이 가장 빨리 종료하는 수업의 종료시간보다 작다면?
    else:
        
        ##아직 수업이 종료된 것이 아니니, 수업은 계속하고
        heapq.heappush(cnt_q,(b_t,b_s))
        
        ##새로운 수업은 다른 강의실에 배치해야합니다.
        heapq.heappush(cnt_q,(t,s))

##모든 수업을 배치하고나서, 표시된 강의실의 수가 최소의 강의실 수입니다.
print(len(cnt_q))