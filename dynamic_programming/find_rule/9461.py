#https://www.acmicpc.net/problem/9461
from sys import stdin

p = [0] * 101

p[1] = 1
p[2] = 1
p[3] = 1
p[4] = 2
p[5] = 2

for i in range(6,101):
    
    p[i] = p[i-1]+p[i-5]

T = int(stdin.readline())

for _ in range(1,T+1):
    
    n = int(stdin.readline())

    print(p[n])