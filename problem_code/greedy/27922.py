from sys import stdin

n,k = map(int,stdin.readline().split())

lecture = []

#애초에 원소를 (a+b,b+c,a+c)로 구성하고..
for _ in range(n):
    
    a,b,c = map(int,stdin.readline().split())
    lecture.append((a+b,b+c,c+a))

answer = 0

#a+b, b+c, c+a 각각 기준으로 내림차순 정렬한다음
#각각에서 k개를 골라 합하면 각각에서 최댓값이 될거고
#전체에서 최댓값 비교해서 갱신
for i in range(3):

    lecture.sort(key = lambda item: -item[i])

    a = 0

    for j in range(k):

        a += lecture[j][i]
        
    if answer < a:
        
        answer = a

print(answer)