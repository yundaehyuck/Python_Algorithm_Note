from collections import deque
from sys import stdin

#어떤 정수 n의 0과 1로만 이루어진 배수 찾기
while 1:
    
    n = int(stdin.readline())

    if n == 0:
        
        break

    if 1 % n == 0:
        
        print(1)
    
    else:
        
        #1부터 시작해서 뒤에 0,1을 붙여나가면 모든 경우를 검사할 수 있다
        #n으로 나눈 나머지가 0이면 그 수는 n의 배수이다
        #0을 붙이는건 10배, 1을 붙이는건 10배하고 1을 더하는 것
        #곱과 합은 모듈로 연산이 가능하므로 어떤 수가 서로 다르더라도 나머지가 서로 같으면 같은 수이다
        #나머지를 visited로 체크해서 이미 있는 경우는 더 이상 계산하지 않아도 되므로 중복을 줄일 수 있다
        queue = deque([(1,1)])

        visited = [0]*n
        visited[1] = 1

        answer = -1

        r1 = 10 % n

        while queue:
            
            #(원래 수, 나머지)를 둬야 원래 수를 출력할 수 있음
            m,r = queue.popleft()

            #뒤에 0을 붙이는 경우
            dr = r*r1
            dr %= n

            if dr == 0:
                
                answer = m*10
                break

            if visited[dr] == 0:
                
                visited[dr] = 1
                queue.append((m*10,dr))
            
            #뒤에 1을 붙이는 경우
            dr = r*r1 + 1
            dr %= n

            if dr == 0:
                
                answer = m*10+1
                break
            
            if visited[dr] == 0:
                
                visited[dr] = 1
                queue.append((m*10+1,dr))

        print(answer)