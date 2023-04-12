from sys import stdin

n = int(stdin.readline())

prod = 1

for i in range(1,n+1):
    
    prod *= i

    ##마지막이 0을 제거
    while prod % 10 == 0:
        
        prod //= 10
    
    #너무 수가 커지면 느려지므로 7자리만 확보하기 위함
    prod %= (10**7)

print(prod % 10)