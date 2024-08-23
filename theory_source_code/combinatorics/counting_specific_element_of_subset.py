#각각이 1/2로 선택하고 T <= t이면, X = t일때, X의 기댓값
#여사건을 이용한 특정 수가 적어도 하나 이상 포함된 부분집합의 개수
n = int(input())

t = list(map(int,input().split()))

#T를 정렬하고
t.sort()

t.append(1001)

x = 0
total = 0

count = 0

#a,a,a,a,...,a,b,b,b,b,...,b에서 b가 적어도 하나 포함된 부분집합의 개수
#전체 부분집합의 수 - a들로만 만든 부분집합의 수
#2**(a의 개수+b의 개수) - 2**(a의 개수)

#count = x보다 작은 값들의 개수
#i=처음부터 x까지의 개수
#x를 적어도 하나 포함하는 부분집합의 개수 = 2**(i) - 2**(count)
for i in range(n+1):

    if x < t[i]:
        
        total += (2**(i)-2**(count))*x
        x = t[i]
        count = i

print(total/(2**n))