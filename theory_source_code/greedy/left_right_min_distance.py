#boj 1461
from sys import stdin

n,m = map(int,stdin.readline().split())

A = list(map(int,stdin.readline().split()))

#A를 오름차순으로 정렬해놓고
A.sort()

minus = []
plus = []

a = 0
b = 0

#음수와 양수방향을 따로 배열에 모아둔다
for i in range(n):
    
    if A[i] < 0:
        
        minus.append(A[i])
        a += 1
    
    else:
        
        plus.append(A[i])
        b += 1

answer = 0

#A배열을 오름차순 정렬했기때문에
#음수방향은 이미 내림차순 정렬(절댓값 기준으로)되어 있고
#양수방향만 내림차순으로 재정렬하면 된다
plus.sort(reverse=True) 

#각 방향을 정방향으로 순회해서 m개씩 집어가는데
#m개씩 집어가서 0번 원소의 2배를 더해준다는 의미는
#m으로 나눈 나머지가 0인 인덱스의 원소의 2배를 더해준다는 의미다.
for i in range(a):
    
    if i % m == 0:

        answer += -2*minus[i]

for j in range(b):
    
    if j % m == 0:
        
        answer += 2*plus[j]

#a가 0이라는 것은 양수방향만 존재한다는 의미다.
#양수방향에서 최댓값은 0번 원소에
if a == 0:
    
    answer -= plus[0]

#b가 0이라는 것은 음수방향만 존재한다는 의미다.
#음수방향에서 절댓값이 최대인 원소는 0번 원소에
#음수를 빼주는건 더해주는거니까
elif b == 0:
    
    answer += minus[0]

#a,b가 0이 아니면, 음수방향 양수방향 둘다 있다
#각 방향에서 절댓값이 최대인 원소를 찾아
#그 방향은 마지막에 가면 다시 돌아가지 않아도 되니 이득을 본다
#다시 돌아가지 않아도 되니, 그 거리만큼을 이미 더해준 값에 빼준다
else:

    answer -= max(-minus[0],plus[0])

print(answer)