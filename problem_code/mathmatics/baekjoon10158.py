#https://www.acmicpc.net/problem/10158

from sys import stdin

w,h = map(int,stdin.readline().split())

p,q = map(int,stdin.readline().split())

t = int(stdin.readline())

x_t = t
y_t = t

if w-p > x_t:
    
    p = p+x_t

else:
    
    x_t -= w-p

    if (x_t//w) % 2 == 0:

        p = w-(x_t%w)

    else:

        p = x_t%w

if h-q > y_t:
    
    q = q+y_t

else:
    
    y_t -= h-q

    if (y_t//h) % 2 == 0:
        
        q = h-(y_t%h)
    
    else:
        
        q = y_t%h

print(p,q)