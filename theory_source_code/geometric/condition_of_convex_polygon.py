#convex polygon이 될 조건
#"가장 긴 변의 길이가 나머지 변의 길이 합보다 작다"
from sys import stdin

z = int(stdin.readline())

for _ in range(z):
    
    n = int(stdin.readline())

    lines = list(map(int,stdin.readline().split()))

    if n < 3:
        
        print(0)
    
    else:

        lines.sort()

        remainder = sum(lines)

        for i in range(n-1,-1,-1):
            
            #최대 < (모든 변 길이합) - 최대이면 바로 break
            #최대 >= (모든 변 길이 합) - 최대 이면, 현재 최대 변은 선택 불가능
            if lines[i] >= remainder - lines[i]:
                
                remainder -= lines[i]
            
            else:
                
                break
        
        print(remainder)