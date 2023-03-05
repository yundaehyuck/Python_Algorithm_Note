from sys import stdin

def distance(a,b):
    
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)

t = int(stdin.readline())

for _ in range(t):
    
    points = []

    for _ in range(4):

        x,y = map(int,stdin.readline().split())

        points.append((x,y))

    
    points.sort()

    a = distance(points[0],points[1])
    b = distance(points[0],points[2])

    c = distance(points[0],points[3])

    if a == b and a+b == c:
        
        print(1)
    
    else:
        
        print(0)