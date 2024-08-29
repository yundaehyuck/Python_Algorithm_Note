#두 직사각형 (x1,y1),(x2,y2)와 (x3,y3), (x4,y4)가 서로 겹치는 영역의 좌표 (a,b), (c,d)
#왼쪽 하단, 오른쪽 상단
def intersect(x1,y1,x2,y2,x3,y3,x4,y4):
     
    a = max(x1,x3)
    b = max(y1,y3)
    c = min(x2,x4)
    d = min(y2,y4)
 
    if a > c or b > d:
         
        return -1,-1,-1,-1
     
    else:
         
        return a,b,c,d
 
 #(a,b), (c,d) 흰색 종이 위에
 #(x1,y1), (x2,y2)와 (x3,y3), (x4,y4) 두 검은색 종이를 올릴떄
 #흰색 종이의 면적이 남아있는가 아닌가?

 #흰색 종이 영역 A
 #검은색 종이1과 겹치는 영역 B
 #검은색 종이2와 겹치는 영역 C
 #검은색 종이1,2가 서로 겹치는 영역 D
 #A - (B+C-D)가 0보다 큰가 아닌가
T = int(input())
 
for _ in range(T):
 
    a,b,c,d = map(int,input().split())
 
    white = (c-a)*(d-b)
 
    x1,y1,x2,y2 = map(int,input().split())
 
    x3,y3,x4,y4 = map(int,input().split())
 
    p,q,r,s = intersect(a,b,c,d,x1,y1,x2,y2)
     
    if p == -1 and q == -1 and r == -1 and s == -1:
 
        black1 = 0
 
    else:
 
        black1 = (r-p)*(s-q)
 
    p,q,r,s = intersect(a,b,c,d,x3,y3,x4,y4)
     
    if p == -1 and q == -1 and r == -1 and s == -1:
 
        black2 = 0
 
    else:
 
        black2 = (r-p)*(s-q)
             
    p,q,r,s = intersect(x1,y1,x2,y2,x3,y3,x4,y4)
     
    if p == -1 and q == -1 and r == -1 and s == -1:
         
        black3 = 0
     
    else:
         
        pp,qq,rr,ss = intersect(a,b,c,d,p,q,r,s)
 
        if pp == -1 and qq == -1 and rr == -1 and ss == -1:
             
            black3 = 0
         
        else:
             
            black3 = (rr-pp)*(ss-qq)
 
    x = white - (black1+black2-black3)
 
    if x <= 0:
         
        print('NO')
     
    else:
         
        print('YES')