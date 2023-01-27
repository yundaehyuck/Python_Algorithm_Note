from sys import stdin

n = int(stdin.readline())

house = list(map(int,stdin.readline().split()))

house.sort()

if n % 2 == 0:
    
    print(house[n//2-1])

else:
    
    print(house[n//2])