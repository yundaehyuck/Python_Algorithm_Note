from sys import stdin

#가장 넓이가 큰 정사각형을 찾는 문제

T = int(stdin.readline())

for _ in range(T):
    
    n = int(stdin.readline())

    A = []
    H = {}

    for _ in range(n):
        
        x,y = map(int,stdin.readline().split())

        A.append((x,y))
        H[(x,y)] = 1
    
    answer = 0

    #두 점 A(x1,y1), B(x2,y2)에 대하여 AB = (x2-x1,y2-y1)을 90도 시계방향으로 회전하면
    #(-(y2-y1),(x2-x1))이고 이를 AD에 이동하면 D(x1-(y2-y1),y1+(x2-x1)), 
    #BC에 이동하면 C(x2-(y2-y1), y2+(x2-x1))으로 구할 수 있다
    #C,D가 존재하는지 hash로 체크
    for i in range(n):
        
        x1,y1 = A[i]

        for j in range(n):
            
            x2,y2 = A[j]

            if i == j:
                
                continue

            v = (x2-x1,y2-y1)
            vv = (-v[1],v[0])

            x3,y3 = x2-v[1],y2+v[0]
            x4,y4 = x1-v[1],y1+v[0]

            if H.get((x3,y3),0) == 1 and H.get((x4,y4),0) == 1:
                
                s = v[0]**2 + v[1]**2 #벡터 크기 제곱이 정사각형 넓이니까 루트 안써도 정수형 연산으로 넓이 구할 수 있음

                if answer < s:
                    
                    answer = s

    print(answer)