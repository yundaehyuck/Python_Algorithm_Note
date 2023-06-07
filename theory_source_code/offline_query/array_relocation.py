#offline query
#query마다 배열을 재배치

n,q = map(int,input().split())

#query에 답하지 않고 모든 query를 일단 구성한다
query_list = []

for _ in range(q):
    
    x = int(input())
    query_list.append(x)

visited = [0]*(n+1)

answer = [0]*n

left = 0
right = -1

#query를 거꾸로 순회해서, 빈 배열 answer에 채워 넣는다.
for i in range(q-1,-1,-1):
    
    x = query_list[i]
    
    #x가 양수라면, 왼쪽부터 차례대로 채워넣는다.
    if x > 0:
        
        #이미 기록한 숫자라면 스킵
        if visited[x] == 1:
            
            continue
        
        else:
            
            #마지막에 나온 양수 query일수록 맨 왼쪽에 배치된다.
            #거꾸로 순회하기 때문에 다음 query에 채워넣을때는 left + 1에 채워넣기만 하면 된다
            answer[left] = x
            left += 1
            visited[x] = 1 #이미 나온 숫자인지 확인하기 위해
    
    #음수라면 오른쪽부터 채워넣는다
    elif x < 0:
        
        #이미 나온 숫자라면 스킵
        if visited[-x] == 1:
            
            continue
        
        else:
            
            #마지막에 나온 음수 query일수록 맨 오른쪽에 배치된다.
            #거꾸로 순회하기 때문에 다음 query에 채워넣을때는 right - 1에 채워넣기만 하면 된다
            answer[right] = -x
            right -= 1
            visited[-x] = 1

#query에 등장하지 않아 아직 채워넣지 않은 숫자를 왼쪽부터 채워넣는다
for i in range(1,n+1):
    
    if visited[i] == 0:
        
        answer[left] = i
        left += 1

print(*answer)