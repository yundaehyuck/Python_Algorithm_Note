from sys import stdin

# 두 선분의 교차 여부 판정
def intersect(x1,y1,x2,y2,x3,y3,x4,y4): #A,B,C,D

    a = ccw((x2-x1,y2-y1),(x3-x1,y3-y1))  #f1 = ccw(A,B,C)
    b = ccw((x2-x1,y2-y1),(x4-x1,y4-y1))  #f2 = ccw(A,B,D)

    f1 = a*b

    c = ccw((x4-x3,y4-y3),(x1-x3,y1-y3)) #f3 = ccw(C,D,A)
    d = ccw((x4-x3,y4-y3),(x2-x3,y2-y3)) #f4 = ccw(C,D,B)

    f2 = c*d

    if f1 < 0 and f2 < 0: # 1)단순하게 교차하는 경우
        
        return 2
    
    #2) 양 끝점중 하나에서 교점을 가지는 경우, 4개의 점이 일직선 위에 있는 경우
    elif f1 == 0 and f2 == 0:
        
        #f1,f2중 하나가 0이 아니고 f3,f4중 하나가 0이 아니라면.. 양 끝점에서 교점을 반드시 가진다.
        if (a != 0 or b != 0) and (c != 0 or d != 0): 
            
            return 1
        
        #4개의 점이 일직선 위에 있는 경우
        #A - C - B - D인가? C - A - D - B인가? 서로 포개질수 있는지 X,Y 크기로 비교
        elif a == 0 and b == 0 and c == 0 and d == 0: #(x1,y1),(x2,y2),(x3,y3),(x4,y4) 모두 일직선
            
            #양 끝점에서 교점을 가지는 경우
            #A - C=B - D이거나 C - A=D - B로... 이렇게도 가능하지..
            if (x2 == x3 and y2 == y3) or (x1 == x4 and y1 == y4):

                return 1
            
            #양 끝점이 아닌데 서로 포개지는 경우
            #A - C - B - D이거나 C - A - D - B이거나..
            elif x1 <= x3 and x3 <= x2 and min(y1,y2) <= y3 and y3 <= max(y1,y2): #(x1,y1), (x3,y3), (x2,y2)

                return 3

            elif x1 <= x4 and x4 <= x2 and min(y1,y2) <= y4 and y4 <= max(y1,y2): #(x1,y1),(x4,y4),(x2,y2)

                return 3

            elif x3 <= x1 and x1 <= x4 and min(y3,y4) <= y1 and y1 <= max(y3,y4): #(x3,y3), (x1,y1), (x4,y4)

                return 3

            elif x3 <= x2 and x2 <= x4 and min(y3,y4) <= y2 and y2 <= max(y3,y4): #(x3,y3),(x2,y2),(x4,y4)

                return 3

            else:

                return 0

    elif a == 0 and b != 0 and c != 0 and d != 0: #(x1,y1),(x2,y2),(x3,y3)가 일직선

        if x1 <= x3 and x3 <= x2 and min(y1,y2) <= y3 and y3 <= max(y1,y2):

            return 1

        else:

            return 0

    elif a != 0 and b == 0 and c != 0 and d != 0:#(x1,y1),(x2,y2),(x4,y4)가 일직선

        if x1 <= x4 and x4 <= x2 and min(y1,y2) <= y4 and y4 <= max(y1,y2):

            return 1

        else:

            return 0

    elif a != 0 and b != 0 and c == 0 and d != 0: #(x3,y3),(x4,y4),(x1,y1)이 일직선

        if x3 <= x1 and x1 <= x4 and min(y3,y4) <= y1 and y1 <= max(y3,y4):

            return 1

        else:

            return 0

    elif a != 0 and b != 0 and c != 0 and d == 0: #(x3,y3),(x4,y4),(x2,y2)이 일직선

        if x3 <= x2 and x2 <= x4 and min(y3,y4) <= y2 and y2 <= max(y3,y4):

            return 1

        else:

            return 0
    
    else:
        
        return 0

def ccw(x,y):

    return x[0]*y[1] - x[1]*y[0]

n = int(stdin.readline())

points = []

#선분을 구성할때, X좌표 기준으로 오름차순 정렬
#X좌표가 같으면 Y좌표 기준으로 오름차순 정렬
for _ in range(n):

    x,y,z,w = map(int,stdin.readline().split())

    if x > z:
        
        x,z = z,x
        y,w = w,y
    
    elif x == z:
        
        if y > w:
        
            y,w = w,y

    points.append((x,y,z,w))

answer = [[3]*n for _ in range(n)]

for i in range(n-1):

    for j in range(i+1,n):

        x1,y1,x2,y2 = points[i]

        x3,y3,x4,y4 = points[j]

        f = intersect(x1,y1,x2,y2,x3,y3,x4,y4)
        
        #(A,B)와 (C,D)의 교차 여부랑 (C,D)와 (A,B)의 교차 여부는 같다
        answer[i][j] = f
        answer[j][i] = f

for row in answer:
    
    print(''.join(map(str,row)))