#ay - bx = 2를 만족하는 a,b 구하기
def extended_gcd(a,b):
    
    before_x = 1
    before_y = 0

    x = 0
    y = 1

    while b != 0:
        
        q,r = a//b, a%b
        a,b = b,r

        before_x,x = x, before_x - x*q
        before_y,y = y, before_y - y*q
    
    return a,before_x, before_y

x,y = map(int,input().split())

#bx - ay = g를 만족하는 g,b,a가 구해짐
g,b,a = extended_gcd(x,-y)

if abs(g) == 2:
    
    print(a,b)

else:

    #bx - ay = 2 형태로 만들려면 양변을 g로 나누고 2배 해야함
    #a,b가 g로 안나누어 떨어진다면 만족하는 정수 a,b가 존재하지 않는다
    if a % g != 0 or b % g != 0:
        
        print(-1)

    else:

        print(2*a//g,2*b//g)