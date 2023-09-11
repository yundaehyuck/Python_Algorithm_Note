def meet_point(x1,y1,x2,y2,x3,y3,x4,y4):
    
    if x2 == x1: #(A,B)가 y축에 평행
        
        b = (y4-y3)/(x4-x3)

        x = x1
        y = b*(x-x3)+y3

    else: #(A,B)가 y축에 평행하지 않음
        
        a = (y2-y1)/(x2-x1) #y = a(x-x1)+y1

        if x3 == x4: #(C,D)가 y축에 평행
            
            x = x3
            y = a*(x-x1)+y1
            
        else:
            
            b = (y4-y3)/(x4-x3)  #y = b(x-x3)+y3

            x = (y3-y1 + a*x1-b*x3)/(a-b) #a(x-x1)+y1 = b(x-x3)+y3 >> (a-b)x = y3-y1-bx3+ax1
            y = a*(x-x1)+y1

    return (x,y)


"""#A(x1,y1), B(x2,y2), C(x3,y3), D(x4,y4)가 주어질때 AB, CD의 교점을 구하는 공식
def meet_point(x1,y1,x2,y2,x3,y3,x4,y4):
    
    ax = (x1-x2)
    bx = (x3-x4)
    
    ay = (y1-y2)
    by = (y3-y4)
    
    c = x1*y2 - y1*x2
    d = x3*y4 - y3*x4
    
    x = (c*bx - ax*d)/(ax*by - ay*bx)
    y = (c*by - ay*d)/(ax*by - ay*bx)
    
    return (x,y)
"""