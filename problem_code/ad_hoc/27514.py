import math

n = int(input())

a = list(map(int,input().split()))

print(2**int(math.log2(sum(a))))