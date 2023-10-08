import math
from sys import stdin

q = int(stdin.readline())

a = 0

for _ in range(q):
    
    s = stdin.readline().rstrip()

    if s[0] == '+':
        
        a += int(s[1:])
    
    else:
        
        a -= int(s[1:])
    
    if a == 0:
        
        print(0)
    
    else:
        
        print(2**int(math.log2(a)))