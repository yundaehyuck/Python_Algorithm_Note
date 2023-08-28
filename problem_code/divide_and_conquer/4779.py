from sys import stdin

def cantor(n):
    
    if n == 1:
        
        return '-'
    
    else:
        
        return cantor(n//3) + ' '*(n//3) + cantor(n//3)

while 1:
    
    try:

        n = int(stdin.readline())

        print(cantor(3**n))

    except:
        
        break