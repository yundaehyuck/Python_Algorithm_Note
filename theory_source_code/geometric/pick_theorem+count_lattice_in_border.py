from sys import stdin

#pick's theorem
#A = I+B/2-1 >>> 2A = 2I+B-2
#2I = 2A+2 - B >>> I = (2A+2-B)//2

#area of triangle
#정수 연산을 위해 1/2을 하지 않는다
def area(x,y):

    return abs(x[0]*y[1] - x[1]*y[0])

#count lattice in edge
#num of (a,b),(c,d) = gcd(c-a,d-b)+1
def count_lattice_edge(x,y):
    
    a = abs(y[0]-x[0])
    b = abs(y[1]-x[1])
    
    while b != 0:
        
        a,b = b,a%b
    
    return a - 1

while 1:

    x1,y1,x2,y2,x3,y3 = map(int,stdin.readline().split())

    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0 and x3 == 0 and y3 == 0:

        break

    else:

        x = [x2-x1,y2-y1]
        y = [x3-x1,y3-y1]

        a = area(x,y)

        b = count_lattice_edge((x1,y1),(x2,y2)) + count_lattice_edge((x2,y2),(x3,y3)) + count_lattice_edge((x3,y3),(x1,y1)) + 3
        
        #pick's theorem
        print((a+2 - b)//2)