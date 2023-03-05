from sys import stdin

n = int(stdin.readline())

num_list = list(map(int,stdin.readline().split()))

answer = []

for i in num_list:
    
    #because of floor error in very large number, 
    if (int(i**(1/2))**2 == i):
        
        print(1,end=' ')
    
    else:
        
        print(0,end=' ')