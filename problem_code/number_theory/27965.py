from sys import stdin
import math

n,k = map(int,stdin.readline().split())

div = 1

for i in range(2,n+1):
    
    div *= (10**(int(math.log10(i))+1))
    div += i
    div %= k

print(div % k)