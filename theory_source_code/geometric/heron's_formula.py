from sys import stdin

pi = 3.141592653589793

while 1:
    
    try:
        x1,y1,x2,y2,x3,y3 = map(float,input().split())

        a = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
        b = ((x3-x2)**2 + (y3-y2)**2)**(1/2)
        c = ((x3-x1)**2 + (y3-y1)**2)**(1/2)

        s = (a+b+c)/2

        #헤론의 공식
        S = (s*(s-a)*(s-b)*(s-c))**(1/2)

        #외접원의 반지름

        R = a*b*c/(4*S)

        print(f"{2*pi*R:.2f}")
    
    except:
        break