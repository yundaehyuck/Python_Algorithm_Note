from sys import stdin

n = int(stdin.readline())

pointX = []
pointY = []

for _ in range(n):
    
    x,y = map(int,stdin.readline().split())

    pointX.append(x)
    pointY.append(y)


pointX.append(pointX[0])
pointY.append(pointY[0])

summation = 0

for i in range(n):
    
    summation += pointX[i]*pointY[i+1]
    summation -= pointY[i]*pointX[i+1]

print(f"{abs(summation)/2:.1f}")