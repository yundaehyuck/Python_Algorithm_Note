#반복문

def iterative_extended_gcd(a,b):
    
    #초기값 설정
    #x0,y0
    before_x = 1
    before_y = 0
    
    #x1,y1
    x = 0
    y = 1
    
    #유클리드 알고리즘
    while b != 0:
        
        #미리 q = a//b를 구해놔야, b가 0일때 a//b를 하지 않는다
        q,r = a//b, a%b
        a,b = b,r
        
        #점화식에 의해 업데이트
        before_x,x = x, before_x - x*q
        before_y,y = y, before_y - y*q
    
    #b=0일때, x,y가 한번 더 업데이트 되어 before_x,before_y에 들어가므로
    return a,before_x,before_y