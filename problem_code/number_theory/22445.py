#111111.... = 10^p-2 + 10^p-3 + ... + 10 + 1 = (10^p-1 - 1)/(10-1) mod p 
#p와 2,3,5가 서로소이면 무조건 0
#서로소가 아니라면 직접 구해준다
n = int(input())

if n == 0 or n == 2:
    
    print(1)

elif n == 1:
    
    print(2)

else:
    
    print(0)