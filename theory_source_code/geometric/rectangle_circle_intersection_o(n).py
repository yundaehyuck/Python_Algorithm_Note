#원과 직사각형 내부 교집합에 존재하는 정수 격자점의 개수를 O(N)에 찾기

x1,y1,x2,y2 = map(int,input().split())
x3,y3,r = map(int,input().split())

x2 -= x1
x3 -= x1
y2 -= y1
y3 -= y1

count = 0

for x in range(x2+1):
    
    #원 내부에 있는 모든 점 [x3-r,x3+r]에 대하여...
    if x >= x3-r and x <= x3+r:
        
        #원의 방정식 (x-x3)**2+(y-y3)**2 = r**2를 이용해 
        #원 둘레 위의 y좌표 a,b를 찾는다
        v = (r**2 - (x-x3)**2)**(1/2)
        v = int(v)
        
        a = v + y3
        b = -v + y3

        #a,b 값에 따라 직사각형 내부의 점을 잘 결정해준다..
        if b < 0:
            
            if a > y2:
                
                count += (y2+1)
            
            elif a >= 0:
                
                count += (a+1)
        
        elif b <= y2:
            
            if a > y2:
                
                count += (y2-b+1)
            
            else:
                
                count += (a-b+1)
        
                
print(count)