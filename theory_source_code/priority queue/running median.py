import heapq
from sys import stdin

min_q = [] #최소힙
min_len = 0 #최소힙의 크기

max_q = [] #최대힙
max_len = 0 #최대힙의 크기

n = int(stdin.readline())

for _ in range(n):
    
    ##현재 들어오는 수열의 값
    x = int(stdin.readline())
    
    #최대힙의 원소 수와 최소힙의 원소 수가 동일하면
    if max_len == min_len:
       
       #최대힙에 수열의 원소를 삽입
       #최대힙에는 (-실제원소,실제원소)로 넣어준다
        heapq.heappush(max_q,(-x,x))

        max_len += 1 #삽입했으니 최대힙 크기를 1 증가
    
    #최대힙의 원소 수가 최소힙의 원소 수보다 1 더 크면
    elif max_len == min_len+1:
    
    #최소힙에 수열의 원소를 삽입
        heapq.heappush(min_q,x)

        min_len += 1 #원소를 넣었으니 최소힙 크기 1 증가
    
    ##최대힙과 최소힙에 모두 원소가 존재할때,
    if max_len >= 1 and min_len >= 1:
        
        ##최대힙의 top이 최소힙의 top보다 크다면
        if max_q[0][1] > min_q[0]:
        
            a,b = heapq.heappop(max_q)
            c = heapq.heappop(min_q)
            
       ##최대힙의 top과 최소힙의 top을 서로 교환
       ##당연하지만 heappop을 하고 heappush로 해서 넣어줘야지
       ##인덱스 교환하면 안돼..
       ##아니 해도 되나?? 모르겠네
            heapq.heappush(max_q,(-c,c))
            heapq.heappush(min_q,b)
    
    ##매 차례에 중앙값은 최대힙의 top에 존재한다
    print(max_q[0][1])