from collections import deque

#인접한 원소의 곱의 합이 최대가 되도록

n = int(input())

A = list(map(int,input().split()))

#양수는 양수끼리, 음수는 음수끼리 곱해야 최대
minus = []
plus = []

for i in range(n):
    
    if A[i] <= 0:
        
        minus.append(A[i])
    
    else:
        
        plus.append(A[i])

#절댓값이 큰 값부터 작은값까지 순서대로 왼쪽,오른쪽 번갈아 배치하는게 최대
#a1 > a2 > ... > an이면 
#a5 a3 a1 a2 a4 a6 ...

B = deque([])
C = deque([])

minus.sort()
plus.sort()

if len(plus) >= 1:

    B.append(plus[-1])
    f = False

    for i in range(len(plus)-2,-1,-1):

        if f == False:

            B.append(plus[i])
            f = True
        
        else:
            
            B.appendleft(plus[i])
            f = False

if len(minus) >= 1:

    C.append(minus[0])
    f = False

    for i in range(1,len(minus)):
        
        if f == False:
            
            C.append(minus[i])
            f = True

        else:
            
            C.appendleft(minus[i])
            f = False

#음수부분과 양수부분을 서로 붙여서 음수*양수가 1번만 일어나도록 만드는 것이 최대
#양끝의 곱이 최소가 되는 부분을 찾아 붙이도록
if len(B) >= 1 and len(C) >= 1:

    x1 = B[0]*C[0]
    x2 = B[0]*C[-1]
    x3 = B[-1]*C[0]
    x4 = B[-1]*C[-1]

    D = [x1,x2,x3,x4]
    D.sort()

    if D[-1] == x1:
        
        while C:
            
            c = C.popleft()
            B.appendleft(c)

    elif D[-1] == x2:
        
        while C:
            
            c = C.pop()
            B.appendleft(c)

    elif D[-1] == x3:
        
        while C:
            
            c = C.popleft()
            B.append(c)

    else:
        
        while C:
            
            c = C.pop()
            B.append(c)

if len(B) >= 1:

    print(*B)

elif len(C) >= 1:
    
    print(*C)