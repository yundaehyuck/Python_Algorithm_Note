from sys import stdin

n,q = map(int,stdin.readline().split())

A = list(map(int,stdin.readline().split()))

box = [0]*(n+1)

for i in range(1,n+1):

    box[i] = set([A[i-1]])

for _ in range(q):

    a,b = map(int,stdin.readline().split())

    #작은 집합에서 큰 집합으로 합치는 테크닉(smaller to larger)
    #a에서 b로 옮기고 a를 빈 상자로 만들지만..
    #반대로 생각하면 b에서 a로 옮긴 다음 a라는 이름을 b로 바꿔주면, 
    #a에서 b로 옮기는거나 결과는 마찬가지다. 
    if len(box[a]) > len(box[b]):
        
        box[a],box[b] = box[b],box[a]

    for c in box[a]:

        box[b].add(c)

    box[a] = set()

    print(len(box[b]))