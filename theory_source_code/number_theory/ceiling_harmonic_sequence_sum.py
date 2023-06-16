#올림으로 된 조화수열의 합

import math
from sys import stdin

n = int(stdin.readline())

if n == 1:
    
    print(1)

else:

    answer = 0

    i = 1

    x = math.ceil(n/i)
    
    #i가 가지는 범위의 부등식 하한과 상한을 정확히 정의
    start = math.ceil(n/x)
    end = math.ceil(n/(x-1))

    while 1:

        answer += (end-start)*x

        i += (end-start)

        x = math.ceil(n/i)

        if x == 1:

            break

        start = math.ceil(n/x)
        end = math.ceil(n/(x-1))
    
    #반복문을 탈출하면, x = 1인 경우 하나가 빠지게 된다
    print(answer+1)