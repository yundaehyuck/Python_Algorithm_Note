#n개의 구간 (l,r) 사이 정수를 하나씩 골라 합해서 0이 될 수 있는가?
from sys import stdin

n = int(stdin.readline())

L = 0
R = 0

interval = []
result = []

for _ in range(n):
    
    l,r = map(int,stdin.readline().split())
    interval.append((l,r))
    result.append(l)

    L += l
    R += r


#l의 합 <= 0 <= R의 합이면, X배열을 찾을 수 있다

if L <= 0 and R >= 0:
    
    print('Yes')
    
    #최초 Xi들을 Li로 초기화(result)
    
    #올려야하는 양은 -L만큼(Li들의 합)
    diff = -L

    for i in range(n):
        
        l,r = interval[i]
        
        #각 구간마다 Xi는 r-l만큼 최대로 올리거나,
        #diff만큼 올리거나 할 수 있다
        
        incre = min(diff,r-l)
        result[i] += incre
        diff -= incre
        
        #올려야하는 양 diff가 0이 되면 합이 전부 0이 된다는 뜻
        if diff == 0:
            
            break
    
    print(*result)


else:
    
    print('No')