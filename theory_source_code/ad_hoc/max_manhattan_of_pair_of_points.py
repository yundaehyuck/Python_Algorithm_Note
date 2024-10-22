#주어진 n개의 점들 중 (xi,yi), (xj,yj)의 가장 큰 맨해튼 거리
n = int(input())

A = []
B = []

for _ in range(n):
    
    x,y = map(int,input().split())
    A.append(x+y)
    B.append(x-y)

A.sort()
B.sort()

#|xi-xj| + |yi-yj| = (xi+yi)-(xj+yj), -( (xi+yi)-(xj+yj) ) , (xi-yi) - (xj-yj), - ( (xi-yi) - (xj-yj) )
#xi+yi, xi-yi의 값을 O(N)에 구하고
#max(xi+yi) - min(xi+yi)
#max(xi-yi) - min(xi-yi)
#둘 중 더 큰 값을 고르면 된다

print(max((A[-1] - A[0]), (B[-1] - B[0])))