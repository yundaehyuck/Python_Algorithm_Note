#마지막 n개의 비트가 모두 켜져있는가?
#2^n으로 나눈 나머지가 2^n-1이어야 한다.
T = int(input())

for test_case in range(1, T + 1):
    
    n,m = map(int,input().split())

    if  m % (2**n)== 2**n-1:
        
        print(f'#{test_case} ON')
    
    else:
        
        print(f'#{test_case} OFF')

#(1 << i) & m == 1이면 m의 i번째 비트가 켜져있다.
"""
T = int(input())

for test_case in range(1, T + 1):
    
    n,m = map(int,input().split())
    
    no = False
    
    for i in range(n):
        
        if (1 << i) & m == 0:
            
            no = True
            break
    
    if no:
        
        print(f'#{test_case} OFF')
    
    else:
        
        print(f'#{test_case} ON')
"""