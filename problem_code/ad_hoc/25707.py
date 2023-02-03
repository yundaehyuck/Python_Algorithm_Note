from sys import stdin

n = int(stdin.readline())

ball = list(map(int,stdin.readline().split()))

ball.sort()

print(2*(ball[-1]-ball[0]))