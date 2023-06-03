from sys import stdin

def find_parent(x,parent):
    
    if x != parent[x]:

        parent[x] = find_parent(parent[x],parent)

    return parent[x]

def union(a,b):
    
    a = find_parent(a,parent)
    b = find_parent(b,parent)

    if parent[a] < parent[b]:
        
        parent[a] = b

    else:
        
        parent[b] = a

n,m =map(int,stdin.readline().split())

parent = [i for i in range(n+1)]

for _ in range(m):
    
    u,v = map(int,stdin.readline().split())

    union(u,v)

k = int(stdin.readline())

#x,y가 서로 다르더라도 대표자가 서로 같은 경우가 존재하므로
#set을 사용해 중복을 제거함
good = set()

for _ in range(k):
    
    x,y = map(int,stdin.readline().split())

    x = find_parent(x,parent)
    y = find_parent(y,parent)
    
    #무방향 그래프이므로, (x,y)를 연결하나 (y,x)를 연결하나 서로 같다
    if x > y:
      x,y = y,x
      
    good.add((x,y))

Q = int(input())

for _ in range(Q):
    
    p,q = map(int,stdin.readline().split())

    p = find_parent(p,parent)
    q = find_parent(q,parent)
    
    if p > q:
      p,q = q,p
    
    #(p,q)가 good에 존재한다는 뜻은
    #(p,q)를 연결하면 good의 어느 두 정점이 서로 연결된다는 뜻이다.
    #그러므로 good 그래프가 되지 않는다.
    if (p,q) in good:
        
        print('No')
    
    else:
        
        print('Yes')