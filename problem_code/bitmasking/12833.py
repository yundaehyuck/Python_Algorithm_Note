from sys import stdin

a,b,c = map(int,stdin.readline().split())

if c % 2 == 1:
    
    a = a ^ b

print(a)