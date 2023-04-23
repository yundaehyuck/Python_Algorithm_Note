from sys import stdin

while 1:
    
    try:

        n = int(stdin.readline())

        i = len(str(n))

        x = int('1'*i) % n

        while x != 0:
            
            x *= 10
            x += 1
            i += 1
            x %= n
            
        print(i)

    except:
        
        break