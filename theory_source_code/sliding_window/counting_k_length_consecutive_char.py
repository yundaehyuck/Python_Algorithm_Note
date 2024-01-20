#한 줄에서 연속한 o의 개수가 k개가 되도록 .을 o로 바꾸는 최소 횟수
from sys import stdin

h,w,k = map(int,stdin.readline().split())

maps = [stdin.readline().rstrip() for _ in range(h)]

INF = 1000000000000000000000000000000000

answer = INF

def check(row,k):

    o = 0
    x = 0

    result = INF

    if len(row) >= k: #한 줄이 k 이상이어야 가능
        
        #먼저 0 ~ k-1 구간에서 o의 개수와 x의 개수를 모두 센다
        for i in range(k):
        
            if row[i] == 'o':
                
                o += 1
            
            elif row[i] == 'x':
                
                x += 1
        
        #한 구간에서 x가 0개여야, 길이가 k인 연속한 o가 될 수 있다
        if x == 0:
            
            if result > k - o:
                
                result = k - o #그러면 (k - (o의 개수))만큼 .을 o로 바꾸면 된다
        
        #이제 1~len(row)-k-1까지 시작점을 이동시킨다
        for i in range(1,len(row)-k-1):
            
            #구간의 시작점이 i일때 i-1번 자리의 o나 x가 사라진다
            if row[i-1] == 'o':
                
                o -= 1
            
            elif row[i-1] == 'x':
                
                x -= 1
            
            #k-1+i번 자리의 o나 x가 추가된다
            if row[k-1+i] == 'o':
                
                o += 1
            
            elif row[k-1+i] == 'x':
                
                x += 1
            
            #마찬가지로 한 구간에서 x가 0개여야 길이가 k인 연속한 o가 가능하다.
            #항상 최솟값으로 갱신
            if x == 0 and result > k - o:
                
                result = k - o
    
    return result

#행에 대해서 모두 체크
for row in maps:

    value = check(row,k)

    if answer > value:

        answer = value

#열에 대해서 모두 체크
for col in zip(*maps):

    value = check(col,k)

    if answer > value:

        answer = value

#모두 체크해도 INF라면, 불가능한 것이므로 -1을 출력
if answer == INF:

    print(-1)

else:

    print(answer)