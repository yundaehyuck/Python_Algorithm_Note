#뒤에서부터 정수를 mod로 나눈 나머지가 0,1,2,...,mod-1이 각각 최소 1번 이상 나온 가장 짧은 범위
from sys import stdin

q,mod = map(int,stdin.readline().split())

A = []

#visited[i] = 정수를 MOD로 나눈 나머지가 i인 원소가 스택에서 가장 마지막에 나타나는 위치
visited = [[] for _ in range(mod)]

for _ in range(q):
    
    Q = stdin.readline().rstrip().split()

    #1번 쿼리는 스택에 정수를 넣는 쿼리
    #저장할때마다 스택에 나타나는 위치를 저장해두면 그것이 스택에서 해당 원소가 마지막에 나타나는 위치
    if Q[0] == '1':
        
        m = int(Q[1]) % mod
        A.append(m)
        visited[m].append(len(A)-1)
    
    #2번 쿼리는 스택에서 마지막 원소를 제거하는 쿼리
    #마지막 원소를 제거했으므로, visited[x]에서 마지막 원소(=마지막으론 나타나는 위치)를 제거
    elif Q[0] == '2':
        
        if len(A) == 0:
            
            continue
            
        x = A.pop()
        
        visited[x].pop()
    
    #3번 쿼리는 스택에서 뒤에서부터 0,1,2,..,MOD-1이 1번 이상 나오는 가장 짧은 구간
    else:
        
        no = False
        j = len(A)+10
        
        #visited[i]들을 검사해서, 하나라도 visited[i]가 빈 배열이면, 불가능
        #가능하다면 visited[i][-1]의 최솟값이 정답
        #0,1,2,..,mod-1이 가장 마지막에 나타나는 인덱스들의 최솟값이 정답일 것
        # [0,1,2,3,3,1,2,0,2,2,3,1]이라고 한다면?
        # 0은 7번, 1은 11번, 2는 9번, 3은 10번
        #뒤에서부터 7번 위치까지 [0,2,2,3,1]이 정답일것
        for i in range(mod):
            
            if len(visited[i]) == 0:
                
                no = True
                break
            
            else:
                
                if j > visited[i][-1]:
                    
                    j = visited[i][-1]
                    
        if no:
            
            print(-1)
        
        else:
            
            print(len(A) - j)