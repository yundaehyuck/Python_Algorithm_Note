#A,B,C를 이은 선분이 어떤 관계를 이루는가

#두 벡터 a,b의 외적
def ccw(a,b):
    
    return (a[1]*b[2] - a[2]*b[1]) - (a[0]*b[2] - a[2]*b[0]) + (a[0]*b[1] - a[1]*b[0])

#세 점 A,B,C의 좌표
x1,y1 = map(int,input().split()) #A

x2,y2 = map(int,input().split()) #B

x3,y3 = map(int,input().split()) #C

#2차원이면, z축 좌표를 0으로 
a = [x2 - x1, y2 - y1, 0] #AB
b = [x3 - x1, y3 - y1, 0] #AC

x = ccw(a,b)

if x > 0: #A,B,C를 이은 선분이 반시계방향
    
    print(1)

elif x < 0: #A,B,C를 이은 선분이 시계방향
    
    print(-1)

else: #A,B,C를 이은 선분이 직선
    
    print(0)