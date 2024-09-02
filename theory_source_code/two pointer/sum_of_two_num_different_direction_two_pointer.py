#두 수의 합이 s가 되는 경우의 수

from sys import stdin

n,s = map(int,stdin.readline().split())

A = []

for _ in range(n):
    
    a = int(stdin.readline())
    A.append(a)

#A가 정렬되어있다면,
# A[i]+A[j] = s이므로 i = 0,1,2,..로 증가한다면 j = n-1,n-2,..로 감소해야한다
#i가 증가할때 j를 감소시켜 A[i]+A[j] > s에서 A[i] + A[j] = s이면 counting
#A[i] +A[j] < s이면 i를 증가시킨다.
#어차피 정렬되어있으므로 j = n-1로 돌아갈필요가 없다는게 포인트
j = n-1

count = 0

for i in range(n):

    while i < j:
        
        v = A[i] + A[j]

        if v == s:

            count += 1
            break

        elif v > s:

            j -= 1

        else:

            break

print(count)