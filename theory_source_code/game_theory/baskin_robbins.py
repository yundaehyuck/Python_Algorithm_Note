from sys import stdin

n,m = map(int,stdin.readline().split())

if (n-1)%(m+1) >= 1:
    
    print("Can win")

else:
    
    print(("Can't win"))