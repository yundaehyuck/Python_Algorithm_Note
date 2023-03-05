from sys import stdin

pi = 3.141592653589793

while 1:
    
    try:
        x1,y1,x2,y2,x3,y3 = map(float,stdin.readline().split())
        
        #b,a의 길이
        b = (x1-x3,y1-y3)
        b2 = (b[0]**2 + b[1]**2)**(1/2)

        a = (x2-x3,y2-y3)
        a2 = (a[0]**2 + a[1]**2)**(1/2)
        
        #b,a의 내적
        ab = a[0]*b[0] + a[1]*b[1]
        
        #내적의 성질
        cos = ab/(a2*b2)
        
        #cos과 sin의 관계
        sin = (1-(cos**2))**(1/2)
        
        c = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
        
        #sin법칙
        print(f"{pi*c/sin:.2f}")
    
    except:
        break