"""
from sys import stdin

n = stdin.readline().rstrip()

len_n = len(n)

n = int(n)

r = int('1'*len_n) % n

period = [0]*n

period[r] = 1

while r != 0:

    r *= 10
    r += 1
    len_n += 1

    r %= n
    
    period[r] += 1
    
    if period[r] >= 2:
        len_n = -1
        break

print(len_n)
"""

from sys import stdin

n = stdin.readline().rstrip()

len_n = len(n)

n = int(n)

if n % 2 == 0 or n % 5 == 0:
    
    print(-1)

else:

    r = int('1'*len_n) % n

    while r != 0:
        
        r *= 10
        r += 1
        len_n += 1

        r %= n

    print(len_n)