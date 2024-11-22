#a1b1 + a2b2+ ... + anbn의 최솟값을 찾는 문제
#a1 >= a2 >= ... an으로 내림차순 정렬
#b1 <= b2 <= ... <= bn으로 오름차순 정렬
#하고 나서 a1b1+...+anbn을 하면 그것이 최솟값
from sys import stdin

T = int(stdin.readline())

for t in range(1,T+1):
    
    n = int(stdin.readline())
    
    A = list(map(int,stdin.readline().split()))
    B = list(map(int,stdin.readline().split()))

    A.sort(reverse = True)
    B.sort()

    x = 0

    for i in range(n):
        
        x += A[i]*B[i]
    
    print(f'Case #{t}: {x}')

"""
#돼지 무게 W, 팔때 얻는 이익 P, 1킬로그램당 1킬로미터 운반시 드는 추가비용 t, 각 마을 거리 D
#돼지 팔면 얻는 이익 WP, 운반비용 WDt
#wp-wdt = w(p-dt)
#i번째 돼지 wi를 각 j번째 마을에 팔면 얻는 이익 (p-dt)
#두 배열 W, P-Dt를 오름차순 정렬해서 동일한 위치끼리 곱해서 합하면 그것이 최댓값
n,t = map(int,input().split())

W = list(map(int,input().split()))
D = list(map(int,input().split()))
P = list(map(int,input().split()))

A = []
B = []

for i in range(n):
    
    w = W[i]
    A.append((w,i))

for i in range(n):
    
    p,d = P[i],D[i]

    B.append(((p-d*t),i))
    
A.sort()
B.sort()

answer = [0]*n

for i in range(n):
    
    answer[B[i][1]] = A[i][1]+1

print(*answer)
"""