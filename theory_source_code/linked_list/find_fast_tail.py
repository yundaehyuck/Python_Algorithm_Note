#단순 연결리스트
#꼬리를 바로 찾는 방법
from sys import stdin

n = int(stdin.readline())

s = [0]

for _ in range(n):
    
    c = stdin.readline().rstrip()
    s.append(c)

link1 = {} #i의 바로 뒤(next)
link2 = {} #i의 마지막 부분(tail)

#i > i
#i번 자기 자신이 i번의 마지막부분
for i in range(1,n+1):
    
    link2[i] = i

for _ in range(n-1):
    
    i,j = map(int,stdin.readline().split())
    
    #i > a1 > a2 > ... > ak > link2[i]
    #j > b1 > b2 > ... > bk > link2[j]

    #i > ... > link2[i] > j > .... > link2[j]

    #i > ... > (link2[i] = link2[j])
    
    #i,j가 들어온다면 i > j로 연결시켜줘야함
    #i의 마지막부분(link2[i]) 바로 뒤에 j를 연결시켜줘야함
    link1[link2[i]] = j
    
    #연결하고 나서, i의 마지막 부분을 변경시켜줘야한다.
    #j와 연결되었으니 j의 마지막부분(link2[j])이 i의 마지막부분(link2[i])이 된다
    link2[i] = link2[j]

answer = []

#i번부터 시작해서 i의 바로 next 부분을 차례대로 answer에 담는다
#i > i1 > i2 > ... 
while 1:

    answer.append(s[i])
    
    if link1.get(i,0) == 0:
        
        break
        
    i = link1[i]

print(''.join(answer))