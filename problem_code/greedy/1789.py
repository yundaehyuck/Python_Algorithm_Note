from sys import stdin

s = int(stdin.readline())

answer = int((-1+(1+8*s)**(1/2))/2)

print(answer)