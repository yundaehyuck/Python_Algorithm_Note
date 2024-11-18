from sys import stdin

#수평선 혹은 수직선 3개로 모든 점을 덮을 수 있는가?
n = int(stdin.readline())

X = {}
X_count = {}
Y = {}
Y_count = {}

#x좌표를 그룹으로 y좌표 묶고, y좌표 그룹으로 x좌표 묶어서 카운팅
for _ in range(n):
    
    x,y = map(int,stdin.readline().split())

    if X.get(x,0) == 0:
        
        X[x] = set()
    
    X[x].add(y)
    X_count[x] = X_count.get(x,0) + 1

    if Y.get(y,0) == 0:
        
        Y[y] = set()

    Y[y].add(x)
    Y_count[y] = Y_count.get(y,0) + 1

#각 그룹이 3개 이하라면 3개 직선으로 모두 덮을 수 있음
if len(X) <= 3 or len(Y) <= 3:
    
    print(1)

else:
    
    find = False

    #X좌표 기준으로 수직선으로 그어보고
    for x in X:
        
        count = 0

        for y in X[x]: #각 수직선이 지나는 y좌표에 대해서
            
            if Y_count[y] == 1: #해당 y좌표의 개수가 1개라면

                count += 1 #카운팅 해주고
        
        #전체 y좌표 그룹 개수만큼 수평선을 그어야하는데
        #y좌표 개수가 1개인 그룹으로는 수평선 안그어도 된다
        #그래서 두 값을 뺸 값이 2 이하라면 수평선을 2개 이하로 그으면 모든 점을 덮을 수 있다
        if len(Y) - count <= 2:
            
            find = True
            break
    
    if find:
        
        print(1)
    
    else:
        
        #Y좌표 기준으로 수평선 그어보고
        for y in Y:
            
            count = 0

            for x in Y[y]: #해당 수평선을 지나는 x좌표 들을 보고
                
                if X_count[x] == 1: #x좌표 개수가 1개라면 그 쪽으로는 수직선 안그어도 된다

                    count += 1
            
            #전체 x좌표 그룹 개수만큼 수직선을 그어야하는데
        #x좌표 개수가 1개인 그룹으로는 수직선 안그어도 된다
        #그래서 두 값을 뺸 값이 2 이하라면 수직선을 2개 이하로 그으면 모든 점을 덮을 수 있다
            if len(X) - count <= 2:
                
                find = True
                break
        
        if find:
            
            print(1)
        
        else:
            
            print(0)