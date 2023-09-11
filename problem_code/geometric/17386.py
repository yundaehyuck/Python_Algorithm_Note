def intersect(x1,y1,x2,y2,x3,y3,x4,y4):
    
    a = ccw((x2-x1,y2-y1),(x3-x1,y3-y1)) 
    b = ccw((x2-x1,y2-y1),(x4-x1,y4-y1))

    if a*b < 0:
        
        return True
    
    else:
        
        return False    

def ccw(x,y):
    
    return x[0]*y[1] - x[1]*y[0]

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())


f1 = intersect(x1,y1,x2,y2,x3,y3,x4,y4) #A,B를 기준으로 A,B,C와 A,B,D의 CCW판단
f2 = intersect(x3,y3,x4,y4,x1,y1,x2,y2) #C,D를 기준으로 C,D,A와 C,D,B의 CCW판단

if f1 == True and f2 == True:
    
    print(1)

else:
    
    print(0)