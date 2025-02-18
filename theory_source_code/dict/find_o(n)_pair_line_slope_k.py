#직선의 기울기가 k인 두 점을 선택하는 경우의 수
#(x1,y1), (x2,y2)가 직선의 기울기가 k라는 뜻은 y2-y1/x2-x1 = k
#y2-y1 = kx2 - kx1
#y2 - kx2 = y1 - kx1
#따라서, 두 점의 y-kx값이 서로 같으면 두 점을 이은 직선의 기울기가 k이다
from sys import stdin

n,k = map(int,stdin.readline().split())

#dict에 y-kx값을 저장해두고
H = {}

for _ in range(n):
    
    a,b = map(int,stdin.readline().split())
    H[b-k*a] = H.get(b-k*a,0) + 1

count = 0

#(x,y)에 대하여 y-kx값을 가지는 (x,y)의 개수가 c개라면, 이 중 2개를 선택하는 방법의 수 cC2 * 자리바꾸기 2! = c(c-1)
for v in H:

    c = H[v]

    count += (c*(c-1))

print(count)