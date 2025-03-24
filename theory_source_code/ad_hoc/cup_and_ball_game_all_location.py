#야바위 게임에서 i-1번,i+1번으로 한번 속임수로 이동시킬때,
#q번 섞고나서 공이 있을 수 있는 모든 컵의 개수
T = int(input())

for t in range(1,T+1):
    
    n,q = map(int,input().split())

    A = list(range(n+1)) #일렬로 나열한 컵의 라벨 [0,1,2,3,..,n]

    now = 1 #현재 공의 위치 1번
    answer = set()
    
    #0번 컵은 존재하지 않는다
    if now-1 >= 1:
        
        answer.add(A[now-1])
    
    if now+1 <= n:
        
        answer.add(A[now+1])
    
    for _ in range(q):
        
        a,b = map(int,input().split()) #a번과 b번을 바꾸는데
        
        #원래 공이 a번에 있으면 b번으로 이동하고
        if now == a:
            
            now = b
        
        #b번에 있으면 a번으로 이동하고
        elif now == b:
            
            now = a
        
        #서로 바꿨으니 라벨도 바뀌어야함
        A[a],A[b] = A[b],A[a]
        
        #여기서 속임수를 쓰면 
        #공은 이후에는 A[now-1]번 라벨 혹은 A[now+1]번 라벨에만 존재할 수 있다
        if now - 1 >= 1:
            
            answer.add(A[now-1])
        
        if now + 1 <= n:
            
            answer.add(A[now+1])
    
    print(f'#{t} {len(answer)}')