#실수 이분탐색
def binary_search(array,v,u,start,end):
    
    #실수 이분탐색은 핵심이 start < end 조건 반복이 아니라 그냥 100번 정도만 돌린다
    for _ in range(100):
        
        mid = (start+end)/2 #고정된 시간 mid

        t = 0

        for i in range(len(array)):
            
            if array[i] > mid*v: #아이스크림은 mid시간동안 mid*v만큼 녹는다.
                
                t += ((array[i]-mid*v)) #내가 i번째 아이스크림은 array[i]-mid*v만큼 먹을 수 있다
        
        #mid동안 이론상 내가 먹을 수 있는 양은 mid*u
        #실제 먹은 양 t와 mid*u를 비교해서
        
        #t가 작으면 mid가 너무 커서 덜 먹은 것이니 end를 줄인다
        if t <= mid*u:
            
            end = mid
        
        #t가 크면 mid가 작아서 많이 먹은거니 start를 키운다
        else:
            
            start = mid
    
    #이분탐색이 끝나면 end시간이 최적해
    #end 시간동안 먹을 수 있는 양은 end*u
    return end*u

n,v,u = map(int,input().split())

A = list(map(int,input().split()))

print(binary_search(A,v,u,0,10**9+1))