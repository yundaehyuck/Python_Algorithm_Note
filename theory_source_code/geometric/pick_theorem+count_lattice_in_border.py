from sys import stdin

#pick's theorem
#A = I+B/2-1 >>> 2A = 2I+B-2
#2I = 2A+2 - B >>> I = (2A+2-B)//2

#area of polygon
#정수 연산을 위해 1/2을 하지 않는다
def area(x,y):
    
    a = 0

    for i in range(m):
        
        a += x[i]*y[i+1]
        a -= y[i]*x[i+1]
    
    if a < 0:
        
        a = -a
    
    return a

#count lattice in edge
#num of (a,b),(c,d) = gcd(c-a,d-b)+1
def count_lattice_edge(x,y):

    #반드시 절댓값을 취해줘야한다.
    #그렇지 않으면 (1,1),(0,1)의 경우 a = -1, b = 0이고 
    #gcd = -1이 나오기 때문에, a-1 = -2가 되어 문제 생긴다 
    a = abs(y[1]-x[1])
    b = abs(y[0]-x[0])

    while b != 0:
        
        a,b = b,a%b
    
    return a-1

T = int(stdin.readline())

for t in range(1,T+1):
    
    m = int(stdin.readline())

    x = []
    y = []

    a = 0
    b = 0

    for _ in range(m):
        
        dx,dy = map(int,stdin.readline().split())

        a += dx
        b += dy

        x.append(a)
        y.append(b)
    
    x.append(x[0])
    y.append(y[0])

    a = area(x,y)

    e = 0

    for i in range(m):

        e += count_lattice_edge((x[i],y[i]),(x[i+1],y[i+1]))
        
    e += m #counting num of verticle in m-polygon

    #pick's theorem 2A = 2I + B - 2(2A = 2I + E - 2)
    i = a+ 2 - e 

    print(f'Scenario #{t}:')
    print(i//2,e,a/2)
    print()